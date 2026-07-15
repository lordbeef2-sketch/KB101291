# NI OSS SOURCE SNAPSHOT: nidaqmx-python

<!--NI_OSS_SNAPSHOT repo=ni/nidaqmx-python commit=03282e1b5c741b9f37e4a4e1b5de3a52ae72442e -->

<!--NI_OSS_SOURCE repo=nidaqmx-python path=.config/cspell/daqmx-api-elements.txt sha256=12ee8ae31960785ab1a34317018a9afdb43301d8fa8b8b3267903fe882b405b3 bytes=6126 -->
## FILE: .config/cspell/daqmx-api-elements.txt

- repository: `ni/nidaqmx-python`
- source_path: `.config/cspell/daqmx-api-elements.txt`
- sha256: `12ee8ae31960785ab1a34317018a9afdb43301d8fa8b8b3267903fe882b405b3`
- bytes: 6126

````text
acceld                # Deprecated; see attribute_helpers.py
ACRMS                 # unseparated initialisms; AC RMS
AHigh                 # unseparated words; A high
AIAC                  # unseparated initialisms; AI AC
AIADC                 # unseparated initialisms; AI ADC
AIDC                  # unseparated initialisms; AI DC
AIGnd                 # unseparated words; AI ground
AILVDT                # unseparated initialisms; AI LVDT
AIRTD                 # unseparated initialisms; AI RTD
AIRTDA                # unseparated initialisms; AI RTD A
AIRTDB                # unseparated initialisms; AI RTD B
AIRTDC                # unseparated initialisms; AI RTD C
AIRTDR0               # unseparated initialisms; AI RTD R0
AIRVDT                # unseparated initialisms; AI RVDT
AITEDS                # unseparated initialisms; AI TEDS
anlg                  # abbreviation; analog
AODAC                 # unseparated initialisms; AO DAC
AOGnd                 # unseparated words; AO ground
AOHW                  # unseparated initialisms; AO HW
APFI                  # initialism; Analog Programmable Function Interface
asyn                  # abbreviation; asynchronous
atten                 # abbreviation; attenuation
attentuation          # Typo; should be: attenuation
BBULK                 # Typo; should be USB_BULK instead of US_BBULK
BHigh                 # unseparated words; B high
calibrationInfo       # unseparated words
CAPI                  # unseparated words; C API
certiticates          # Typo; should be: certificates
cfgd                  # abbreviation; configured
cfgs                  # abbreviation; configurations
chans                 # abbreviation; channels
CIGPS                 # unseparated initialisms; CI GPS
CIHW                  # unseparated initialisms; CI HW
CITC                  # unseparated initialisms; CI TC
CIUTC                 # unseparated initialisms; CI UTC
clks                  # abbreviation; clocks
cmplt                 # abbreviation; complete
coeff                 # abbreviation; coefficient
coeffs                # abbreviation; coefficients
COHW                  # unseparated initialisms; CO HW
COHWTSP               # unseparated initialisms; CO HWTSP
compen                # abbreviation; compensated / compensation
conv                  # abbreviation; convert
couldnt               # abbreviation; couldn't
ctrs                  # abbreviation; counters
DAQError              # unseparated words
descr                 # abbreviation; description
difft                 # abbreviation; different
doesnt                # abbreviation; doesn't
DSTAR                 # for further research; stands for differential star (PXIe trigger), but we also use D_STAR
elec                  # abbreviation; electrical
excit                 # abbreviation; excitation
expir                 # abbreviation; expiration
exportSignal          # unseparated words
fltr                  # abbreviation; filter
forceLb               # unseparated words; force in pounds
freqOut               # abbreviation; frequency output
frequencyWith         # unseparated words
globalVirtualChannels # unseparated words; global virtual channels
hshk                  # abbreviation; handshake
HWTEDS                # unseparated initialisms; HW TEDS
HWTSP                 # initialism; Hardware-Timed Single Point
hyst                  # abbreviation; hysteresis
hysts                 # abbreviation; hysteresis
immed                 # abbreviation; immediate
invalidc              # Typo; should be: INVALID_CDAQ_SYNC_PORT_CONNECTION_FORMAT
IRIGB                 # initialism; IRIG-B
isoc                  # abbreviation; isochronous
lvls                  # abbreviation; levels
MIOAI                 # unseparated initialisms; MIO AI
mult                  # abbreviation; multiple
multiDevice           # unseparated words
NIDAQ                 # initialism; NI-DAQ (legacy product name)
nidaqmx               # NI-DAQmx package name
nonBuffered           # unseparated words
notKnown              # unseparated words
NRSE                  # initialism; Non-Referenced Single-Ended
nums                  # abbreviation; numbers
onbrd                 # abbreviation; onboard
outp                  # abbreviation; output
persistedChannel      # unseparated words
persistedScale        # unseparated words
persistedTask         # unseparated words
physicalChannel       # unseparated words
posssible             # Typo; should be: possible
pretrig               # abbreviation; pre-trigger
prpty                 # abbreviation; property
rangeWith             # unseparated words
regen                 # abbreviation; regeneration
rngs                  # abbreviation; ranges
rqst                  # abbreviation; request
samp                  # abbreviation; sample
samps                 # abbreviation; samples
scanList              # unseparated words
sensord               # Deprecated; see attribute_helpers.py
sensitivit            # Typo; should be: sensitivity
SMIO                  # initialism; Simultaneously-sampling Multifunction I/O
specd                 # abbreviation; specified
srcs                  # abbreviation; sources
subsytem              # Typo; should be: subsystem
taskToCopy            # unseparated words; task to copy
tcpip                 # initialism; TCP/IP
TEDSAI                # unseparated initialisms; TEDS AI
TEDSAIRTD             # unseparated initialisms; TEDS AI RTD
TEDSHWTEDS            # unseparated initialisms; TEDS HWTEDS
thrmcpl               # abbreviation; thermocouple
thrmstr               # abbreviation; thermistor
timeTriggers          # unseparated words
trigs                 # abbreviation; triggers
unavail               # abbreviation; unavailable
USBDAQ                # unseparated initialisms; USB DAQ
verif                 # abbreviation; verification
voltaged              # Deprecated; see attribute_helpers.py
xfer                  # abbreviation; transfer
ZIdx                  # abbreviation; Z index
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=.config/cspell/mako-keywords.txt sha256=1e411ba1608d94ccfd4fa1fb15c20b4b05189681dac106d05367615c1ee4b523 bytes=299 -->
## FILE: .config/cspell/mako-keywords.txt

- repository: `ni/nidaqmx-python`
- source_path: `.config/cspell/mako-keywords.txt`
- sha256: `1e411ba1608d94ccfd4fa1fb15c20b4b05189681dac106d05367615c1ee4b523`
- bytes: 299

````text
# Mako template closing keywords for control structures (% endXXX markers).
# Mako closes each % control block with a matching % end<keyword> line.
# All seven closing keywords are included; they are all used in src/codegen/templates/.
endblock
enddef
endfor
endif
endtry
endwhile
endwith
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=.config/cspell/project-software-terms.txt sha256=5e26e7d39b73dc92f4a62d4b3560f62fdd4404a8203ed225e861ac1872b1c76d bytes=3066 -->
## FILE: .config/cspell/project-software-terms.txt

- repository: `ni/nidaqmx-python`
- source_path: `.config/cspell/project-software-terms.txt`
- sha256: `5e26e7d39b73dc92f4a62d4b3560f62fdd4404a8203ed225e861ac1872b1c76d`
- bytes: 3066

````text
addoption         # Dependency: pytest
allclose          # Dependency: numpy
argtype           # Standard library: ctypes
argtypes          # Standard library: ctypes
ascontiguousarray # Dependency: numpy
autoinstall       # Linux system tool names (external)
byref             # Standard library: ctypes
callspec          # Dependency: pytest
caplog            # Dependency: pytest
cdecl             # C calling convention name (used in codegen)
chkconfig         # Linux system tool names (external)
codegen           # codegen internals
ctypes            # Standard library: ctypes
ctypeslib         # Standard library: ctypes
CVICALLBACK       # NI CVI calling convention macro (C interop comment)
docstrings        # Python terminology
dotenv            # Dependency: python-decouple / dotenv
dpkg              # Linux system tool names (external)
dtype             # Dependency: numpy
fixturenames      # Dependency: pytest
frombuffer        # Dependency: numpy
getfixturevalue   # Dependency: pytest
grpcdevice        # NI package name; ni-grpcdevice
hightime          # Dependency: hightime
htmlcov           # Python tooling (directory/artifact names, not real words)
iinfo             # Dependency: numpy
insserv           # Linux system tool names (external)
installdriver     # CLI command name and corresponding function
localzone         # Dependency: tzlocal
matplotlib        # Dependency: matplotlib
metafunc          # Dependency: pytest
modifyitems       # Dependency: pytest
nbytes            # Dependency: numpy
ndarray           # Dependency: numpy
ndpointer         # Dependency: numpy
NISHAREDDIR       # NI Linux install directory environment variable
nicai             # NI-DAQmx C library filename (Windows DLL)
nicaiu            # NI-DAQmx C library filename (Windows DLL, Unicode)
nidevice          # NI package name; ni-device-grpc
nitypes           # Dependency: nitypes
nptdms            # Dependency: nptdms
numpy             # Dependency: numpy
parametrizing     # Dependency: pytest
printoptions      # Dependency: numpy
protoc            # Tool name: protobuf compiler
pycache           # Python tooling (directory/artifact names, not real words)
pykka             # Dependency: pykka
pyplot            # Dependency: matplotlib
pytest            # Dependency: pytest
rtol              # Dependency: numpy
scrapigen         # codegen internals
styleguide        # ni-python-styleguide linting tool
sint              # Protobuf type; signed integer
tobytes           # Dependency: numpy
tolist            # Dependency: numpy
typeshed          # Python type stubs repository (mypy/pyright tooling)
unraisable        # Dependency: pytest
unraisablehook    # Dependency: pytest
ulonglong         # C type: unsigned long long
varargs           # Standard library: ctypes
venv              # Python tooling (directory/artifact names, not real words)
xlabel            # Dependency: matplotlib
ylabel            # Dependency: matplotlib
zizmor            # Dependency: zizmor
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=.config/cspell/real-words.txt sha256=856109aeff56e247612b1de252005e5dcaf0b596ab0c42e108494c5b8d957d53 bytes=4227 -->
## FILE: .config/cspell/real-words.txt

- repository: `ni/nidaqmx-python`
- source_path: `.config/cspell/real-words.txt`
- sha256: `856109aeff56e247612b1de252005e5dcaf0b596ab0c42e108494c5b8d957d53`
- bytes: 4227

````text
autozero            # Electronic instrumentation term
backplane           # Digital electronics and computer engineering term
bandpass            # Filter term
bitfield            # Computing term; contiguous range of bits in a value
bitfields           # Computing term; contiguous range of bits in a value
bitstream           # Computing term; sequence of bits transmitted serially
brickwall           # Filter term
Butterworth         # Scientist name; Butterworth filter
cDAQ                # CompactDAQ (NI hardware platform)
Callendar           # Physicist name; Callendar-Van Dusen equation
CPLD                # Complex Programmable Logic Device
DAQmx               # Data Acquisition Measurement Extensions
deassert            # Digital electronics and computer engineering term
deasserting         # Digital electronics and computer engineering term
deasserts           # Digital electronics and computer engineering term
deleters            # Software term
DKMS                # Dynamic Kernel Module Support
Dusen               # Physicist name; Van Dusen of Callendar-Van Dusen equation
EEPROM              # Electrically Erasable Programmable Read-Only Memory
HDOP                # Horizontal Dilution of Precision (GPS)
highpass            # Filter term
HWCU                # Hardware Configuration Utility
IEPE                # Integrated Electronics Piezo-Electric
IRIG                # Inter-Range Instrumentation Group
jumpered            # Electronics term
lowpass             # Filter term
LVDT                # Linear Variable Differential Transformer
LVTTL               # Low Voltage Transistor-Transistor Logic
MBCS                # Multi-Byte Character Set
MDNS                # Multicast DNS
MeasurementLink     # NI product name
micropascals        # Unit of pressure
mioDAQ              # NI product category
milli               # SI prefix
multibyte           # Computing term; character encoding using multiple bytes
NIELVIS             # NI product name; NI ELVIS
nonprintable        # Computing term
overcurrent         # Electrical engineering term
overrange           # Measurement term; signal exceeding the measurable range
overread            # Data acquisition term
overtemperature     # Electrical/safety term; exceeding a temperature limit
overvoltage         # Electrical engineering term
PDOP                # Position Dilution of Precision (GPS)
pico                # SI prefix
powerline           # Electrical engineering term
powerup             # Electronics term
pseudodifferential  # Electronics measurement term
PXIe                # PCI eXtensions for Instrumentation, Express variant
ratiometric         # Electronics measurement term
RDMA                # Remote Direct Memory Access
readall             # Software term; read all available data
reglitch            # Electronics DAC term
reglitching         # Electronics DAC term (gerund)
replug              # Hardware term
retriggerable       # Electronics term; able to be triggered again before previous cycle ends
RTSI                # Real-Time System Integration
RVDT                # Rotary Variable Differential Transformer
SCXI                # Signal Conditioning eXtensions for Instrumentation
Steinhart           # Physicist name; Steinhart-Hart thermistor equation
stopband            # Filter term
subsecond           # Time measurement term; less than one second
subseconds          # Time measurement term; less than one second
TDMS                # Technical Data Management Streaming
timebase            # Electronics term; reference clock signal
timebases           # Electronics term
tristated           # Electronics term
tristates           # Electronics term (verb/noun)
unflatten           # Software term; deserialize/reconstruct nested data
unloadable          # Computing term
unreserve           # Software term; release a reserved resource
unreserves          # Software term; release a reserved resource
VCXO                # Voltage-Controlled Crystal Oscillator
VDOP                # Vertical Dilution of Precision (GPS)
yoctosecond         # Unit of time; SI prefix
yoctoseconds        # Unit of time; SI prefix
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=.config/cspell/sphinx-directives.txt sha256=7db7939f7467db96b8e808e9a786e01bf7888a3c5b5ff4903b3d702d3aa28391 bytes=355 -->
## FILE: .config/cspell/sphinx-directives.txt

- repository: `ni/nidaqmx-python`
- source_path: `.config/cspell/sphinx-directives.txt`
- sha256: `7db7939f7467db96b8e808e9a786e01bf7888a3c5b5ff4903b3d702d3aa28391`
- bytes: 355

````text
# Sphinx directive names and option values flagged by cspell in this project's .rst files.
# This is not an exhaustive list of Sphinx directives — only words that cspell does not
# recognize from its built-in dictionaries and that appear in docs/ are included here.
automodule
backlinks
bysource
currentmodule
genindex
modindex
toctree
undoc
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=.config/cspell.json sha256=d5ba0cc4f966d0fb81429e5cb7b72e0361b836e23377d990693be2e82876e27c bytes=2294 -->
## FILE: .config/cspell.json

- repository: `ni/nidaqmx-python`
- source_path: `.config/cspell.json`
- sha256: `d5ba0cc4f966d0fb81429e5cb7b72e0361b836e23377d990693be2e82876e27c`
- bytes: 2294

````json
{
  "version": "0.2",
  "globRoot": "${cwd}",
  // Keep the following list of items in alphabetical order.
  "dictionaryDefinitions": [
    { "name": "daqmx-api-elements", "path": "./cspell/daqmx-api-elements.txt", "noSuggest": true },
    { "name": "real-words", "path": "./cspell/real-words.txt", "noSuggest": false },
    { "name": "mako-keywords", "path": "./cspell/mako-keywords.txt", "noSuggest": true },
    { "name": "project-software-terms", "path": "./cspell/project-software-terms.txt", "noSuggest": true },
    { "name": "sphinx-directives", "path": "./cspell/sphinx-directives.txt", "noSuggest": true }
  ],
  "dictionaries": ["real-words", "daqmx-api-elements", "project-software-terms", "python"],
  "useGitignore": true,
  // Keep the following list of items in the order that they appear in VSCode
  // Explorer (directories in alphabetical order, followed by top-level files
  // in alphabetical order).
  "ignorePaths": [
    ".config/cspell/**",           // dictionary source files; words here are not prose
    "docs/img/**",                 // binary image files
    "docs/conf.py",                // Sphinx config; extension names and config keys
    "docs/make.bat",               // Sphinx build script; not prose
    "docs/Makefile",               // Sphinx build script; not prose
    "generated/nidaqmx/_stubs/**", // protobuf-generated stubs; too noisy to check
    "tests/max_config/**",         // NI MAX config files; NI-specific identifiers
    "tests/test_assets/**",        // test fixture files; not prose
    "third_party/**",              // third-party code we don't own or control
    ".readthedocs.yml",            // ReadTheDocs config
    "poetry.lock",                 // auto-generated lock file; hashes and package URLs
    "poetry.toml",                 // Poetry config
    "tox.ini"                      // tox config
  ],
  "overrides": [
    {
      "filename": "**/*.mako",
      "dictionaries": ["real-words", "daqmx-api-elements", "python", "mako-keywords"]
    },
    {
      "filename": "**/*.rst",
      "dictionaries": ["real-words", "daqmx-api-elements", "python", "sphinx-directives"]
    },
    {
      "filename": "**/CONTRIBUTING.md",
      "dictionaries": ["real-words"]
    }
  ]
}
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=.env.sample sha256=d637fd5bf4f9f17d9ddb22f4dff575e62ba4673120364acc201f719f3c3311f1 bytes=641 -->
## FILE: .env.sample

- repository: `ni/nidaqmx-python`
- source_path: `.env.sample`
- sha256: `d637fd5bf4f9f17d9ddb22f4dff575e62ba4673120364acc201f719f3c3311f1`
- bytes: 641

````text
# This is a sample nidaqmx-python configuration file.

# To use it:
# - Copy this file to your application's directory or one of its parent directories
#   (such as the root of your Git repository).
# - Rename it to `.env`.
# - Uncomment and edit the options you want to change.
# - Restart any affected applications or services.

# By default, nidaqmx-python on Windows uses nicai_utf8, the UTF-8 version of the NI-DAQmx C library.
# If that is not available, it falls back to nicaiu, the MBCS (multibyte character set) version. You can override
# this behavior by uncommenting the following option:

# NIDAQMX_C_LIBRARY=nicaiu
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=.github/CODEOWNERS sha256=37e716e8a1aef9b673f719418ab4c627e08f1c6ecd9e85d63eee56df2f14824a bytes=31 -->
## FILE: .github/CODEOWNERS

- repository: `ni/nidaqmx-python`
- source_path: `.github/CODEOWNERS`
- sha256: `37e716e8a1aef9b673f719418ab4c627e08f1c6ecd9e85d63eee56df2f14824a`
- bytes: 31

````text
* @zhindes @maxxboehme @bkeryan
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=.github/ISSUE_TEMPLATE/bug_report.md sha256=9e4621832b9fdad470452f32a83c20f0e1d8278595b68e6b5ac0f4e9d6f44c39 bytes=1503 -->
## FILE: .github/ISSUE_TEMPLATE/bug_report.md

- repository: `ni/nidaqmx-python`
- source_path: `.github/ISSUE_TEMPLATE/bug_report.md`
- sha256: `9e4621832b9fdad470452f32a83c20f0e1d8278595b68e6b5ac0f4e9d6f44c39`
- bytes: 1503

````markdown
---
name: Bug report
about: Create a report to help us improve
title: ''
labels: 'bug,triage'
---

<!---
Thanks for filing an issue! Before you submit, please read the following:

Search open/closed issues before submitting. Someone may have reported the same issue before.
-->

# Bug Report

<!--- Provide a general summary of the issue here -->

## Repro or Code Sample

<!-- Please provide steps to reproduce the issue and/or a code repository, gist, code snippet or sample files -->

## Expected Behavior

<!--- Tell us what should happen -->

## Current Behavior

<!--- Tell us what happens instead of the expected behavior -->
<!--- If you are seeing an error, please include the full error message and stack trace -->
<!--- If applicable, provide screenshots -->

## Possible Solution

<!--- Not obligatory, but suggest a fix/reason for the bug -->
<!--- Please let us know if you'd be willing to contribute the fix; we'd be happy to work with you -->

## Context

<!--- How has this issue affected you? What are you trying to accomplish? -->
<!--- Providing context helps us come up with a solution that is most useful in the real world -->

## Your Environment

<!--- Include as many relevant details as possible about the environment you experienced the bug in -->

* Operating system and version: [e.g. Windows 11 24H2, Ubuntu Linux 24.04]
* NI-DAQmx version: [e.g. 2024 Q4]
* `nidaqmx-python` version: [e.g. 1.0.1]
* Python version [e.g. 3.11]
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=.github/ISSUE_TEMPLATE/feature_request.md sha256=e00ddb5b02a84de7f991b8a86a1bc750d91141603aad727f2a85d4c0bc8be6b1 bytes=712 -->
## FILE: .github/ISSUE_TEMPLATE/feature_request.md

- repository: `ni/nidaqmx-python`
- source_path: `.github/ISSUE_TEMPLATE/feature_request.md`
- sha256: `e00ddb5b02a84de7f991b8a86a1bc750d91141603aad727f2a85d4c0bc8be6b1`
- bytes: 712

````markdown
---
name: Feature request
about: Suggest an idea for this project
title: ''
labels: 'enhancement,triage'
---

<!---
Thanks for filing an issue! Before you submit, please read the following:

Search open/closed issues before submitting. Someone may have requested the same feature before.
-->

## Problem to Solve

<!--- Provide a clear and concise description of why this feature is wanted or what problem it solves. -->

## Proposed Solution

<!--- Provide a clear and concise description of the feature you're proposing. -->

<!--- The implementing team may build a list of tasks/sub-issues here:
## Tasks
- [ ] This is a subtask of the feature. (It can be converted to an issue.)
-->
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=.github/ISSUE_TEMPLATE/tech_debt.md sha256=a80e6afbbd5f723466dab578104fedfe7d38413e65714a4e5ccb40d1d35389d0 bytes=164 -->
## FILE: .github/ISSUE_TEMPLATE/tech_debt.md

- repository: `ni/nidaqmx-python`
- source_path: `.github/ISSUE_TEMPLATE/tech_debt.md`
- sha256: `a80e6afbbd5f723466dab578104fedfe7d38413e65714a4e5ccb40d1d35389d0`
- bytes: 164

````markdown
---
name: Tech debt
about: (DEV TEAM ONLY) Non-user-visible improvement to code or development process
title: ''
labels: 'tech debt,triage'
---
## Tech Debt
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=.github/ISSUE_TEMPLATE/user_story.md sha256=db24cb4a5576436f0dd3e0fbfd2d95a20336d2aa1c5d68cddbd5a717dc993012 bytes=321 -->
## FILE: .github/ISSUE_TEMPLATE/user_story.md

- repository: `ni/nidaqmx-python`
- source_path: `.github/ISSUE_TEMPLATE/user_story.md`
- sha256: `db24cb4a5576436f0dd3e0fbfd2d95a20336d2aa1c5d68cddbd5a717dc993012`
- bytes: 321

````markdown
---
name: User story
about: (DEV TEAM ONLY) A small chunk of work to be done
title: '(Fully descriptive title)'
labels: 'user story,triage'
---

<!-- Ensure the title can be understood without the parent item's context, e.g. "nimble-button Angular wrapper" rather than just "Angular wrapper" -->

## User Story
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=.github/PULL_REQUEST_TEMPLATE.md sha256=b05587eb2428f980ceb96494ddfe746490dd09fbd85ebc8ce8f37b3c5f5059e3 bytes=1283 -->
## FILE: .github/PULL_REQUEST_TEMPLATE.md

- repository: `ni/nidaqmx-python`
- source_path: `.github/PULL_REQUEST_TEMPLATE.md`
- sha256: `b05587eb2428f980ceb96494ddfe746490dd09fbd85ebc8ce8f37b3c5f5059e3`
- bytes: 1283

````markdown
- [ ] This contribution adheres to [CONTRIBUTING.md](https://github.com/ni/nidaqmx-python/blob/master/CONTRIBUTING.md).

TODO: Check the above box with an 'x' indicating you've read and followed [CONTRIBUTING.md](https://github.com/ni/nidaqmx-python/blob/master/CONTRIBUTING.md).

- [ ] I've updated [CHANGELOG.md](https://github.com/ni/nidaqmx-python/blob/master/CHANGELOG.md) if applicable.

TODO: Check the above box with an 'x' if considered if there were any and then documented client facing changes in [CHANGELOG.md](https://github.com/ni/nidaqmx-python/blob/master/CHANGELOG.md). Strike through if this is not a relevant client facing change.

- [ ] I've added tests applicable for this pull request

TODO: Check the above box with an 'x' indicating you have considered and added any applicable system or unit tests. Strike through if you considered and decided additional tests were not warranted.

### What does this Pull Request accomplish?

TODO: Include high-level description of the changes in this pull request.

### Why should this Pull Request be merged?

TODO: Justify why this contribution should be part of the project.

### What testing has been done?

TODO: Detail what testing has been done to ensure this submission meets requirements.
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=.github/renovate.json sha256=60909f4835c7ec398d2e67ef80b54755d8288f94e525c80d00865267c91128c2 bytes=153 -->
## FILE: .github/renovate.json

- repository: `ni/nidaqmx-python`
- source_path: `.github/renovate.json`
- sha256: `60909f4835c7ec398d2e67ef80b54755d8288f94e525c80d00865267c91128c2`
- bytes: 153

````json
{
    "$schema": "https://docs.renovatebot.com/renovate-schema.json",
    "extends": [
        "local>ni/python-renovate-config:recommended"
    ]
}
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=.github/workflows/build.yml sha256=caaa65e0621aab25a2fd8d6aa8a6b60fb265006f4cc46ed6a775220e7ebc9f0b bytes=1886 -->
## FILE: .github/workflows/build.yml

- repository: `ni/nidaqmx-python`
- source_path: `.github/workflows/build.yml`
- sha256: `caaa65e0621aab25a2fd8d6aa8a6b60fb265006f4cc46ed6a775220e7ebc9f0b`
- bytes: 1886

````yaml
name: Build

on:
  workflow_call:
  workflow_dispatch:

permissions: {}

jobs:
  build:
    name: Build
    runs-on:
      - ${{ matrix.os }}
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest]
        python-version: ["3.9", "3.14"] # oldest supported and latest tested
    env:
      codegen-python-version: "3.9"
    steps:
      - name: Check out repo
        uses: actions/checkout@9c091bb21b7c1c1d1991bb908d89e4e9dddfe3e0 # v7.0.0
        with:
          submodules: true
          persist-credentials: false
      - name: Set up Python
        uses: ni/python-actions/setup-python@a2554c7e5680982d3355677b2290e48b60678744 # v0.8.0
        id: setup-python
        with:
          python-version: ${{ matrix.python-version }}
      - name: Set up Poetry
        uses: ni/python-actions/setup-poetry@a2554c7e5680982d3355677b2290e48b60678744 # v0.8.0
      - name: Run linters and type checkers
        uses: ni/python-actions/analyze-project@a2554c7e5680982d3355677b2290e48b60678744 # v0.8.0
        with:
          install-args: "--all-extras --with examples"
      - name: Run Bandit security checks
        run: poetry run bandit -c pyproject.toml -r generated/nidaqmx
      - name: Run cspell
        uses: streetsidesoftware/cspell-action@de2a73e963e7443969755b648a1008f77033c5b2 # v8.4.0
        with:
          incremental_files_only: false
          check_dot_files: explicit
      - name: Generate ni-daqmx files
        if: ${{ runner.os == 'Linux' && matrix.python-version == env.codegen-python-version }}
        run: |
          rm -fr generated/nidaqmx
          poetry run python src/codegen --dest generated/nidaqmx
      - name: Check for files dirtied by codegen
        if: ${{ runner.os == 'Linux' && matrix.python-version == env.codegen-python-version }}
        run: git diff --exit-code
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=.github/workflows/check_workflows.yml sha256=e00c7fb6d0a5207cb751edb5b39eeb643512d2e4de96419e8fc6cbdbbd9601c1 bytes=498 -->
## FILE: .github/workflows/check_workflows.yml

- repository: `ni/nidaqmx-python`
- source_path: `.github/workflows/check_workflows.yml`
- sha256: `e00c7fb6d0a5207cb751edb5b39eeb643512d2e4de96419e8fc6cbdbbd9601c1`
- bytes: 498

````yaml
name: Check workflows

on:
  workflow_call:
  workflow_dispatch:

permissions: {}

jobs:
  zizmor:
    name: Run zizmor
    runs-on: ubuntu-latest
    permissions:
      security-events: write
    steps:
      - name: Check out repo
        uses: actions/checkout@9c091bb21b7c1c1d1991bb908d89e4e9dddfe3e0 # v7.0.0
        with:
          persist-credentials: false
      - name: Run zizmor
        uses: zizmorcore/zizmor-action@192e21d79ab29983730a13d1382995c2307fbcaa # v0.5.7
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=.github/workflows/CI.yml sha256=0d1330b255afd55d447994823b4aaee09e2a9fa9df9c8af3f949f3c49e3c5782 bytes=990 -->
## FILE: .github/workflows/CI.yml

- repository: `ni/nidaqmx-python`
- source_path: `.github/workflows/CI.yml`
- sha256: `0d1330b255afd55d447994823b4aaee09e2a9fa9df9c8af3f949f3c49e3c5782`
- bytes: 990

````yaml
name: CI

on:
  push:
    branches:
      - master
      - 'releases/**'
  workflow_call:
  workflow_dispatch:

permissions: {}

jobs:
  build:
    name: Build
    uses: ./.github/workflows/build.yml
  run_unit_tests:
    name: Run unit tests
    uses: ./.github/workflows/run_unit_tests.yml
    needs: [build]
  generate_docs:
    name: Generate docs
    uses: ./.github/workflows/generate_docs.yml
    needs: [build]
  check_workflows:
    name: Check workflows
    uses: ./.github/workflows/check_workflows.yml
    permissions:
      security-events: write
  run_system_tests:
    name: Run system tests
    uses: ./.github/workflows/run_system_tests.yml
    needs: [build, run_unit_tests]
  report_test_results:
    name: Report test results
    uses: ./.github/workflows/report_test_results.yml
    needs: [run_unit_tests, run_system_tests]
    if: always()
    permissions:
      contents: read
      checks: write
      pull-requests: write
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=.github/workflows/generate_docs.yml sha256=974bb9e47cdbbf02dd6514b0da6889c3e4a4058dfe89b3dd1c964bc5dc564b97 bytes=1133 -->
## FILE: .github/workflows/generate_docs.yml

- repository: `ni/nidaqmx-python`
- source_path: `.github/workflows/generate_docs.yml`
- sha256: `974bb9e47cdbbf02dd6514b0da6889c3e4a4058dfe89b3dd1c964bc5dc564b97`
- bytes: 1133

````yaml
name: Generate docs

on:
  workflow_call:
  workflow_dispatch:

permissions: {}

jobs:
  generate_docs:
    name: Generate docs
    runs-on:
      - ubuntu-latest
    steps:
      - name: Check out repo
        uses: actions/checkout@9c091bb21b7c1c1d1991bb908d89e4e9dddfe3e0 # v7.0.0
        with:
          persist-credentials: false
      - name: Set up Python
        uses: ni/python-actions/setup-python@a2554c7e5680982d3355677b2290e48b60678744 # v0.8.0
        id: setup-python
      - name: Set up Poetry
        uses: ni/python-actions/setup-poetry@a2554c7e5680982d3355677b2290e48b60678744 # v0.8.0
      - name: Cache virtualenvs
        uses: actions/cache@55cc8345863c7cc4c66a329aec7e433d2d1c52a9 # v6.1.0
        with:
          path: |
            .venv
            .tox
          key: generate-docs-${{ runner.os }}-py${{ steps.setup-python.outputs.python-version }}-${{ hashFiles('poetry.lock') }}
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          poetry install
      - name: Generate docs
        run: poetry run tox -e docs
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=.github/workflows/PR.yml sha256=edfc088f10a3bf29a7f2e203f0691dfd9f558d1c0dfbd16e89e43a7dc5256dec bytes=471 -->
## FILE: .github/workflows/PR.yml

- repository: `ni/nidaqmx-python`
- source_path: `.github/workflows/PR.yml`
- sha256: `edfc088f10a3bf29a7f2e203f0691dfd9f558d1c0dfbd16e89e43a7dc5256dec`
- bytes: 471

````yaml
name: PR

on:
  pull_request:
    branches:
      - master
      - 'releases/**'
  workflow_call:
  workflow_dispatch:

concurrency:
  group: ${{ github.workflow }}-${{ github.event.pull_request.number || github.ref }}
  cancel-in-progress: true

permissions: {}

jobs:
  run_ci:
    name: Run CI
    uses: ./.github/workflows/CI.yml
    permissions:
      contents: read
      checks: write
      pull-requests: write
      security-events: write
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=.github/workflows/publish.yml sha256=1be35a897a62f1ae97be5d35bf26d9cacf6168692057bd7d7730c479314c3d22 bytes=3776 -->
## FILE: .github/workflows/publish.yml

- repository: `ni/nidaqmx-python`
- source_path: `.github/workflows/publish.yml`
- sha256: `1be35a897a62f1ae97be5d35bf26d9cacf6168692057bd7d7730c479314c3d22`
- bytes: 3776

````yaml
name: Publish nidaqmx

on:
  release:
    types: [published]
  workflow_dispatch:
    inputs:
      environment:
        description: The environment to publish to.
        default: 'none'
        required: true
        type: choice
        options:
          - none
          - pypi
          - testpypi

env:
  dist-artifact-name: nidaqmx-distribution-packages
  environment: ${{ github.event_name == 'release' && 'pypi' || inputs.environment }}
  environment-info: |
    {
      "pypi": {
        "base-url": "https://pypi.org",
        "upload-url": "https://upload.pypi.org/legacy/"
      },
      "testpypi": {
        "base-url": "https://test.pypi.org",
        "upload-url": "https://test.pypi.org/legacy/"
      }
    }

permissions: {}

jobs:
  check_nidaqmx:
    name: Check nidaqmx
    uses: ./.github/workflows/build.yml
  check_docs:
    name: Check docs
    uses: ./.github/workflows/generate_docs.yml
  build_nidaqmx:
    name: Build nidaqmx
    runs-on: ubuntu-latest
    needs: [check_nidaqmx, check_docs]
    steps:
      - name: Check out repo
        uses: actions/checkout@9c091bb21b7c1c1d1991bb908d89e4e9dddfe3e0 # v7.0.0
        with:
          persist-credentials: false
      - name: Set up Python
        uses: ni/python-actions/setup-python@a2554c7e5680982d3355677b2290e48b60678744 # v0.8.0
      - name: Set up Poetry
        uses: ni/python-actions/setup-poetry@a2554c7e5680982d3355677b2290e48b60678744 # v0.8.0
        with:
          use-cache: false
      - name: Check project version
        if: github.event_name == 'release'
        uses: ni/python-actions/check-project-version@a2554c7e5680982d3355677b2290e48b60678744 # v0.8.0
      - name: Build distribution packages
        run: poetry build
      - name: Upload build artifacts
        uses: actions/upload-artifact@043fb46d1a93c77aae656e7c1c64a875d1fc6a0a # v7.0.1
        with:
          name: ${{ env.dist-artifact-name }}
          path: dist/*
  publish_to_pypi:
    name: Publish nidaqmx to PyPI
    if: github.event_name == 'release' || inputs.environment != 'none'
    runs-on: ubuntu-latest
    needs: [build_nidaqmx]
    environment:
      # This logic is duplicated because `name` doesn't support the `env` context.
      name: ${{ github.event_name == 'release' && 'pypi' || inputs.environment }}
      url: ${{ fromJson(env.environment-info)[env.environment].base-url }}/p/nidaqmx
    permissions:
      id-token: write
    steps:
    - name: Download build artifacts
      uses: actions/download-artifact@3e5f45b2cfb9172054b4087a40e8e0b5a5461e7c # v8.0.1
      with:
        name: ${{ env.dist-artifact-name }}
        path: dist/
    - run: ls -lR
    - name: Upload to ${{ env.environment }}
      uses: pypa/gh-action-pypi-publish@cef221092ed1bacb1cc03d23a2d87d1d172e277b # v1.14.0
      with:
        repository-url: ${{ fromJson(env.environment-info)[env.environment].upload-url }} 
  update_version:
    name: Update nidaqmx version
    runs-on: ubuntu-latest
    needs: [build_nidaqmx]
    permissions:
      contents: write
      pull-requests: write
    steps:
      - name: Check out repo
        uses: actions/checkout@9c091bb21b7c1c1d1991bb908d89e4e9dddfe3e0 # v7.0.0
        with:
          persist-credentials: false
      - name: Set up Python
        uses: ni/python-actions/setup-python@a2554c7e5680982d3355677b2290e48b60678744 # v0.8.0
      - name: Set up Poetry
        uses: ni/python-actions/setup-poetry@a2554c7e5680982d3355677b2290e48b60678744 # v0.8.0
        with:
          use-cache: false
      - name: Update project version
        uses: ni/python-actions/update-project-version@a2554c7e5680982d3355677b2290e48b60678744 # v0.8.0
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=.github/workflows/report_test_results.yml sha256=10261aad8ad731a1d887bdff275ddd992573dfb80a9dbc494be33133cb1ab7cc bytes=946 -->
## FILE: .github/workflows/report_test_results.yml

- repository: `ni/nidaqmx-python`
- source_path: `.github/workflows/report_test_results.yml`
- sha256: `10261aad8ad731a1d887bdff275ddd992573dfb80a9dbc494be33133cb1ab7cc`
- bytes: 946

````yaml
name: Report test results

on:
  workflow_call:
  workflow_dispatch:

permissions: {}

jobs:
  report_test_results:
    name: Report test results
    runs-on: ubuntu-latest
    permissions:
      contents: read
      checks: write
      pull-requests: write
    steps:
      - name: Check out repo
        uses: actions/checkout@9c091bb21b7c1c1d1991bb908d89e4e9dddfe3e0 # v7.0.0
        with:
          persist-credentials: false
      - name: Download test results
        uses: actions/download-artifact@3e5f45b2cfb9172054b4087a40e8e0b5a5461e7c # v8.0.1
        with:
          path: test_results
          pattern: test_results_*
          merge-multiple: true
      - name: List downloaded files
        run: ls -lR
      - name: Publish test results
        uses: EnricoMi/publish-unit-test-result-action@d0a4676d0e0b938bc201470d88276b7c74c712b3 # v2.24.0
        with:
          files: "test_results/*.xml"
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=.github/workflows/run_system_tests.yml sha256=8a4a07be5631cf4b072b47ac9f668ce5e08b521e93ea93d74cecd0451e4c59a7 bytes=2330 -->
## FILE: .github/workflows/run_system_tests.yml

- repository: `ni/nidaqmx-python`
- source_path: `.github/workflows/run_system_tests.yml`
- sha256: `8a4a07be5631cf4b072b47ac9f668ce5e08b521e93ea93d74cecd0451e4c59a7`
- bytes: 2330

````yaml
name: Run system tests

on:
  workflow_call:
  workflow_dispatch:

permissions: {}

jobs:
  run_system_tests:
    name: Run system tests
    runs-on:
      - self-hosted
      - windows
      - x64
      - rdss-nidaqmxbot-${{ matrix.configuration }}
    strategy:
      matrix:
        configuration: ["win-10-py32", "win-10-py64"]
      # Fail-fast skews the pass/fail ratio and seems to make pytest produce
      # incomplete JUnit XML results.
      fail-fast: false
    timeout-minutes: 90
    steps:
      - name: Check out repo
        uses: actions/checkout@9c091bb21b7c1c1d1991bb908d89e4e9dddfe3e0 # v7.0.0
        with:
          persist-credentials: false
      - name: Import DAQmx config
        run: C:\nidaqmxconfig\targets\win64U\x64\msvc-14.0\release\nidaqmxconfig.exe --eraseconfig --import tests\max_config\nidaqmxMaxConfig.ini
      - name: Set up Python
        uses: ni/python-actions/setup-python@a2554c7e5680982d3355677b2290e48b60678744 # v0.8.0
      - name: Set up Poetry
        uses: ni/python-actions/setup-poetry@a2554c7e5680982d3355677b2290e48b60678744 # v0.8.0
      - name: Cache virtualenvs
        uses: actions/cache@55cc8345863c7cc4c66a329aec7e433d2d1c52a9 # v6.1.0
        with:
          path: |
            .venv
            .tox
          key: run-system-tests-${{ runner.os }}-${{ matrix.configuration }}-${{ hashFiles('poetry.lock') }}
      - name: Install dependencies
        run: poetry install
      - name: Run system tests
        run: poetry run tox
      - name: Rename test results
        # TODO: Add Git Bash to the path on self-hosted Windows runners
        run: Get-ChildItem test_results/*.xml | Rename-Item -NewName { $_.Name -replace '.xml','-${{ matrix.configuration }}.xml' }
        if: always() && runner.os == 'Windows'
      - name: Rename test results
        run: |
          for result in test_results/*.xml; do
            mv $result ${result%.xml}-${{ matrix.configuration }}.xml
          done
        if: always() && runner.os != 'Windows'
      - name: Upload test results
        uses: actions/upload-artifact@043fb46d1a93c77aae656e7c1c64a875d1fc6a0a # v7.0.1
        with:
          name: test_results_system_${{ matrix.configuration }}
          path: test_results/*.xml
        if: always()
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=.github/workflows/run_unit_tests.yml sha256=06521643a487d82ac496eb2e4ac5279a8d2b27df6c64d257a27631d78aaa3725 bytes=3765 -->
## FILE: .github/workflows/run_unit_tests.yml

- repository: `ni/nidaqmx-python`
- source_path: `.github/workflows/run_unit_tests.yml`
- sha256: `06521643a487d82ac496eb2e4ac5279a8d2b27df6c64d257a27631d78aaa3725`
- bytes: 3765

````yaml
name: Run unit tests

on:
  workflow_call:
  workflow_dispatch:
    
permissions: {}

jobs:
  run_unit_tests:
    name: Run unit tests
    runs-on:
      - ${{ matrix.os }}
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest]
        python-version: ["3.9", "3.10", "3.11", "3.12", "3.13", "3.14", "3.14t", "pypy3.11"]
      # Fail-fast skews the pass/fail ratio and seems to make pytest produce
      # incomplete JUnit XML results.
      fail-fast: false
    env:
      # grpcio does not have binary wheels for pypy or free-threading, as of version 1.75.1.
      GRPC_SUPPORTED: ${{ case(
                            startsWith(matrix.python-version, 'pypy'), 'false',
                            endsWith(matrix.python-version, 't'), 'false',
                            'true'
                          ) }}
    steps:
      - name: Check out repo
        uses: actions/checkout@9c091bb21b7c1c1d1991bb908d89e4e9dddfe3e0 # v7.0.0
        with:
          persist-credentials: false
      - name: Set up Python ${{ matrix.python-version }}
        uses: ni/python-actions/setup-python@a2554c7e5680982d3355677b2290e48b60678744 # v0.8.0
        id: setup-python
        with:
          python-version: ${{ matrix.python-version }}
      - name: Set up Poetry
        uses: ni/python-actions/setup-poetry@a2554c7e5680982d3355677b2290e48b60678744 # v0.8.0
      - name: Cache virtualenv (with test dependencies)
        uses: actions/cache@55cc8345863c7cc4c66a329aec7e433d2d1c52a9 # v6.1.0
        with:
          path: .venv
          key: nidaqmx-with-test-${{ runner.os }}-py${{ steps.setup-python.outputs.python-version }}-${{ hashFiles('poetry.lock') }}
      - name: Install test dependencies
        run: poetry install --only main,test ${{ case(env.GRPC_SUPPORTED == 'true', '--extras grpc', '') }}
      - name: Run unit tests
        run: poetry run pytest -v --cov=generated/nidaqmx --junitxml=test_results/unit-${{ matrix.os }}-py${{ matrix.python-version }}.xml tests/unit ${{ case(env.GRPC_SUPPORTED == 'true', '', '-k "not grpc"') }}
      - name: Upload test results
        uses: actions/upload-artifact@043fb46d1a93c77aae656e7c1c64a875d1fc6a0a # v7.0.1
        with:
          name: test_results_unit_${{ matrix.os }}_py${{ matrix.python-version }}
          path: test_results/*.xml
        if: always()
  test_installdriver:
    name: Test installdriver
    runs-on:
      - ${{ matrix.os }}
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest]
        python-version: ["3.10", "3.13", "pypy3.11"]
    steps:
      - name: Check out repo
        uses: actions/checkout@9c091bb21b7c1c1d1991bb908d89e4e9dddfe3e0 # v7.0.0
        with:
          persist-credentials: false
      - name: Set up Python ${{ matrix.python-version }}
        uses: ni/python-actions/setup-python@a2554c7e5680982d3355677b2290e48b60678744 # v0.8.0
        id: setup-python
        with:
          python-version: ${{ matrix.python-version }}
      - name: Set up Poetry
        uses: ni/python-actions/setup-poetry@a2554c7e5680982d3355677b2290e48b60678744 # v0.8.0
      - name: Cache virtualenv (main only)
        uses: actions/cache@55cc8345863c7cc4c66a329aec7e433d2d1c52a9 # v6.1.0
        id: cache-nidaqmx-main-only
        with:
          path: .venv
          key: nidaqmx-main-only-${{ runner.os }}-py${{ steps.setup-python.outputs.python-version }}-${{ hashFiles('poetry.lock') }}
      - name: Install main package dependencies
        run: |
          python -m pip install --upgrade pip
          poetry install --only main
      - name: check installdriver subcommand can be invoked
        run: poetry run nidaqmx installdriver --help
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=.github/workflows/sync_github_issues_to_azdo.yml sha256=ad6d1b613badce5a290fd8119b5450a4e5d22f2e697723ae3f8f5920673f7971 bytes=1396 -->
## FILE: .github/workflows/sync_github_issues_to_azdo.yml

- repository: `ni/nidaqmx-python`
- source_path: `.github/workflows/sync_github_issues_to_azdo.yml`
- sha256: `ad6d1b613badce5a290fd8119b5450a4e5d22f2e697723ae3f8f5920673f7971`
- bytes: 1396

````yaml
name: Sync issue to Azure DevOps work item

on:
  issues:
    # Omit "labeled" and "unlabeled" to work around https://github.com/danhellem/github-actions-issue-to-work-item/issues/70
    types:
      [opened, edited, deleted, closed, reopened, assigned]
  issue_comment:
    types: [created, edited, deleted]

permissions: {}

jobs:
  alert:
    if: ${{ !github.event.issue.pull_request && github.event.issue.title != 'Dependency Dashboard' }}
    runs-on: ubuntu-latest
    steps:
      - uses: danhellem/github-actions-issue-to-work-item@45eb3b46e684f2acd2954f02ef70350c835ee4bb # v2.4
        env:
          ado_token: "${{ secrets.AZDO_WORK_ITEM_TOKEN }}"
          github_token: "${{ secrets.GH_REPO_TOKEN }}"
          ado_organization: "ni"
          ado_project: "DevCentral"
          ado_area_path: "DevCentral\\Product RnD\\Platform HW and SW\\Core SW and Drivers\\Platform HW and Drivers\\Drivers\\Venus"
          ado_wit: "${{ case(
            contains(github.event.issue.labels.*.name, 'enhancement') || contains(github.event.issue.labels.*.name, 'user story'), 'User Story',
            contains(github.event.issue.labels.*.name, 'tech debt'), 'Technical Debt',
            'Bug') }}"
          ado_new_state: "New"
          ado_active_state: "Active"
          ado_close_state: "Closed"
          ado_bypassrules: true
          log_level: 100
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=.gitignore sha256=1d280e36868b85ac99eef26f8a2867162cfd5f4a85021ed3e4968a785893873a bytes=244 -->
## FILE: .gitignore

- repository: `ni/nidaqmx-python`
- source_path: `.gitignore`
- sha256: `1d280e36868b85ac99eef26f8a2867162cfd5f4a85021ed3e4968a785893873a`
- bytes: 244

````text
# Byte-compiled / optimized / DLL files
__pycache__/

# Unit tests
.tox/
test_results/

# Coverage output
.coverage
htmlcov/

# Environments
.env
.venv

# Built artifacts
dist/
docs/_build/

# Common editor metadata
.vscode/
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=.gitmodules sha256=07c20115d1e3e99cc2e3911d005b6ddd8714eee0dda1a2e856c3ce33dc8a44d5 bytes=94 -->
## FILE: .gitmodules

- repository: `ni/nidaqmx-python`
- source_path: `.gitmodules`
- sha256: `07c20115d1e3e99cc2e3911d005b6ddd8714eee0dda1a2e856c3ce33dc8a44d5`
- bytes: 94

````text
[submodule "ni-apis"]
	path = third_party/ni-apis
	url = https://github.com/ni/ni-apis.git
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=.readthedocs.yml sha256=90a8fa406be9c009b40f536ab21143566ea61d235acf346e4d4788576e2c2c39 bytes=311 -->
## FILE: .readthedocs.yml

- repository: `ni/nidaqmx-python`
- source_path: `.readthedocs.yml`
- sha256: `90a8fa406be9c009b40f536ab21143566ea61d235acf346e4d4788576e2c2c39`
- bytes: 311

````yaml
# .readthedocs.yml

version: 2

build:
  os: ubuntu-24.04
  tools:
    python: "3.11"
  jobs:
    post_create_environment:
      - pip install poetry==2.1.4
    post_install:
      - VIRTUAL_ENV=$READTHEDOCS_VIRTUALENV_PATH poetry install --only main,docs

sphinx:
  configuration: docs/conf.py
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=CHANGELOG.md sha256=4ee222a25b9447622a6f4348975acb234f9a866912cdd9bad34a91b125b184cd bytes=22496 -->
## FILE: CHANGELOG.md

- repository: `ni/nidaqmx-python`
- source_path: `CHANGELOG.md`
- sha256: `4ee222a25b9447622a6f4348975acb234f9a866912cdd9bad34a91b125b184cd`
- bytes: 22496

````markdown
# Changelog
* [1.6.0](#160)
* [1.5.0](#150)
* [1.4.1](#141)
* [1.4.0](#140)
* [1.3.0](#130)
* [1.2.0](#120)
* [1.1.0](#110)
* [1.0.2](#102)
* [1.0.1](#101)
* [1.0.0](#100)
* [0.9.0](#090)
* [0.8.0](#080)
* [0.7.0](#070)
* [0.6.5](#065)
* [0.6.4](#064)
* [0.6.3](#063)
* [0.6.2](#062)
* [0.6.1](#061)
* [0.6.0](#060)
* [0.5.8](#058)
* [0.5.7](#057)
* [0.5.6](#056)
* [0.5.5](#055)
* [0.5.4](#054)
* [0.5.2](#052)
* [0.5.0](#050)

All notable changes to this project will be documented in this file.

## 1.6.0
* ### Merged Pull Requests
    * [Full changelog: 1.5.0...1.6.0](https://github.com/ni/nidaqmx-python/compare/1.5.0...1.6.0)

* ### Resolved Issues
    * ...

* ### Major Changes
    * [zizmor](https://zizmor.sh/) is now used for GitHub Actions static analysis.

* ### Known Issues
    * ...

## 1.5.0
* ### Merged Pull Requests
    * [Full changelog: 1.4.1...1.5.0](https://github.com/ni/nidaqmx-python/compare/1.4.1...1.5.0)

* ### Resolved Issues
    * [936: New example voltage_acq_int_clk_plot_wfm.py does not behave as expected](https://github.com/ni/nidaqmx-python/issues/936)

* ### Major Changes
    * [cspell](https://cspell.org/) is now used for spell checking.

* ### Known Issues
    * ...

## 1.4.1
* ### Merged Pull Requests
    * [Full changelog: 1.4.0...1.4.1](https://github.com/ni/nidaqmx-python/compare/1.4.0...1.4.1)

* ### Resolved Issues
    * ...

* ### Major Changes
    * Update installer metadata using DAQmx version 26.0.0

* ### Known Issues
    * ...

## 1.4.0
* ### Merged Pull Requests
    * [Full changelog: 1.3.0...1.4.0](https://github.com/ni/nidaqmx-python/compare/1.3.0...1.4.0)

* ### Resolved Issues
    * [24: Support Waveform Reads/Writes](https://github.com/ni/nidaqmx-python/issues/24)
    * [820: Create a synchronization example for TDMS logging](https://github.com/ni/nidaqmx-python/issues/820)
    <!-- cspell:ignore rdss nidaqmxbot -->
    * [862: docs tox env fails on rdss-nidaqmxbot-win-10-py32](https://github.com/ni/nidaqmx-python/issues/862)

* ### Major Changes
    * Added support for reading and writing Waveform data, including through gRPC using [NI gRPC Device Server](https://github.com/ni/grpc-device).
    * Add support for calculated power channels
    * Add support for A and C-type Thermocouples

* ### Known Issues
    * ...

## 1.3.0
* ### Merged Pull Requests
    * [Full changelog: 1.2.0...1.3.0](https://github.com/ni/nidaqmx-python/compare/1.2.0...1.3.0)

* ### Resolved Issues
    * [843: read methods use task.in_stream.channels_to_read, which is slow](https://github.com/ni/nidaqmx-python/issues/843)
    * [639: first_samp_timestamp_val property does not work because LibraryInterpreter is missing a method](https://github.com/ni/nidaqmx-python/issues/639)

* ### Major Changes
    * (IN PROGRESS behind "WAVEFORM_SUPPORT" feature toggle) Added support for reading and writing Waveform data.
    * Simplify `numpy` and `click` version constraints.
        * `nidaqmx` supports a wider range of Python versions than `numpy` and `click`, so testing
          `nidaqmx` against its oldest supported Python version (currently 3.9) requires downgrading
          to older versions of `numpy` and `click`.
        * Previously, these testing-specific version constraints leaked into to the `nidaqmx`
          distribution package and affected clients. Adding PyPy-specific markers exacerbated
          this problem by requiring clients to specify the same markers.
        * `numpy` 2.0.x is the last version that supports Python 3.9, and it crashes with Python
          3.13, so the `nidaqmx` distribution package specifies two `numpy` version constraints:
          one for Python 3.9-3.12 (numpy>=1.22) and one for Python 3.13+ (numpy>=2.1).
        * The `nidaqmx` distribution package now specifies only a lower bound for `click`.
    * Clarify PyPy support and enable unit testing with PyPy.
    * Adopt ni-python-styleguide for hand-written code.
    * Upgrade to Poetry 2.x and migrate `pyproject.toml` format.
    * Add support for Python 3.14.
    * Add https://github.com/ni/ni-apis as a submodule of nidaqmx-python.
    * Add an optional dependency on `ni.grpcdevice.v1.proto`.
        * The internal `session_pb2` submodule has been moved to the shared package `ni.grpcdevice.v1.proto`. Installing the `nidaqmx` package's `grpc` extra will automatically install this package.
        * If you get `ModuleNotFoundError: No module named 'session_pb2'`, make sure you are installing the `nidaqmx` package's `grpc` extra.

* ### Known Issues
    * ...

## 1.2.0
* ### Merged Pull Requests
    * [Full changelog: 1.1.0...1.2.0](https://github.com/ni/nidaqmx-python/compare/1.1.0...1.2.0)

* ### Resolved Issues
    * Fix PEP 660 builds by setting `build-system` to use `poetry-core`
    * [579: nidaqmx does not generate numbered virtual channel names correctly](https://github.com/ni/nidaqmx-python/issues/579)
    * [692: Cannot set "ai_conv_rate" on NI DAQ 9209 due to missing active device modifier for timing attributes](https://github.com/ni/nidaqmx-python/issues/692)

* ### Major Changes
    * Removed the `docs` extra and converted it to a Poetry dependency group.
    * Updated hightime dependency from `^0.2.2` to `>=0.2.2` to allow for newer versions.

* ### Known Issues
    * ...

## 1.1.0
* ### Merged Pull Requests
    * [Full changelog: 1.0.2...1.1.0](https://github.com/ni/nidaqmx-python/compare/1.0.2...1.1.0)

* ### Resolved Issues
    * [656: Missing usage of slots in classes with DAQmx attributes](https://github.com/ni/nidaqmx-python/issues/656)

* ### Major Changes
    * Added support for mioDAQ configurable digital voltage.
    * Added support for mioDAQ ID Pin.
    * Removed support for Python 3.8.

* ### Known Issues
    * ...

## 1.0.2
* ### Merged Pull Requests
    * [Full changelog: 1.0.1...1.0.2](https://github.com/ni/nidaqmx-python/compare/1.0.1...1.0.2)

* ### Resolved Issues
    * [644: nidaqmx doesn't support Python 3.13+](https://github.com/ni/nidaqmx-python/issues/644)
    * [641: No devices found](https://github.com/ni/nidaqmx-python/issues/641)
        * Fall back to ASCII encoding if the system locale is not set.

* ### Known Issues
    * [639: first_samp_timestamp_val property does not work because LibraryInterpreter is missing a method](https://github.com/ni/nidaqmx-python/issues/639)

## 1.0.1
* ### Merged Pull Requests
    * [Full changelog: 1.0.0...1.0.1](https://github.com/ni/nidaqmx-python/compare/1.0.0...1.0.1)

* ### Resolved Issues
    * [540: Task.wait_for_valid_timestamp doesn't return the timestamp](https://github.com/ni/nidaqmx-python/issues/540)
    * [606: CERTIFICATE_VERIFY_FAILED occurs when executing installdriver command on Windows system](https://github.com/ni/nidaqmx-python/issues/606)
    * [615: Onboard device memory overflow](https://github.com/ni/nidaqmx-python/issues/615)
    * [623: installdriver CLI doesn't prompt or indicate what versions are being downloaded/installed on a clean system](https://github.com/ni/nidaqmx-python/issues/623)

* ### Known Issues
    * [613: InStream.logging_file_path setter type hint is not effective](https://github.com/ni/nidaqmx-python/issues/613)
    * [620: InStream.get_channels_buffer_size uses wrong encoding](https://github.com/ni/nidaqmx-python/issues/620)
    * [621: InStream.get_channels_buffer_size should not be public](https://github.com/ni/nidaqmx-python/issues/621)

## 1.0.0
* ### Merged Pull Requests
    * [Full changelog: 0.9.0...1.0.0](https://github.com/ni/nidaqmx-python/compare/0.9.0...1.0.0)

* ### Resolved Issues
    * [38: No spacing in raw-read function names](https://github.com/ni/nidaqmx-python/issues/38)
    * [384: Support internationalization](https://github.com/ni/nidaqmx-python/issues/384)
    * [392: Indexing PhysicalChannelCollection fails for slices and strings containing a list/range of channels](https://github.com/ni/nidaqmx-python/issues/392)
    * [482: Default argument values for bridge create channel functions are unusable](https://github.com/ni/nidaqmx-python/issues/482)

* ### Major Changes
    * Add support for strain calibration (offset nulling and shunt calibration)
    * Add support for DAQmx calibration info properties
    * Add support for WaitForValidTimestamp
    * Fix naming issues:
        <!-- cspell:ignore AAND -->
        * Rename `ShuntCalSelect.AAND_B` to `A_AND_B`.
    * Automate Driver Install Experience within nidaqmx Module
    <!-- cspell:ignore libtime -->
    * Update libtime to accept time before 1970

* ### Known Issues
    * ...

## 0.9.0

* ### Merged Pull Requests
    *  [460: enabled support for DAQmxSelfCal](https://github.com/ni/nidaqmx-python/pull/460)
* ### Major Changes
    * `nidaqmx.errors.DaqNotFoundError`, `nidaqmx.errors.DaqNotSupportedError`, and
    `nidaqmx.errors.DaqFunctionNotSupportedError` are now public exceptions.
    * Consistently return `nidaqmx.errors.DaqNotFoundError` on all platforms when the NI-DAQmx
    driver is not installed.
    * Updated supported Python versions to 3.8, 3.9, 3.10, 3.11, and 3.12
* ### Known Issues
    * ...

## 0.8.0

* ### Merged Pull Requests
    * [Full changelog: 0.7.0...0.8.0](https://github.com/ni/nidaqmx-python/compare/0.7.0...0.8.0)
    * [Query: Closed PRs with the label: interpreter_implementation](https://github.com/ni/nidaqmx-python/pulls?q=label%3Ainterpreter_implementation+is%3Aclosed)
    * [Query: Closed PRs with the label: library_interpreter](https://github.com/ni/nidaqmx-python/pulls?q=label%3Alibrary_interpreter+is%3Aclosed)
    * [Query: Closed PRs with the label: grpc_interpreter](https://github.com/ni/nidaqmx-python/pulls?q=label%3Agrpc_interpreter+is%3Aclosed)
    * [Query: Closed PRs with the label: test_improvements](https://github.com/ni/nidaqmx-python/pulls?q=label%3Atest_improvements+is%3Aclosed)
    * [Query: Closed PRs with the label: interpreter_fixes](https://github.com/ni/nidaqmx-python/pulls?q=label%3Ainterpreter_fixes+is%3Aclosed)
    * [Query: Closed PRs with the label: interpreter_testcase_update](https://github.com/ni/nidaqmx-python/pulls?q=label%3Ainterpreter_testcase_updates+is%3Aclosed)
    * [Query: Closed PRs with the label: event_handling](https://github.com/ni/nidaqmx-python/pulls?q=label%3Aevent_handling+is%3Aclosed)

* ### Major Changes

    * Added support for communicating with DAQmx devices through gRPC using [NI gRPC Device Server](https://github.com/ni/grpc-device). This enables using DAQmx with the MeasurementLink session management service.
        * The initialization methods for `Task`, `Scale`, and other classes now accept a keyword-only `grpc_options` parameter. Pass a `GrpcSessionsOptions` object to enable gRPC support.
        * The `System` class now has a `remote()` method which accepts a `GrpcSessionOptions` object.
        * [NI gRPC Device Server](https://github.com/ni/grpc-device) version 2.2 or later is required. Older versions of NI gRPC Device Server are unsupported because they are missing bug fixes needed to support nidaqmx-python.
    * The following functions now emit `DeprecationWarning` when called:
        * `nidaqmx.errors` module: `check_for_error`, `is_string_buffer_too_small`, and `is_array_buffer_too_small` are `ctypes`-specific helper functions, so they have been moved to an internal module.
        * `System` class: `set_analog_power_up_states` does not support `PowerUpStates.TRISTATE` and `get_analog_power_up_states` has design issues that make the previous implementation unworkable, so they have been deprecated in favor of `set_analog_power_up_states_with_output_type` and `get_analog_power_up_states_with_output_type`.
    * The internals of the `nidaqmx` package have been refactored to support gRPC:
        * Access to the DAQmx driver is now handled by the internal `BaseInterpreter` abstract base class. There are separate implementations of this abstract base class for `ctypes` vs. gRPC.
        * Internal initialization methods now accept an `interpreter` parameter. Methods that take an `interpreter` are not part of the public API.
        * Added a stub generator which will generate the gRPC stub files based on the proto files present in `src/codegen/protos`. The files will be generated into `generator/nidaqmx/_stubs`.
        * The internal `nidaqmx._task_modules.read_functions` and `nidaqmx._task_modules.write_functions` modules have been removed. If your application uses these modules, you must update it to use public APIs such as `task.read()`/`task.write()`, `task.in_stream.read()`/`task.out_stream.write()`, or `nidaqmx.stream_readers`/`nidaqmx.stream_writers`.
        * Updated the existing tests to run with and without gRPC support.
        * Added multiple test cases to improve the overall test coverage.

* ### Known Issues
   * Comparisons between DAQmx object instances do not take gRPC remoting into account. For example, `Device("Dev1")` refers to a local device and `Device("Dev1", grpc_options=...)` refers to a remote device, but they are considered equal. Likewise, two instances of `Device("Dev1", grpc_options=...)` with different remote hosts are considered equal.

## 0.7.0

* ### Merged Pull Requests
    * [217: Handle leading zeros in flatten/unflatten implementation](https://github.com/ni/nidaqmx-python/issues/217)
    * [219: nidaqmx: Use in-project virtualenvs](https://github.com/ni/nidaqmx-python/pull/219)
    * [Query: Closed PRs with label:generator_refactor](https://github.com/ni/nidaqmx-python/pulls?page=1&q=is%3Apr+is%3Aclosed+label%3Agenerator_refactor)
    * [Query: Closed PRs with label:test_improvements](https://github.com/ni/nidaqmx-python/pulls?page=1&q=is%3Apr+is%3Aclosed+label%3Atest_improvements)
    * [256: nidaqmx: Remove Python 2.7 workarounds](https://github.com/ni/nidaqmx-python/pull/256)
* ### Resolved Issues
    * [216: Can read channel_names of PersistedTask but not channels](https://github.com/ni/nidaqmx-python/issues/216)
* ### Major Changes
    * Added a generator that produces the `nidaqmx` module code.
    * Some properties were renamed in an effort to improve the consistency of the `nidaqmx` module and to support maintainability of the generator. The previous names are still usable, but will emit a `DeprecationWarning` on usage. These deprecated properties may be removed in a future update.
    * Unused enums have been removed. This affects enums that are solely used by DAQmx features that are not supported in the `nidaqmx` module, such as external calibration, the DAQmx switch API, and internal APIs.
    * Refactored the repository folder structure as follows:
        * `generated/nidaqmx/` - The output of the code generator and source for the build `nidaqmx` module. Do not directly modify any files in this folder.
        * `examples/` - Example programs demonstrating how to use the `nidaqmx` module.
        * `src/codegen/` - The code generator.
        * `src/handwritten/` - Hand-maintained files that are copied as-is during code generation.
        * `tests` - Test code that exercises the `nidaqmx` module to ensure it functions correctly and doesn't introduce regressions.
    * Multiple various test improvements in support of the generator refactoring.

## 0.6.5

* ### Resolved Issues
    * [194: Multiple Voltage Measurement Types in the same task causes errors on Read](https://github.com/ni/nidaqmx-python/pull/194)

## 0.6.4

* ### Merged Pull Requests
    * [179: Optimize for happy path](https://github.com/ni/nidaqmx-python/pull/179)
    * [180: Use ndarray.size instead of numpy.prod](https://github.com/ni/nidaqmx-python/pull/180)
    * [182: fix enum bitfields](https://github.com/ni/nidaqmx-python/pull/182)
    * [183: add support for reverse voltage error attributes to nidaqmx-python](https://github.com/ni/nidaqmx-python/pull/183)
    * [185: update testing to allow for some simulation](https://github.com/ni/nidaqmx-python/pull/185)
* ### Resolved Issues
    * [181: mismatched enum names in ai_term_cfgs](https://github.com/ni/nidaqmx-python/issues/181)

## 0.6.3

* ### Major Changes
    * DAQmx 22.0 updates.

## 0.6.2

* ### Major Changes
    * Added NI-DAQmx Power Channel APIs.

## 0.6.1

* ### Resolved Issues
    * [37: ai_raw example is bad](https://github.com/ni/nidaqmx-python/issues/37)
    * [54: Linux supported?](https://github.com/ni/nidaqmx-python/issues/54)
    <!-- cspell:ignore pynidaqmx -->
    * [64: nidaqmx-python and pynidaqmx projects use the same package name](https://github.com/ni/nidaqmx-python/issues/64)
    * [65: ci_count_edges.py REQUIRES A START COMMAND](https://github.com/ni/nidaqmx-python/issues/65)
    * [100: How to clear task and create a new task with same name?](https://github.com/ni/nidaqmx-python/issues/100)
    * [101: Use IntEnum instead of Enum](https://github.com/ni/nidaqmx-python/issues/101)
    * [102: handle types and daqmx versions](https://github.com/ni/nidaqmx-python/issues/102)
    * [117: Error in example](https://github.com/ni/nidaqmx-python/issues/117)
    * [131: task.write for COUNTER_OUTPUT - UsageTypeCO.PULSE_FREQUENCY has frequency and duty cycle reversed](https://github.com/ni/nidaqmx-python/issues/131)
    * [124: nidaqmx_examples/system_properties.py errors out as of version 0.5.7](https://github.com/ni/nidaqmx-python/issues/124)
    * [151: Write functions require writable numpy array](https://github.com/ni/nidaqmx-python/issues/151)
    * [154: Problem with task.write() when not enough buffer free](https://github.com/ni/nidaqmx-python/issues/154)
* ### Major Changes
    * Scrubbed all examples to ensure they all function correctly and use DAQmx best practices.
    * Added `DaqReadError` and `DaqWriteError` subclasses of `DaqError` that provide important metadata for partial reads and writes.
    * Linux is officially supported.

## 0.6.0

* ### Resolved Issues
    * [132: __future__ imports are now all mandatory in the minimum supported python version](https://github.com/ni/nidaqmx-python/issues/132)
* ### Major Changes
    * Add support for most NI-DAQmx 16.1-21.5 APIs.
        * APIs using time data types are not yet supported.
    * Various other improvements:
        * No more empty docstrings on constants.
        * Fix C API function mapping for attributes - dozens were incorrect.
        * Remove some internal-only enumerations that were unused.
        * **(compat breaker)** Fix two egregious naming issues when translating the API to `SNAKE_CASE`. `M_HZ` is now
        `MHZ` (megahertz) and `<word>m_VOLTS` is now `MILLIVOLTS`.
        * **(compat breaker)** Fix various constant names that didn't make any sense.
        * Add a header to all auto-generated files indicating that they should not be edited by hand.


## 0.5.8

* ### Merged Pull Requests
    * [Bug in InStream.readinto()](https://github.com/ni/nidaqmx-python/pull/45)
    * [Fix for Linux where DAQmxGetSysNIDAQUpdateVersion is not available](https://github.com/ni/nidaqmx-python/pull/75)
    * [Fix RelativeTo function names to match DLL names](https://github.com/ni/nidaqmx-python/pull/86)
    * [fix: exported symbol names](https://github.com/ni/nidaqmx-python/pull/93)
    * [fix: dev dependencies to avoid security alerts](https://github.com/ni/nidaqmx-python/pull/94)
    * [fix: task.__del__ to use _saved_name](https://github.com/ni/nidaqmx-python/pull/95)
    * [remove: python2.7 support](https://github.com/ni/nidaqmx-python/pull/96)
    * [update: requirements](https://github.com/ni/nidaqmx-python/pull/97)
    * [Fix warning regarding ABC import from collections](https://github.com/ni/nidaqmx-python/pull/104)
    * [remove: py2, py27 support from classifiers](https://github.com/ni/nidaqmx-python/pull/105)
    * [Correct Network Connection Loss Property](https://github.com/ni/nidaqmx-python/pull/111)
* ### Resolved Issues
    * Fixed `test_many_sample_pulse_ticks` test
    * Added a bridge device to test MAX config to enable `test_list_of_floats_property` to run
    * [36: no version information available](https://github.com/ni/nidaqmx-python/issues/36)
* ### Major Changes
    * Switched to [poetry](https://python-poetry.org/) build system.
    * Updated supported Python versions to 3.7, 3.8, 3.9, and 3.10
    * Updated to latest dependencies
        * Replaced `numpy.bool` with `bool` native type

## 0.5.7
* ### Resolved Issues
    * [40: is_task_done() cannot be used.](https://github.com/ni/nidaqmx-python/issues/40)
    * [42: register signal event not supported?](https://github.com/ni/nidaqmx-python/issues/42)

## 0.5.6
* ### Resolved Issues
    * [32: Incorrect types in samp_quant_samp_per_chan and total_samp_per_chan_generated parameters](https://github.com/ni/nidaqmx-python/issues/32)
    * [1: nidaqmx doesn't work on Python 2.7.13](https://github.com/ni/nidaqmx-python/issues/1)

## 0.5.5
* ### Resolved Issues
    * Adding lock around `argtypes` to prevent race condition between setting `argtypes` and calling functions, in cases
    the functions run in parallel.
    * Some special cases needed unconditional locks around both the setting of `argtypes` and the actual function call,
    like the variadic power-up state functions in system.py, and the register events functions in task.py.

## 0.5.4
* ### Merged Pull Requests
    * [Fix for unregistering callbacks](https://github.com/ni/nidaqmx-python/pull/15)
* ### Resolved Issues
    * [13: Should _import_lib error for unsupported platforms?](https://github.com/ni/nidaqmx-python/issues/13)
    * [12: Cannot catch load/version issues with public API](https://github.com/ni/nidaqmx-python/issues/12)
    * [11: CONTRIBUTING.rst link to Issues is broken](https://github.com/ni/nidaqmx-python/issues/11)

## 0.5.2
* Initial public release of nidaqmx
* Update setup.py description and fix issues 2, 3, 5, and 6 raised by Ed Page.
    <!-- cspell:ignore AIADC AIDC AILVDT AIRVDT CITC -->
    * Splitting joined acronyms AIADC, AIDC, AILVDT, AIRVDT and CITC.
    * Adding link to LICENSE file.
    * Updating README.rst file in source directory to eliminate Sphinx domain directives and add link to documentation on
    readthedocs.

## 0.5.0
* Initial pre-release of nidaqmx
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=CONTRIBUTING.md sha256=565de6b143976b66e6fd3fb1f5424d35f060e3639775da1df192103b3acc1c1a bytes=10057 -->
## FILE: CONTRIBUTING.md

- repository: `ni/nidaqmx-python`
- source_path: `CONTRIBUTING.md`
- sha256: `565de6b143976b66e6fd3fb1f5424d35f060e3639775da1df192103b3acc1c1a`
- bytes: 10057

````markdown
# Contributing to nidaqmx

Contributions to **nidaqmx** are welcome from all!

**nidaqmx** is managed via [git](https://git-scm.com), with the canonical upstream repository hosted
<!-- cspell:ignore developercertificate -->
on [GitHub](http://developercertificate.org/).

**nidaqmx** follows a pull-request model for development.  If you wish to contribute, you will need
to create a GitHub account, fork this project, push a branch with your changes to your project, and
then submit a pull request.

See [GitHub's official documentation](https://help.github.com/articles/using-pull-requests/) for
more details.

# Getting Started

To contribute to this project, it is recommended that you follow these steps:

1. Ensure you have [poetry](https://python-poetry.org/) [installed](https://python-poetry.org/docs/#installation)
2. Clone the repository using `git clone https://github.com/ni/nidaqmx-python.git`
3. Get the submodules using `git submodule update --init --recursive`
3. Install **nidaqmx** dependencies using `poetry install --all-extras --with examples`
4. Run the regression tests on your system (see Testing section). At this point, if any tests fail, do not
begin development. Try to investigate these failures. If you're unable to do so, report an issue
through our [GitHub issues page](http://github.com/ni/nidaqmx-python/issues).
5. Write new tests that demonstrate your bug or feature. Ensure that these new tests fail.
6. Make your change.
7. Once the necessary changes are done, update the auto-generated code using `poetry run python src/codegen --dest generated/nidaqmx`. This will ensure that the latest files are present in the ``generated`` folder.
   > **Note**
   > The codegen scripts require Python 3.10 or later.
8. Run all the regression tests again (including the tests you just added), and confirm that they all
pass.
9. Run `poetry run ni-python-styleguide lint` to check that the updated code follows NI's Python coding
conventions. If this reports errors, first run `poetry run ni-python-styleguide fix` in order to sort
imports and format the code with Black, then manually fix any remaining errors.
<!-- cspell:ignore mypy -->
10. Run `poetry run mypy` to statically type-check the updated code.
11. Run `npx cspell "**" --no-progress` to check for spelling errors. This requires [Node.js](https://nodejs.org/) to be installed.
12. Send a GitHub Pull Request to the main repository's master branch. GitHub Pull Requests are the
expected method of code collaboration on this project.

# Testing

In order to be able to run the **nidaqmx** regression tests, your setup should meet the following minimum
requirements:

- Setup has a machine with NI-DAQmx or the NI-DAQmx Runtime installed.
   - Currently the minimum supported NI-DAQmx version to run all tests is 21.3.
- Machine has a supported version of CPython or PyPy installed.
- Machine has [poetry](https://python-poetry.org/) installed.
- (recommended) Machine has an X Series DAQ device (e.g. PCIe-6363 or USB-6351) connected to it.
  - You can still run the tests without a physical X Series DAQ device, but some tests will be skipped.

Before running the regression tests, import the appropriate NI MAX configuration files:
- ``tests\max_config\nidaqmxMaxConfig.ini``: Contains custom scales, global channels, simulated devices,
  and tasks used by many regression tests.
   - **Note:** On Linux, use ``tests\max_config\linux\nidaqmxMaxConfig.ini`` to avoid importing an unsupported device.
- ``tests\max_config\examplesMaxConfig.ini``: Contains simulated devices used by the example programs.
  Importing this file is optional. It is used to run a subset of the example programs as test cases.

Refer to this [KB article](http://digital.ni.com/public.nsf/allkb/0E0D3D7C4AA8903886256B29000C9D5A) for
details on how to import a MAX configuration.

To run the **nidaqmx** regression tests in a specific version of Python, run the following command in the
root of the distribution:

```sh
$ poetry run pytest
```

To run the regression tests in all Python interpreters supported by **nidaqmx**, run the following
commands in the root of the distribution:

```sh
$ poetry run tox
```

This requires you to have all the Python interpreters supported by **nidaqmx** installed on your
machine.

# Benchmarks

Benchmark tests are not run by default when you run pytest. To run the benchmarks, use this command:

```sh
# Run the benchmarks
#   Compare benchmark before/after a change
#     see https://pytest-benchmark.readthedocs.io/en/latest/comparing.html
#   Run 1:  --benchmark-save=some-name
#   Run N:  --benchmark-compare=0001
$ poetry run pytest -v tests/benchmark --device Dev1
```

Or you can use tox (which skips the gRPC variants):
```
poetry run -- tox -e py310-base-benchmark -- --device Dev1
```

The benchmarks are designed to run on a 6363 device. If you don't specify a specific
device using `--device`, then it will automatically use any real or simulated 6363
that can be found.

# Building Documentation

To build the documentation install the optional docs packages and run sphinx. For example:

```sh
$ poetry install --with docs
$ poetry run sphinx-build -b html docs docs\_build
```

# Branching Policy

Active development for the next release occurs on the `master` branch.

During finalization, we create a release branch (e.g. `releases/1.2`) in order to control which changes target the imminent
release vs. the next release after that. Changes that are intended for both the imminent release and subsequent releases
should be made in the `master` branch and cherry-picked into the release branch. Changes that only apply to the imminent
release (such as version numbers) may be made directly in the release branch.

# Release Process

1. Ensure your git `HEAD` is at the latest version of the `master` or appropriate `releases/*` branch with no pending changes.
2. Note the version currently being released by running:
   ```sh
   $ poetry version
   ```
3. Run tests on every supported Python version. Refer to [Testing](#testing) section for details.
4. Build the documentation and spot check the output. Refer to [Building Documentation](#building-documentation)
section for details. Note that [nidaqmx-python @ readthedocs.io](https://nidaqmx-python.readthedocs.io/en/latest/)
has been configured to automatically update when the tagged GitHub release has been created. That
can be verified once that has been completed.
5. Create a release on GitHub, attaching the source at the latest commit as follows:
   * **Tag:** Create a new tag matching the version being released.
   * **Release Title:** The version being released.
   * **Description:** Contents of the `CHANGELOG.md` for the version being released.

   Publishing a release automatically triggers the [publish.yml](./.github/workflows/publish.yml)
<!-- cspell:ignore pypi -->
   workflow, which checks and builds the package, requests approval to publish it using the `pypi`
   deployment environment, publishes the package to PyPI using [Trusted
   Publishing](https://docs.pypi.org/trusted-publishers/), and creates a PR to update the version of
<!-- cspell:ignore pyproject -->
   **nidaqmx** in `pyproject.toml`.
6. GitHub contacts the approvers for the `pypi` deployment environment, who are currently the repo
   admins. One of them must approve the deployment for the publishing to proceed.
7. Find the auto-created PR named `chore: Update project version - <branch>`.
   - If it is waiting for checks to complete, close it and re-open it to work around the issue
     described in [the `ni/python-actions/update-project-version`
     docs](https://github.com/ni/python-actions?tab=readme-ov-file#token).
   - If the new version number is incorrect, update it by posting and committing a suggestion.
8. Create a PR adding a section to `CHANGELOG.md` for the new version with empty subsections.

# Updating gRPC stubs when the .proto file is modified

The `generated\nidaqmx\_stubs` directory contains the auto-generated Python files based on the NI-DAQmx protobuf (`.proto`) file.

The latest NI-DAQmx .proto file is available in the [grpc-device GitHub repo](https://github.com/ni/grpc-device/blob/main/generated/nidaqmx/nidaqmx.proto). Manually download and overwrite the `.proto` file under the location `codegen\protos\nidaqmx.proto`.

Run `poetry run python src/codegen --dest generated/nidaqmx`. This will ensure that the latest stub files are present in the `generated\nidaqmx\_stubs` folder.


# Developer Certificate of Origin (DCO)

Developer's Certificate of Origin 1.1

By making a contribution to this project, I certify that:

(a) The contribution was created in whole or in part by me and I
    have the right to submit it under the open source license
    indicated in the file; or

(b) The contribution is based upon previous work that, to the best
    of my knowledge, is covered under an appropriate open source
    license and I have the right under that license to submit that
    work with modifications, whether created in whole or in part
    by me, under the same open source license (unless I am
    permitted to submit under a different license), as indicated
    in the file; or

(c) The contribution was provided directly to me by some other
    person who certified (a), (b) or (c) and I have not modified
    it.

(d) I understand and agree that this project and the contribution
    are public and that a record of the contribution (including all
    personal information I submit with it, including my sign-off) is
    maintained indefinitely and may be redistributed consistent with
    this project or the open source license(s) involved.

(taken from [developercertificate.org](http://developercertificate.org/))

See [LICENSE](https://github.com/ni/nidaqmx-python/blob/master/LICENSE)
for details about how **nidaqmx** is licensed.
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=docs/collections.rst sha256=2cafaf560d2a0ad5179e8c707ea36fbf126fafed0a9e2f989f30d885a233f545 bytes=225 -->
## FILE: docs/collections.rst

- repository: `ni/nidaqmx-python`
- source_path: `docs/collections.rst`
- sha256: `2cafaf560d2a0ad5179e8c707ea36fbf126fafed0a9e2f989f30d885a233f545`
- bytes: 225

````rst
nidaqmx.system.collections
==========================

.. toctree::
   
   device_collection
   persisted_channel_collection
   persisted_scale_collection
   persisted_task_collection
   physical_channel_collection
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=docs/conf.py sha256=95a4862f8478503169df7a742cebadfcfc675ead4b33fccdfe245fcaed51557a bytes=2483 -->
## FILE: docs/conf.py

- repository: `ni/nidaqmx-python`
- source_path: `docs/conf.py`
- sha256: `95a4862f8478503169df7a742cebadfcfc675ead4b33fccdfe245fcaed51557a`
- bytes: 2483

````python
"""Sphinx Configuration File."""

import os
import pathlib
import sys

import toml

sys.path.insert(0, os.path.abspath("../"))


# -- General configuration ------------------------------------------------

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.coverage",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
]

source_suffix = ".rst"

master_doc = "index"

root_path = pathlib.Path(__file__).parent.parent
pyproj_file = root_path / "pyproject.toml"
proj_config = toml.loads(pyproj_file.read_text())

project = proj_config["project"]["name"]
company = "National Instruments"
author = company
copyright = f"2017-%Y, {company}"

# Release is the full version, version is only the major component
release = proj_config["project"]["version"]
version = ".".join(release.split(".")[:2])
description = proj_config["project"]["description"]

language = "en"

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

pygments_style = "sphinx"

todo_include_todos = False

intersphinx_mapping = {
    "grpc": ("https://grpc.github.io/grpc/python/", None),
    "nitypes": ("https://nitypes.readthedocs.io/en/latest/", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "protobuf": ("https://googleapis.dev/python/protobuf/latest/", None),
    "python": ("https://docs.python.org/3", None),
}

# -- Options for HTML output ----------------------------------------------

html_theme = "sphinx_rtd_theme"

html_static_path = []


# -- Options for HTMLHelp output ------------------------------------------

htmlhelp_basename = "NI-DAQmxPythonAPIdoc"


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {}

latex_documents = [
    (
        master_doc,
        "NI-DAQmxPythonAPI.tex",
        "NI-DAQmx Python API Documentation",
        "National Instruments",
        "manual",
    ),
]


# -- Options for manual page output ---------------------------------------

man_pages = [(master_doc, "ni-daqmxpythonapi", "NI-DAQmx Python API Documentation", [author], 1)]


# -- Options for Texinfo output -------------------------------------------

texinfo_documents = [
    (
        master_doc,
        "NI-DAQmxPythonAPI",
        "NI-DAQmx Python API Documentation",
        author,
        "NI-DAQmxPythonAPI",
        "One line description of project.",
        "Miscellaneous",
    ),
]
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=docs/constants.rst sha256=c3b1843958cc698e458710839efabf4a3c92f46b467102c34a6ab80d6f0b74d8 bytes=131 -->
## FILE: docs/constants.rst

- repository: `ni/nidaqmx-python`
- source_path: `docs/constants.rst`
- sha256: `c3b1843958cc698e458710839efabf4a3c92f46b467102c34a6ab80d6f0b74d8`
- bytes: 131

````rst
nidaqmx.constants
=================
.. automodule:: nidaqmx.constants
    :members:
    :undoc-members:
    :show-inheritance:
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=docs/device.rst sha256=7c7042e46d4734a8e842fcad15cdf2a40a3317581f11466ca96288bf68dbac9d bytes=149 -->
## FILE: docs/device.rst

- repository: `ni/nidaqmx-python`
- source_path: `docs/device.rst`
- sha256: `7c7042e46d4734a8e842fcad15cdf2a40a3317581f11466ca96288bf68dbac9d`
- bytes: 149

````rst
nidaqmx.system.device
=====================

.. automodule:: nidaqmx.system.device
    :members:
    :show-inheritance:
    :special-members:
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=docs/device_collection.rst sha256=b96c2a725f65ae8a436d348ea77915d87477f6e3d67316d8fc41abf90a534a75 bytes=172 -->
## FILE: docs/device_collection.rst

- repository: `ni/nidaqmx-python`
- source_path: `docs/device_collection.rst`
- sha256: `b96c2a725f65ae8a436d348ea77915d87477f6e3d67316d8fc41abf90a534a75`
- bytes: 172

````rst
nidaqmx.system.device_collection
================================

.. automodule:: nidaqmx.system._collections.device_collection
    :members:
    :show-inheritance:
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=docs/errors.rst sha256=04715d2ed21eff1b46ca7c8b41f300c3a0cc4c315abaa8977f858c07281aa804 bytes=122 -->
## FILE: docs/errors.rst

- repository: `ni/nidaqmx-python`
- source_path: `docs/errors.rst`
- sha256: `04715d2ed21eff1b46ca7c8b41f300c3a0cc4c315abaa8977f858c07281aa804`
- bytes: 122

````rst
nidaqmx.errors
==============
.. automodule:: nidaqmx.errors
    :members:
    :undoc-members:
    :show-inheritance:
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=docs/expiration_state.rst sha256=ba1472f3414bc9aaff78be8ac106d9371566903eb75e98ef9796c3f392450e62 bytes=174 -->
## FILE: docs/expiration_state.rst

- repository: `ni/nidaqmx-python`
- source_path: `docs/expiration_state.rst`
- sha256: `ba1472f3414bc9aaff78be8ac106d9371566903eb75e98ef9796c3f392450e62`
- bytes: 174

````rst
nidaqmx.system.expiration_state
===============================

.. automodule:: nidaqmx.system._watchdog_modules.expiration_state
    :members:
    :show-inheritance:
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=docs/expiration_states_collection.rst sha256=d27d754567dbf2631eb697227cfc6e539d9be783f5cf347f580f631e13add1eb bytes=210 -->
## FILE: docs/expiration_states_collection.rst

- repository: `ni/nidaqmx-python`
- source_path: `docs/expiration_states_collection.rst`
- sha256: `d27d754567dbf2631eb697227cfc6e539d9be783f5cf347f580f631e13add1eb`
- bytes: 210

````rst
nidaqmx.system.expiration_states_collection
===========================================

.. automodule:: nidaqmx.system._watchdog_modules.expiration_states_collection
    :members:
    :show-inheritance:
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=docs/grpc_session_options.rst sha256=fa7f5c9c0b902ad1ec42f52166acabd07cdbabbef39f4b68f0c0bd97e1d8a5c4 bytes=3203 -->
## FILE: docs/grpc_session_options.rst

- repository: `ni/nidaqmx-python`
- source_path: `docs/grpc_session_options.rst`
- sha256: `fa7f5c9c0b902ad1ec42f52166acabd07cdbabbef39f4b68f0c0bd97e1d8a5c4`
- bytes: 3203

````rst
nidaqmx.grpc_session_options
============================

Support for using NI-DAQmx over gRPC

.. note:: For MeasurementLink and NI gRPC Device Server, a NI-DAQmx task is considered to be a type of driver session.

.. py:currentmodule:: nidaqmx

.. py:class:: SessionInitializationBehavior
    :canonical: nidaqmx.grpc_session_options.SessionInitializationBehavior

    .. py:attribute:: SessionInitializationBehavior.AUTO

        The NI gRPC Device Server will attach to an existing session with the specified name if it exists,
        otherwise the server will initialize a new session.

        .. note:: When using a :class:`~nidaqmx.task.Task` as a context manager and the context exits, the behavior depends on what happened when the constructor
            was called. If it resulted in a new session being created on the NI gRPC Device Server, then it will automatically close the
            server session. If it instead attached to an existing session, then it will detach from the server session and leave it open.

    .. py:attribute:: SessionInitializationBehavior.INITIALIZE_SERVER_SESSION

        Require the NI gRPC Device Server to initialize a new session with the specified name.

        .. note:: When using a :class:`~nidaqmx.task.Task` as a context manager and the context exits, it will automatically close the
            server session.

    .. py:attribute:: SessionInitializationBehavior.ATTACH_TO_SERVER_SESSION

        Require the NI gRPC Device Server to attach to an existing session with the specified name.

        .. note:: When using a :class:`~nidaqmx.task.Task` as a context manager and the context exits, it will detach from the server session
            and leave it open.


.. py:class:: GrpcSessionOptions(self, grpc_channel, session_name, initialization_behavior=SessionInitializationBehavior.AUTO)
    :canonical: nidaqmx.grpc_session_options.GrpcSessionOptions

    Collection of options that specifies session behaviors related to gRPC.

    Creates and returns an object you can pass to a :class:`~nidaqmx.task.Task` constructor or various other constructors and methods.

    :param grpc_channel:

        Specifies the channel to the NI gRPC Device Server.

    :type grpc_channel: :class:`grpc.Channel`

    :param session_name:

        User-specified name that identifies the driver session on the NI gRPC Device Server.

        This is different from the resource name parameter many APIs take as a separate
        parameter. Specifying a name makes it easy to share sessions across multiple gRPC clients.

        For NI-DAQmx tasks, the driver session name is the same as the NI-DAQmx task name.
        You can either specify the name passed to a :class:`~nidaqmx.task.Task` constructor or an empty string.

    :type session_name: str

    :param initialization_behavior:

        Specifies whether it is acceptable to initialize a new session or attach to an existing one, or if only one of the behaviors is desired.

        The driver session exists on the NI gRPC Device Server.

    :type initialization_behavior: :py:data:`nidaqmx.SessionInitializationBehavior`
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=docs/index.rst sha256=5ecfdf8b5a868a001a523e78269b0b6e25970d13443ec318cfa0ec349abb493e bytes=639 -->
## FILE: docs/index.rst

- repository: `ni/nidaqmx-python`
- source_path: `docs/index.rst`
- sha256: `5ecfdf8b5a868a001a523e78269b0b6e25970d13443ec318cfa0ec349abb493e`
- bytes: 639

````rst
.. NI-DAQmx Python API documentation master file, created by
   sphinx-quickstart on Thu Dec 15 09:40:36 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

NI-DAQmx Python Documentation
=============================

.. include:: ../README.rst

.. py:module:: nidaqmx

.. toctree::
   :maxdepth: 3
   :caption: API Reference:

   constants
   errors
   grpc_session_options
   scale
   stream_readers
   stream_writers
   system
   task
   types
   utils


Indices and Tables
==================

* :ref:`genindex`
* :ref:`modindex`
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=docs/make.bat sha256=4742daac0ad84c9f7e1fad239930f9a0231d3060d130060a1b9c98e227b28b6e bytes=821 -->
## FILE: docs/make.bat

- repository: `ni/nidaqmx-python`
- source_path: `docs/make.bat`
- sha256: `4742daac0ad84c9f7e1fad239930f9a0231d3060d130060a1b9c98e227b28b6e`
- bytes: 821

````batch
@ECHO OFF

pushd %~dp0

REM Command file for Sphinx documentation

if "%SPHINXBUILD%" == "" (
	set SPHINXBUILD=sphinx-build
)
set SOURCEDIR=.
set BUILDDIR=_build
set SPHINXPROJ=NI-DAQmxPythonAPI

if "%1" == "" goto help

%SPHINXBUILD% >NUL 2>NUL
if errorlevel 9009 (
	echo.
	echo.The 'sphinx-build' command was not found. Make sure you have Sphinx
	echo.installed, then set the SPHINXBUILD environment variable to point
	echo.to the full path of the 'sphinx-build' executable. Alternatively you
	echo.may add the Sphinx directory to PATH.
	echo.
	echo.If you don't have Sphinx installed, grab it from
	echo.http://sphinx-doc.org/
	exit /b 1
)

%SPHINXBUILD% -M %1 %SOURCEDIR% %BUILDDIR% %SPHINXOPTS%
goto end

:help
%SPHINXBUILD% -M help %SOURCEDIR% %BUILDDIR% %SPHINXOPTS%

:end
popd
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=docs/Makefile sha256=36b5389937c42e6122cf72c4a623b62703ef898bbbbbef0eb86ac82bea69625c bytes=633 -->
## FILE: docs/Makefile

- repository: `ni/nidaqmx-python`
- source_path: `docs/Makefile`
- sha256: `36b5389937c42e6122cf72c4a623b62703ef898bbbbbef0eb86ac82bea69625c`
- bytes: 633

````text
# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SPHINXPROJ    = NI-DAQmxPythonAPI
SOURCEDIR     = .
BUILDDIR      = _build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=docs/persisted_channel.rst sha256=640539745a7b10250e4c0ad68730ab32b55df4fba2eea722154763d978f4f6b7 bytes=190 -->
## FILE: docs/persisted_channel.rst

- repository: `ni/nidaqmx-python`
- source_path: `docs/persisted_channel.rst`
- sha256: `640539745a7b10250e4c0ad68730ab32b55df4fba2eea722154763d978f4f6b7`
- bytes: 190

````rst
nidaqmx.system.persisted_channel
================================

.. automodule:: nidaqmx.system.storage.persisted_channel
    :members:
    :show-inheritance:
    :special-members:
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=docs/persisted_channel_collection.rst sha256=5967365e0a893f6988c09396a9f45309c3d660d0d26f1131fcafe81780acc835 bytes=205 -->
## FILE: docs/persisted_channel_collection.rst

- repository: `ni/nidaqmx-python`
- source_path: `docs/persisted_channel_collection.rst`
- sha256: `5967365e0a893f6988c09396a9f45309c3d660d0d26f1131fcafe81780acc835`
- bytes: 205

````rst
nidaqmx.system.persisted_channel_collection
===========================================

.. automodule:: nidaqmx.system._collections.persisted_channel_collection
    :members:
    :show-inheritance:
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=docs/persisted_scale.rst sha256=8195177b03d5c234684a8baa6caa3b02cbda71f26f54191242fa924657398de7 bytes=184 -->
## FILE: docs/persisted_scale.rst

- repository: `ni/nidaqmx-python`
- source_path: `docs/persisted_scale.rst`
- sha256: `8195177b03d5c234684a8baa6caa3b02cbda71f26f54191242fa924657398de7`
- bytes: 184

````rst
nidaqmx.system.persisted_scale
==============================

.. automodule:: nidaqmx.system.storage.persisted_scale
    :members:
    :show-inheritance:
    :special-members:
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=docs/persisted_scale_collection.rst sha256=a70bcdec6648a0cce1f865afefc87b4eba7fd512ff9f073a2ff6573fd96a855d bytes=199 -->
## FILE: docs/persisted_scale_collection.rst

- repository: `ni/nidaqmx-python`
- source_path: `docs/persisted_scale_collection.rst`
- sha256: `a70bcdec6648a0cce1f865afefc87b4eba7fd512ff9f073a2ff6573fd96a855d`
- bytes: 199

````rst
nidaqmx.system.persisted_scale_collection
=========================================

.. automodule:: nidaqmx.system._collections.persisted_scale_collection
    :members:
    :show-inheritance:
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=docs/persisted_task.rst sha256=bfc1c7452637891613cc4422efe6628bf87a23f0ed0981907041fb60c6210158 bytes=181 -->
## FILE: docs/persisted_task.rst

- repository: `ni/nidaqmx-python`
- source_path: `docs/persisted_task.rst`
- sha256: `bfc1c7452637891613cc4422efe6628bf87a23f0ed0981907041fb60c6210158`
- bytes: 181

````rst
nidaqmx.system.persisted_task
=============================

.. automodule:: nidaqmx.system.storage.persisted_task
    :members:
    :show-inheritance:
    :special-members:
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=docs/persisted_task_collection.rst sha256=5948ad2a7b71f66dfab55d3f73f88a08fe78b7d69175b781e8dd482dd7f0d0c2 bytes=196 -->
## FILE: docs/persisted_task_collection.rst

- repository: `ni/nidaqmx-python`
- source_path: `docs/persisted_task_collection.rst`
- sha256: `5948ad2a7b71f66dfab55d3f73f88a08fe78b7d69175b781e8dd482dd7f0d0c2`
- bytes: 196

````rst
nidaqmx.system.persisted_task_collection
========================================

.. automodule:: nidaqmx.system._collections.persisted_task_collection
    :members:
    :show-inheritance:
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=docs/physical_channel.rst sha256=b677ac2967e07dc30f98ed35233e73a5d257dbdd7b0d77e8e360e83eb56c036c bytes=177 -->
## FILE: docs/physical_channel.rst

- repository: `ni/nidaqmx-python`
- source_path: `docs/physical_channel.rst`
- sha256: `b677ac2967e07dc30f98ed35233e73a5d257dbdd7b0d77e8e360e83eb56c036c`
- bytes: 177

````rst
nidaqmx.system.physical_channel
===============================

.. automodule:: nidaqmx.system.physical_channel
    :members:
    :show-inheritance:
    :special-members:
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=docs/physical_channel_collection.rst sha256=391f8726faf8349d31d03cc9cbf8e475a80cacae53bf4e308001fb7a497d67c6 bytes=202 -->
## FILE: docs/physical_channel_collection.rst

- repository: `ni/nidaqmx-python`
- source_path: `docs/physical_channel_collection.rst`
- sha256: `391f8726faf8349d31d03cc9cbf8e475a80cacae53bf4e308001fb7a497d67c6`
- bytes: 202

````rst
nidaqmx.system.physical_channel_collection
==========================================

.. automodule:: nidaqmx.system._collections.physical_channel_collection
    :members:
    :show-inheritance:
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=docs/scale.rst sha256=4422f01ee5f5659ceb482d839e5210b00829e72b6e414293ea7b4195c047244e bytes=131 -->
## FILE: docs/scale.rst

- repository: `ni/nidaqmx-python`
- source_path: `docs/scale.rst`
- sha256: `4422f01ee5f5659ceb482d839e5210b00829e72b6e414293ea7b4195c047244e`
- bytes: 131

````rst
nidaqmx.scale
=====================

.. automodule:: nidaqmx.scale
    :members:
    :show-inheritance:
    :special-members:
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=docs/storage.rst sha256=9d2644bfb40297fc46809b5801d91091580c53b6a5f70d6ea980da1a78df46e6 bytes=130 -->
## FILE: docs/storage.rst

- repository: `ni/nidaqmx-python`
- source_path: `docs/storage.rst`
- sha256: `9d2644bfb40297fc46809b5801d91091580c53b6a5f70d6ea980da1a78df46e6`
- bytes: 130

````rst
nidaqmx.system.storage
======================

.. toctree::
   
   persisted_channel
   persisted_scale
   persisted_task
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=docs/stream_readers.rst sha256=1689416f02fd6b7c1b77d00776fad424461eb89d2be9c0bcd080fa4537c37c9a bytes=152 -->
## FILE: docs/stream_readers.rst

- repository: `ni/nidaqmx-python`
- source_path: `docs/stream_readers.rst`
- sha256: `1689416f02fd6b7c1b77d00776fad424461eb89d2be9c0bcd080fa4537c37c9a`
- bytes: 152

````rst
nidaqmx.stream_readers
======================

.. automodule:: nidaqmx.stream_readers
    :members:
    :show-inheritance:
    :inherited-members:
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=docs/stream_writers.rst sha256=9dae38654d2be6552ea144777751ac351d6254f346361525825c14bf10eb7773 bytes=152 -->
## FILE: docs/stream_writers.rst

- repository: `ni/nidaqmx-python`
- source_path: `docs/stream_writers.rst`
- sha256: `9dae38654d2be6552ea144777751ac351d6254f346361525825c14bf10eb7773`
- bytes: 152

````rst
nidaqmx.stream_writers
======================

.. automodule:: nidaqmx.stream_writers
    :members:
    :show-inheritance:
    :inherited-members:
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=docs/system.rst sha256=f1372ee06c54fc43e14e60ccf9556b5c32cf597de1ad11ffb19b8dad92500daa bytes=206 -->
## FILE: docs/system.rst

- repository: `ni/nidaqmx-python`
- source_path: `docs/system.rst`
- sha256: `f1372ee06c54fc43e14e60ccf9556b5c32cf597de1ad11ffb19b8dad92500daa`
- bytes: 206

````rst
nidaqmx.system
==============

.. automodule:: nidaqmx.system.system
    :members:
    :show-inheritance:

.. toctree::
   
   collections
   device
   physical_channel
   storage
   watchdog
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=docs/task.rst sha256=fb3ca78dd084d2b0936963b011216e09d6746525150a5289b89fa67751d265d5 bytes=198 -->
## FILE: docs/task.rst

- repository: `ni/nidaqmx-python`
- source_path: `docs/task.rst`
- sha256: `fb3ca78dd084d2b0936963b011216e09d6746525150a5289b89fa67751d265d5`
- bytes: 198

````rst
nidaqmx.task
============
.. automodule:: nidaqmx.task
    :members:
    :show-inheritance:
    :special-members:

.. toctree::
   
   task_channels
   task_collections
   task_triggering
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=docs/task_channels.rst sha256=4260284f54622dc75c643a5646570bdb6a8535e05316154fda00c86341314c82 bytes=155 -->
## FILE: docs/task_channels.rst

- repository: `ni/nidaqmx-python`
- source_path: `docs/task_channels.rst`
- sha256: `4260284f54622dc75c643a5646570bdb6a8535e05316154fda00c86341314c82`
- bytes: 155

````rst
nidaqmx.task.channels
=====================

.. automodule:: nidaqmx.task.channels
    :members:
    :show-inheritance:
    :member-order: bysource
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=docs/task_collections.rst sha256=6a232c66aad7182e8ce907fb94050dc2bf7093375ecfe5a942b1a61534f1a653 bytes=175 -->
## FILE: docs/task_collections.rst

- repository: `ni/nidaqmx-python`
- source_path: `docs/task_collections.rst`
- sha256: `6a232c66aad7182e8ce907fb94050dc2bf7093375ecfe5a942b1a61534f1a653`
- bytes: 175

````rst
nidaqmx.task.collections
===============================

.. automodule:: nidaqmx.task.collections
    :members:
    :show-inheritance:
    :member-order: bysource
    
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=docs/task_triggering.rst sha256=62901f51bb22df671e54464b26fd15ca2fccfb24b7073c1bbb8d9e3ec96d4272 bytes=161 -->
## FILE: docs/task_triggering.rst

- repository: `ni/nidaqmx-python`
- source_path: `docs/task_triggering.rst`
- sha256: `62901f51bb22df671e54464b26fd15ca2fccfb24b7073c1bbb8d9e3ec96d4272`
- bytes: 161

````rst
nidaqmx.task.triggering
=======================

.. automodule:: nidaqmx.task.triggering
    :members:
    :show-inheritance:
    :member-order: bysource
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=docs/types.rst sha256=eba3df5a5df94e4137e17a30e066219e85c780f6f35b89c649e8f37ba8025c10 bytes=119 -->
## FILE: docs/types.rst

- repository: `ni/nidaqmx-python`
- source_path: `docs/types.rst`
- sha256: `eba3df5a5df94e4137e17a30e066219e85c780f6f35b89c649e8f37ba8025c10`
- bytes: 119

````rst
nidaqmx.types
=============
.. automodule:: nidaqmx.types
    :members:
    :undoc-members:
    :show-inheritance:
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=docs/utils.rst sha256=12e4504a94402e751e354a41626a9586c275eda14c3c4abbb25cbb2a16d793d4 bytes=100 -->
## FILE: docs/utils.rst

- repository: `ni/nidaqmx-python`
- source_path: `docs/utils.rst`
- sha256: `12e4504a94402e751e354a41626a9586c275eda14c3c4abbb25cbb2a16d793d4`
- bytes: 100

````rst
nidaqmx.utils
=============

.. automodule:: nidaqmx.utils
    :members:
    :show-inheritance:
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=docs/watchdog.rst sha256=3a81d2eab719cf3e0380dbcae946f3d400aa68e2f79a6bf58efe3fae0ea1eae4 bytes=230 -->
## FILE: docs/watchdog.rst

- repository: `ni/nidaqmx-python`
- source_path: `docs/watchdog.rst`
- sha256: `3a81d2eab719cf3e0380dbcae946f3d400aa68e2f79a6bf58efe3fae0ea1eae4`
- bytes: 230

````rst
nidaqmx.system.watchdog
=======================

.. automodule:: nidaqmx.system.watchdog
    :members:
    :show-inheritance:
    :special-members:

.. toctree::
   
   expiration_state
   expiration_states_collection
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=examples/analog_in/ai_multi_task_pxie_ref_clk.py sha256=8d42c6b71a11143e9512f383ce37d365dea39d0adfd7254a4fcfeed64ce2f6d0 bytes=1413 -->
## FILE: examples/analog_in/ai_multi_task_pxie_ref_clk.py

- repository: `ni/nidaqmx-python`
- source_path: `examples/analog_in/ai_multi_task_pxie_ref_clk.py`
- sha256: `8d42c6b71a11143e9512f383ce37d365dea39d0adfd7254a4fcfeed64ce2f6d0`
- bytes: 1413

````python
"""Example of AI multitask operation."""

import pprint

import nidaqmx
from nidaqmx.constants import AcquisitionType, TaskMode

pp = pprint.PrettyPrinter(indent=4)


with nidaqmx.Task() as master_task, nidaqmx.Task() as slave_task:
    master_task.ai_channels.add_ai_voltage_chan("/PXI1Slot3/ai0")
    slave_task.ai_channels.add_ai_voltage_chan("/PXI1Slot7/ai0")

    master_task.timing.ref_clk_src = "PXIe_Clk100"
    master_task.timing.ref_clk_rate = 100000000
    master_task.timing.cfg_samp_clk_timing(1000, sample_mode=AcquisitionType.CONTINUOUS)
    master_task.triggers.sync_type.MASTER = True

    slave_task.timing.ref_clk_src = "PXIe_Clk100"
    slave_task.timing.ref_clk_rate = 100000000
    slave_task.timing.cfg_samp_clk_timing(1000, sample_mode=AcquisitionType.CONTINUOUS)
    slave_task.triggers.sync_type.SLAVE = True

    master_task.control(TaskMode.TASK_COMMIT)

    slave_task.triggers.start_trigger.cfg_dig_edge_start_trig("/PXI1Slot3/ai/StartTrigger")

    print("2 Channels 1 Sample Read Loop 10: ")
    slave_task.start()
    master_task.start()

    for _ in range(10):
        master_data = master_task.read(number_of_samples_per_channel=10)
        slave_data = slave_task.read(number_of_samples_per_channel=10)

        print("Master Task Data: ")
        pp.pprint(master_data)
        print("Slave Task Data: ")
        pp.pprint(slave_data)
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=examples/analog_in/ai_raw.py sha256=7c56a5ed499ff299194a39aad954dc2c2abec2c987ee7c088dc7205c12783013 bytes=806 -->
## FILE: examples/analog_in/ai_raw.py

- repository: `ni/nidaqmx-python`
- source_path: `examples/analog_in/ai_raw.py`
- sha256: `7c56a5ed499ff299194a39aad954dc2c2abec2c987ee7c088dc7205c12783013`
- bytes: 806

````python
"""Example of AI raw operation."""

import pprint

import nidaqmx

pp = pprint.PrettyPrinter(indent=4)

with nidaqmx.Task() as task:
    task.ai_channels.add_ai_voltage_chan("cDAQ1Mod1/ai0")
    in_stream = task.in_stream

    print("1 Channel 1 Sample Read Raw: ")
    data = in_stream.read(number_of_samples_per_channel=1)
    pp.pprint(data)

    print("1 Channel N Samples Read Raw: ")
    data = in_stream.read(number_of_samples_per_channel=8)
    pp.pprint(data)

    task.ai_channels.add_ai_voltage_chan("cDAQ1Mod1/ai1:3")

    print("N Channel 1 Sample Read Raw: ")
    data = in_stream.read(number_of_samples_per_channel=1)
    pp.pprint(data)

    print("N Channel N Samples Read Raw: ")
    data = in_stream.read(number_of_samples_per_channel=8)
    pp.pprint(data)
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=examples/analog_in/calculated_power_acq_int_clk.py sha256=1bc5d7ac985d1c3316140bce9464dedf38d5923dc7178854b29cac939ea6bf14 bytes=907 -->
## FILE: examples/analog_in/calculated_power_acq_int_clk.py

- repository: `ni/nidaqmx-python`
- source_path: `examples/analog_in/calculated_power_acq_int_clk.py`
- sha256: `1bc5d7ac985d1c3316140bce9464dedf38d5923dc7178854b29cac939ea6bf14`
- bytes: 907

````python
"""Example of analog input calculated power acquisition.

This example demonstrates how to acquire a finite amount
of calculated power data using the DAQ device's internal clock.

Supported Devices:

- PXIe-4311 (DAQmx 26.3.0 or later)
"""

import nidaqmx
from nidaqmx.constants import READ_ALL_AVAILABLE, AcquisitionType

with nidaqmx.Task() as task:
    task.ai_channels.add_ai_calculated_power_chan(
        voltage_physical_channel="Dev1/ai0",
        current_physical_channel="Dev1/ai1",
        voltage_min_val=0.0,
        voltage_max_val=5.0,
        current_min_val=0.0,
        current_max_val=0.02,
        ext_shunt_resistor_val=249.0,
    )

    task.timing.cfg_samp_clk_timing(1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=50)

    data = task.read(READ_ALL_AVAILABLE)
    print("Acquired data: [" + ", ".join(f"{value:f}" for value in data) + "]")
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=examples/analog_in/cont_calculated_power_acq_int_clk.py sha256=c4e01a96c4f9d6dc3e5832c59f6fa3d352c58178c6e165444b7917e1bb654519 bytes=1224 -->
## FILE: examples/analog_in/cont_calculated_power_acq_int_clk.py

- repository: `ni/nidaqmx-python`
- source_path: `examples/analog_in/cont_calculated_power_acq_int_clk.py`
- sha256: `c4e01a96c4f9d6dc3e5832c59f6fa3d352c58178c6e165444b7917e1bb654519`
- bytes: 1224

````python
"""Example of analog input calculated power acquisition.

This example demonstrates how to acquire a continuous amount of
calculated power data using the DAQ device's internal clock.

Supported Devices:

- PXIe-4311 (DAQmx 26.3.0 or later)
"""

import nidaqmx
from nidaqmx.constants import AcquisitionType

with nidaqmx.Task() as task:
    task.ai_channels.add_ai_calculated_power_chan(
        voltage_physical_channel="Dev1/ai0",
        current_physical_channel="Dev1/ai1",
        voltage_min_val=0.0,
        voltage_max_val=5.0,
        current_min_val=0.0,
        current_max_val=0.02,
        ext_shunt_resistor_val=249.0,
    )
    task.timing.cfg_samp_clk_timing(1000.0, sample_mode=AcquisitionType.CONTINUOUS)
    task.start()
    print("Running task. Press Ctrl+C to stop.")

    try:
        total_read = 0
        while True:
            data = task.read(number_of_samples_per_channel=1000)
            read = len(data)
            total_read += read
            print(f"Acquired data: {read} samples. Total {total_read}.", end="\r")
    except KeyboardInterrupt:
        pass
    finally:
        task.stop()
        print(f"\nAcquired {total_read} total samples.")
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=examples/analog_in/cont_thrmcpl_samples_int_clk.py sha256=ffda6424a9c105873692463d5d95ab488f6a0d909ea4253c990b1f129b171b60 bytes=1149 -->
## FILE: examples/analog_in/cont_thrmcpl_samples_int_clk.py

- repository: `ni/nidaqmx-python`
- source_path: `examples/analog_in/cont_thrmcpl_samples_int_clk.py`
- sha256: `ffda6424a9c105873692463d5d95ab488f6a0d909ea4253c990b1f129b171b60`
- bytes: 1149

````python
"""Example of continuous temperature acquisition.

This example demonstrates how to make continuous, hardware-timed
temperature measurement using a thermocouple.
"""

import nidaqmx
from nidaqmx.constants import (
    AcquisitionType,
    CJCSource,
    TemperatureUnits,
    ThermocoupleType,
)

with nidaqmx.Task() as task:
    task.ai_channels.add_ai_thrmcpl_chan(
        "Dev1/ai0",
        units=TemperatureUnits.DEG_C,
        thermocouple_type=ThermocoupleType.K,
        cjc_source=CJCSource.CONSTANT_USER_VALUE,
        cjc_val=25.0,
    )
    task.timing.cfg_samp_clk_timing(10.0, sample_mode=AcquisitionType.CONTINUOUS)
    task.start()
    print("Acquiring samples continuously. Press Ctrl+C to stop.")

    try:
        total_read = 0
        while True:
            data = task.read(number_of_samples_per_channel=50)
            read = len(data)
            total_read += read
            print(f"Acquired data: {read} samples. Total {total_read}.", end="\r")
    except KeyboardInterrupt:
        pass
    finally:
        task.stop()
        print(f"\nAcquired {total_read} total samples.")
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=examples/analog_in/cont_voltage_acq_int_clk.py sha256=15cd065333ab033c97e871d7bde0fa0f96948ab4a45a8cf43cfa97fec2344067 bytes=880 -->
## FILE: examples/analog_in/cont_voltage_acq_int_clk.py

- repository: `ni/nidaqmx-python`
- source_path: `examples/analog_in/cont_voltage_acq_int_clk.py`
- sha256: `15cd065333ab033c97e871d7bde0fa0f96948ab4a45a8cf43cfa97fec2344067`
- bytes: 880

````python
"""Example of analog input voltage acquisition.

This example demonstrates how to acquire a continuous amount of data
using the DAQ device's internal clock.
"""

import nidaqmx
from nidaqmx.constants import AcquisitionType

with nidaqmx.Task() as task:
    task.ai_channels.add_ai_voltage_chan("Dev1/ai0")
    task.timing.cfg_samp_clk_timing(1000.0, sample_mode=AcquisitionType.CONTINUOUS)
    task.start()
    print("Running task. Press Ctrl+C to stop.")

    try:
        total_read = 0
        while True:
            data = task.read(number_of_samples_per_channel=1000)
            read = len(data)
            total_read += read
            print(f"Acquired data: {read} samples. Total {total_read}.", end="\r")
    except KeyboardInterrupt:
        pass
    finally:
        task.stop()
        print(f"\nAcquired {total_read} total samples.")
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=examples/analog_in/cont_voltage_acq_int_clk_dig_start.py sha256=09da21a4a3ae988f59f8fe7b6e3a3468374aa4f0cebaa078938487089f0b7cf9 bytes=1364 -->
## FILE: examples/analog_in/cont_voltage_acq_int_clk_dig_start.py

- repository: `ni/nidaqmx-python`
- source_path: `examples/analog_in/cont_voltage_acq_int_clk_dig_start.py`
- sha256: `09da21a4a3ae988f59f8fe7b6e3a3468374aa4f0cebaa078938487089f0b7cf9`
- bytes: 1364

````python
"""Example of analog input voltage acquisition with a digital start trigger.

This example demonstrates how to acquire a continuous amount of
data using an external sample clock, started by a digital edge.
"""

import nidaqmx
from nidaqmx.constants import AcquisitionType


def main():
    """Continuously acquires data started by a digital edge."""
    total_read = 0
    with nidaqmx.Task() as task:

        def callback(task_handle, every_n_samples_event_type, number_of_samples, callback_data):
            """Callback function for reading signals."""
            nonlocal total_read
            read = len(task.read(number_of_samples_per_channel=number_of_samples))
            total_read += read
            print(f"Acquired data: {read} samples. Total {total_read}.", end="\r")

            return 0

        task.ai_channels.add_ai_voltage_chan("Dev1/ai0")
        task.timing.cfg_samp_clk_timing(1000.0, sample_mode=AcquisitionType.CONTINUOUS)
        task.triggers.start_trigger.cfg_dig_edge_start_trig("/Dev1/PFI0")

        task.register_every_n_samples_acquired_into_buffer_event(1000, callback)
        task.start()

        input("Acquiring samples continuously. Press Enter to stop.\n")

        task.stop()
        print(f"\nAcquired {total_read} total samples.")


if __name__ == "__main__":
    main()
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=examples/analog_in/cont_voltage_acq_int_clk_dig_start_retrig.py sha256=4e58957bfbc4a21fc8351844cf413c632c2ab71e8a02c777cb1d3e013f7f8e2f bytes=1398 -->
## FILE: examples/analog_in/cont_voltage_acq_int_clk_dig_start_retrig.py

- repository: `ni/nidaqmx-python`
- source_path: `examples/analog_in/cont_voltage_acq_int_clk_dig_start_retrig.py`
- sha256: `4e58957bfbc4a21fc8351844cf413c632c2ab71e8a02c777cb1d3e013f7f8e2f`
- bytes: 1398

````python
"""Example of analog input voltage acquisition with retriggering.

This example demonstrates how to acquire finite amounts of data
on each digital trigger.
"""

import nidaqmx
from nidaqmx.constants import AcquisitionType


def main():
    """Acquires data on each digital trigger."""
    total_read = 0
    with nidaqmx.Task() as task:

        def callback(task_handle, every_n_samples_event_type, number_of_samples, callback_data):
            """Callback function for reading signals."""
            nonlocal total_read
            read = len(task.read(number_of_samples_per_channel=number_of_samples))
            total_read += read
            print(f"Acquired data: {read} samples. Total {total_read}.", end="\r")

            return 0

        task.ai_channels.add_ai_voltage_chan("Dev1/ai0")
        task.timing.cfg_samp_clk_timing(
            1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=1000
        )
        task.triggers.start_trigger.cfg_dig_edge_start_trig("/Dev1/PFI0")
        task.triggers.start_trigger.retriggerable = True

        task.register_every_n_samples_acquired_into_buffer_event(1000, callback)
        task.start()

        input("Acquiring samples continuously. Press Enter to stop.\n")

        task.stop()
        print(f"\nAcquired {total_read} total samples.")


if __name__ == "__main__":
    main()
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=examples/analog_in/cont_voltage_acq_int_clk_every_n_samples_event.py sha256=589e87000b8cba540100dabc6d4061fdf0588757fd4b5c61be638750c1cd9778 bytes=1345 -->
## FILE: examples/analog_in/cont_voltage_acq_int_clk_every_n_samples_event.py

- repository: `ni/nidaqmx-python`
- source_path: `examples/analog_in/cont_voltage_acq_int_clk_every_n_samples_event.py`
- sha256: `589e87000b8cba540100dabc6d4061fdf0588757fd4b5c61be638750c1cd9778`
- bytes: 1345

````python
"""Example of analog input voltage acquisition with events.

This example demonstrates how to use Every N Samples events to
acquire a continuous amount of data using the DAQ device's
internal clock. The Every N Samples events indicate when data is
available from DAQmx.
"""

import nidaqmx
from nidaqmx.constants import AcquisitionType


def main():
    """Continuously acquires data using an Every N Samples event."""
    total_read = 0
    with nidaqmx.Task() as task:

        def callback(task_handle, every_n_samples_event_type, number_of_samples, callback_data):
            """Callback function for reading signals."""
            nonlocal total_read
            read = task.read(number_of_samples_per_channel=number_of_samples)
            total_read += len(read)
            print(f"Acquired data: {len(read)} samples. Total {total_read}.", end="\r")

            return 0

        task.ai_channels.add_ai_voltage_chan("Dev1/ai0")
        task.timing.cfg_samp_clk_timing(1000.0, sample_mode=AcquisitionType.CONTINUOUS)
        task.register_every_n_samples_acquired_into_buffer_event(1000, callback)
        task.start()

        input("Running task. Press Enter to stop.\n")

        task.stop()
        print(f"\nAcquired {total_read} total samples.")


if __name__ == "__main__":
    main()
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=examples/analog_in/thrmcpl_sample.py sha256=3f5a5f419def221b3d795ddc9ef40d09c9691260db111d4ab32dba5aa6a69273 bytes=473 -->
## FILE: examples/analog_in/thrmcpl_sample.py

- repository: `ni/nidaqmx-python`
- source_path: `examples/analog_in/thrmcpl_sample.py`
- sha256: `3f5a5f419def221b3d795ddc9ef40d09c9691260db111d4ab32dba5aa6a69273`
- bytes: 473

````python
"""Example of analog input temperature acquisition.

This example demonstrates how to acquire thermocouple measurement using
software timing.
"""

import nidaqmx
from nidaqmx.constants import ThermocoupleType, TemperatureUnits

with nidaqmx.Task() as task:
    task.ai_channels.add_ai_thrmcpl_chan(
        "Dev1/ai0", units=TemperatureUnits.DEG_C, thermocouple_type=ThermocoupleType.K
    )

    data = task.read()
    print(f"Acquired data: {data:f}")
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=examples/analog_in/voltage_acq_int_clk.py sha256=54ca33fcd99d923c39e57b54d5fa2514f2da8bf39f79cd2d4b380c91ced7eed8 bytes=561 -->
## FILE: examples/analog_in/voltage_acq_int_clk.py

- repository: `ni/nidaqmx-python`
- source_path: `examples/analog_in/voltage_acq_int_clk.py`
- sha256: `54ca33fcd99d923c39e57b54d5fa2514f2da8bf39f79cd2d4b380c91ced7eed8`
- bytes: 561

````python
"""Example of analog input voltage acquisition.

This example demonstrates how to acquire a finite amount
of data using the DAQ device's internal clock.
"""

import nidaqmx
from nidaqmx.constants import AcquisitionType, READ_ALL_AVAILABLE

with nidaqmx.Task() as task:
    task.ai_channels.add_ai_voltage_chan("Dev1/ai0")
    task.timing.cfg_samp_clk_timing(1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=50)

    data = task.read(READ_ALL_AVAILABLE)
    print("Acquired data: [" + ", ".join(f"{value:f}" for value in data) + "]")
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=examples/analog_in/voltage_acq_int_clk_dig_ref.py sha256=684207368b1d701fbb4ee7d367f0b9c714a987c1c10e8eb4c3e5bbf031124c0b bytes=709 -->
## FILE: examples/analog_in/voltage_acq_int_clk_dig_ref.py

- repository: `ni/nidaqmx-python`
- source_path: `examples/analog_in/voltage_acq_int_clk_dig_ref.py`
- sha256: `684207368b1d701fbb4ee7d367f0b9c714a987c1c10e8eb4c3e5bbf031124c0b`
- bytes: 709

````python
"""Example of analog input voltage acquisition with reference trigger.

This example demonstrates how to acquire a finite amount of data
using a digital reference trigger.
"""

import nidaqmx
from nidaqmx.constants import READ_ALL_AVAILABLE, AcquisitionType

with nidaqmx.Task() as task:
    task.ai_channels.add_ai_voltage_chan("Dev1/ai0")
    task.timing.cfg_samp_clk_timing(1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=100)
    task.triggers.reference_trigger.cfg_dig_edge_ref_trig("/Dev1/PFI8", pretrigger_samples=50)

    task.start()
    data = task.read(READ_ALL_AVAILABLE)
    print("Acquired data: [" + ", ".join(f"{value:f}" for value in data) + "]")
    task.stop()
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=examples/analog_in/voltage_acq_int_clk_dig_start_ref.py sha256=7f00e7d7f61bb13db77915be9547c17107ffe07e03cad77d371a6433d162a341 bytes=834 -->
## FILE: examples/analog_in/voltage_acq_int_clk_dig_start_ref.py

- repository: `ni/nidaqmx-python`
- source_path: `examples/analog_in/voltage_acq_int_clk_dig_start_ref.py`
- sha256: `7f00e7d7f61bb13db77915be9547c17107ffe07e03cad77d371a6433d162a341`
- bytes: 834

````python
"""Example of analog input voltage acquisition with digital start and reference trigger.

This example demonstrates how to acquire a finite amount of data
using an internal clock and a digital start and reference
trigger.
"""

import nidaqmx
from nidaqmx.constants import READ_ALL_AVAILABLE, AcquisitionType

with nidaqmx.Task() as task:
    task.ai_channels.add_ai_voltage_chan("Dev1/ai0")
    task.timing.cfg_samp_clk_timing(1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=100)
    task.triggers.start_trigger.cfg_dig_edge_start_trig("/Dev1/PFI0")
    task.triggers.reference_trigger.cfg_dig_edge_ref_trig("/Dev1/PFI8", pretrigger_samples=50)

    task.start()
    data = task.read(READ_ALL_AVAILABLE)
    print("Acquired data: [" + ", ".join(f"{value:f}" for value in data) + "]")
    task.stop()
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=examples/analog_in/voltage_acq_int_clk_plot_data.py sha256=a625a43d35c06287aa39c68d895d9aa00f3d8253ca1254dd8d42ee5a2468bd91 bytes=687 -->
## FILE: examples/analog_in/voltage_acq_int_clk_plot_data.py

- repository: `ni/nidaqmx-python`
- source_path: `examples/analog_in/voltage_acq_int_clk_plot_data.py`
- sha256: `a625a43d35c06287aa39c68d895d9aa00f3d8253ca1254dd8d42ee5a2468bd91`
- bytes: 687

````python
"""Example of generating visualizations for acquired data.

This example demonstrates how to plot the acquired data.
This example requires the matplotlib module.
Run 'pip install matplotlib' to install the matplotlib module.
"""

import matplotlib.pyplot as plot

import nidaqmx
from nidaqmx.constants import READ_ALL_AVAILABLE, AcquisitionType

with nidaqmx.Task() as task:
    task.ai_channels.add_ai_voltage_chan("Dev1/ai0")
    task.timing.cfg_samp_clk_timing(1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=50)

    data = task.read(READ_ALL_AVAILABLE)

    plot.plot(data)
    plot.ylabel("Amplitude")
    plot.title("Waveform")
    plot.show()
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=examples/analog_in/voltage_acq_int_clk_plot_wfm.py sha256=4672e96e5c6919a7d8d527962602933b93db5ade4fc1cd2198be7d05d5cf299b bytes=1842 -->
## FILE: examples/analog_in/voltage_acq_int_clk_plot_wfm.py

- repository: `ni/nidaqmx-python`
- source_path: `examples/analog_in/voltage_acq_int_clk_plot_wfm.py`
- sha256: `4672e96e5c6919a7d8d527962602933b93db5ade4fc1cd2198be7d05d5cf299b`
- bytes: 1842

````python
"""Example of generating visualizations for acquired data using the AnalogWaveform data type.

This example demonstrates how to plot the acquired waveform data.
This example requires the matplotlib module.
Run 'pip install matplotlib' to install the matplotlib module.
"""

import matplotlib.pyplot as plot
import numpy as np

import nidaqmx
from nidaqmx.constants import READ_ALL_AVAILABLE, AcquisitionType


def plot_analog_waveform(waveform, min_start_time=None):
    """Plot a single analog waveform."""
    # For multiplexed devices, each channel has a different time offset, based on the AI Convert
    # Clock rate. Calculate the time offset for this channel by subtracting the minimum start time.
    time_offset = 0.0
    if min_start_time is not None:
        time_offset = (waveform.timing.start_time - min_start_time).total_seconds()
    duration = waveform.sample_count * waveform.timing.sample_interval.total_seconds()
    time_data = np.linspace(
        time_offset, time_offset + duration, waveform.sample_count, endpoint=False
    )
    plot.plot(time_data, waveform.scaled_data, label=waveform.channel_name)


with nidaqmx.Task() as task:
    task.ai_channels.add_ai_voltage_chan("Dev1/ai0")
    task.timing.cfg_samp_clk_timing(1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=50)

    waveforms = task.read_waveform(READ_ALL_AVAILABLE)
    if not isinstance(waveforms, list):
        waveforms = [waveforms]

    min_start_time = min(waveform.timing.start_time for waveform in waveforms)
    for waveform in waveforms:
        plot_analog_waveform(waveform, min_start_time)
    plot.xlabel("Seconds")
    plot.ylabel(waveforms[0].units)  # assume all channels have the same units
    plot.title("Waveforms")
    plot.legend()
    plot.grid(True)

    plot.show()
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=examples/analog_in/voltage_acq_int_clk_tdms_logging.py sha256=a81a209f89b73783c6b4d8877a9cb57bf4317d7480301a7f631890f5f90e8953 bytes=1253 -->
## FILE: examples/analog_in/voltage_acq_int_clk_tdms_logging.py

- repository: `ni/nidaqmx-python`
- source_path: `examples/analog_in/voltage_acq_int_clk_tdms_logging.py`
- sha256: `a81a209f89b73783c6b4d8877a9cb57bf4317d7480301a7f631890f5f90e8953`
- bytes: 1253

````python
"""Example of logging acquired data to TDMS file and read back.

This example demonstrates how to log the acquired data to a TDMS file
and then read the data from the file.
This example requires the nptdms module.
Run 'pip install nptdms' to install the nptdms module.
"""

import os

from nptdms import TdmsFile

import nidaqmx
from nidaqmx.constants import (
    READ_ALL_AVAILABLE,
    AcquisitionType,
    LoggingMode,
    LoggingOperation,
)

with nidaqmx.Task() as task:
    task.ai_channels.add_ai_voltage_chan("Dev1/ai0")
    task.timing.cfg_samp_clk_timing(1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=10)
    task.in_stream.configure_logging(
        "TestData.tdms", LoggingMode.LOG_AND_READ, operation=LoggingOperation.CREATE_OR_REPLACE
    )

    task.read(READ_ALL_AVAILABLE)

with TdmsFile.open("TestData.tdms") as tdms_file:
    for group in tdms_file.groups():
        for channel in group.channels():
            data = channel[:]
            print("Read data from TDMS file: [" + ", ".join(f"{value:f}" for value in data) + "]")

if os.path.exists("TestData.tdms"):
    os.remove("TestData.tdms")

if os.path.exists("TestData.tdms_index"):
    os.remove("TestData.tdms_index")
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=examples/analog_in/voltage_acq_int_clk_wfm.py sha256=95e268a1c1c7b9500a16ee30b08ba3b89085e40631962b3757ad8a5f3ca20a1b bytes=707 -->
## FILE: examples/analog_in/voltage_acq_int_clk_wfm.py

- repository: `ni/nidaqmx-python`
- source_path: `examples/analog_in/voltage_acq_int_clk_wfm.py`
- sha256: `95e268a1c1c7b9500a16ee30b08ba3b89085e40631962b3757ad8a5f3ca20a1b`
- bytes: 707

````python
"""Example of analog input voltage waveform acquisition.

This example demonstrates how to acquire a finite amount
of data using the DAQ device's internal clock.
"""

import nidaqmx
from nidaqmx.constants import AcquisitionType

with nidaqmx.Task() as task:
    task.ai_channels.add_ai_voltage_chan("Dev1/ai0")
    task.timing.cfg_samp_clk_timing(1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=50)

    waveform = task.read_waveform()
    print(f"Acquired data: {waveform.scaled_data}")
    print(f"Channel name: {waveform.channel_name}")
    print(f"Units: {waveform.units}")
    print(f"t0: {waveform.timing.start_time}")
    print(f"dt: {waveform.timing.sample_interval}")
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=examples/analog_in/voltage_sample.py sha256=b3b27972d96bedad45a50d1ea1f258ae65697e5fec6b15d8f5955a3ddaa03e76 bytes=315 -->
## FILE: examples/analog_in/voltage_sample.py

- repository: `ni/nidaqmx-python`
- source_path: `examples/analog_in/voltage_sample.py`
- sha256: `b3b27972d96bedad45a50d1ea1f258ae65697e5fec6b15d8f5955a3ddaa03e76`
- bytes: 315

````python
"""Example of analog input voltage acquisition.

This example demonstrates how to acquire a voltage measurement using software timing.
"""

import nidaqmx

with nidaqmx.Task() as task:
    task.ai_channels.add_ai_voltage_chan("Dev1/ai0")

    data = task.read()
    print(f"Acquired data: {data:f}")
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=examples/analog_out/cont_gen_voltage_wfm_int_clk.py sha256=62e500acbbeb2cedbbd3123d3bb8caa878bd8943be550408a25c3569beb54fc5 bytes=2195 -->
## FILE: examples/analog_out/cont_gen_voltage_wfm_int_clk.py

- repository: `ni/nidaqmx-python`
- source_path: `examples/analog_out/cont_gen_voltage_wfm_int_clk.py`
- sha256: `62e500acbbeb2cedbbd3123d3bb8caa878bd8943be550408a25c3569beb54fc5`
- bytes: 2195

````python
"""Example of analog output voltage generation.

This example demonstrates how to output a continuous periodic
waveform using an internal sample clock.
"""

import numpy as np
import numpy.typing

import nidaqmx
from nidaqmx.constants import AcquisitionType


def generate_sine_wave(
    frequency: float,
    amplitude: float,
    sampling_rate: float,
    number_of_samples: int,
    phase_in: float = 0.0,
) -> tuple[numpy.typing.NDArray[numpy.double], float]:
    """Generates a sine wave with a specified phase.

    Args:
        frequency: Specifies the frequency of the sine wave.
        amplitude: Specifies the amplitude of the sine wave.
        sampling_rate: Specifies the sampling rate of the sine wave.
        number_of_samples: Specifies the number of samples to generate.
        phase_in: Specifies the phase of the sine wave in radians.

    Returns:
        Indicates a tuple containing the generated data and the phase
        of the sine wave after generation.
    """
    duration_time = number_of_samples / sampling_rate
    duration_radians = duration_time * 2 * np.pi
    phase_out = (phase_in + duration_radians) % (2 * np.pi)
    t = np.linspace(phase_in, phase_in + duration_radians, number_of_samples, endpoint=False)

    return (amplitude * np.sin(frequency * t), phase_out)


def main():
    """Continuously generates a sine wave."""
    with nidaqmx.Task() as task:
        sampling_rate = 1000.0
        number_of_samples = 1000
        task.ao_channels.add_ao_voltage_chan("Dev1/ao0")
        task.timing.cfg_samp_clk_timing(sampling_rate, sample_mode=AcquisitionType.CONTINUOUS)

        actual_sampling_rate = task.timing.samp_clk_rate
        print(f"Actual sampling rate: {actual_sampling_rate:g} S/s")

        data, _ = generate_sine_wave(
            frequency=10.0,
            amplitude=1.0,
            sampling_rate=actual_sampling_rate,
            number_of_samples=number_of_samples,
        )
        task.write(data)
        task.start()

        input("Generating voltage continuously. Press Enter to stop.\n")

        task.stop()


if __name__ == "__main__":
    main()
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=examples/analog_out/cont_gen_voltage_wfm_int_clk_every_n_samples_event.py sha256=18396bbf73d8e7ad559832c64809c4cd2f43a707c30856c4c5649463857268b7 bytes=2936 -->
## FILE: examples/analog_out/cont_gen_voltage_wfm_int_clk_every_n_samples_event.py

- repository: `ni/nidaqmx-python`
- source_path: `examples/analog_out/cont_gen_voltage_wfm_int_clk_every_n_samples_event.py`
- sha256: `18396bbf73d8e7ad559832c64809c4cd2f43a707c30856c4c5649463857268b7`
- bytes: 2936

````python
"""Example of analog output voltage generation with events.

This example demonstrates how to use a Every N Samples events to output a
continuous periodic waveform to an Analog Output Channel
using an internal sample clock. The Every N Samples events indicate when
the specified number of samples generation is complete.
"""

import numpy as np
import numpy.typing

import nidaqmx
from nidaqmx.constants import AcquisitionType


def generate_sine_wave(
    frequency: float,
    amplitude: float,
    sampling_rate: float,
    number_of_samples: int,
    phase_in: float = 0.0,
) -> tuple[numpy.typing.NDArray[numpy.double], float]:
    """Generates a sine wave with a specified phase.

    Args:
        frequency: Specifies the frequency of the sine wave.
        amplitude: Specifies the amplitude of the sine wave.
        sampling_rate: Specifies the sampling rate of the sine wave.
        number_of_samples: Specifies the number of samples to generate.
        phase_in: Specifies the phase of the sine wave in radians.

    Returns:
        Indicates a tuple containing the generated data and the phase
        of the sine wave after generation.
    """
    duration_time = number_of_samples / sampling_rate
    duration_radians = duration_time * 2 * np.pi
    phase_out = (phase_in + duration_radians) % (2 * np.pi)
    t = np.linspace(phase_in, phase_in + duration_radians, number_of_samples, endpoint=False)

    return (amplitude * np.sin(frequency * t), phase_out)


def main():
    """Continuously generates a sine wave using an Every N Samples event."""
    total_write = 0
    with nidaqmx.Task() as task:
        sampling_rate = 1000.0
        number_of_samples = 1000

        def callback(task_handle, every_n_samples_event_type, number_of_samples, callback_data):
            """Callback function for Transferred N samples."""
            nonlocal total_write
            total_write += number_of_samples
            print(f"Transferred data: {number_of_samples} samples. Total {total_write}.", end="\r")

            return 0

        task.ao_channels.add_ao_voltage_chan("Dev1/ao0")
        task.timing.cfg_samp_clk_timing(sampling_rate, sample_mode=AcquisitionType.CONTINUOUS)
        task.register_every_n_samples_transferred_from_buffer_event(1000, callback)

        actual_sampling_rate = task.timing.samp_clk_rate
        print(f"Actual sampling rate: {actual_sampling_rate:g} S/s")

        data, _ = generate_sine_wave(
            frequency=10.0,
            amplitude=1.0,
            sampling_rate=actual_sampling_rate,
            number_of_samples=number_of_samples,
        )
        task.write(data)
        task.start()

        input("Generating voltage continuously. Press Enter to stop.\n")

        task.stop()
        print(f"\nTransferred {total_write} total samples.")


if __name__ == "__main__":
    main()
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=examples/analog_out/cont_gen_voltage_wfm_int_clk_non_regen.py sha256=b97522908260535aa3caf9b05d72a0244d9a8a6cff001cd4e1f8acac79ec29a3 bytes=3693 -->
## FILE: examples/analog_out/cont_gen_voltage_wfm_int_clk_non_regen.py

- repository: `ni/nidaqmx-python`
- source_path: `examples/analog_out/cont_gen_voltage_wfm_int_clk_non_regen.py`
- sha256: `b97522908260535aa3caf9b05d72a0244d9a8a6cff001cd4e1f8acac79ec29a3`
- bytes: 3693

````python
"""Example of analog output voltage generation.

This example demonstrates how to continuously generate an
analog output waveform by providing new data to the output buffer
as the task is running.

This example is useful if you want to generate a non-repeating waveform,
make updates on-the-fly, or generate a frequency that is not an
even divide-down of your sample clock. In this example,
the default frequency value is 17.0 to demonstrate that non-regenerative output
can be used to create a signal with a frequency that is not an even divide-down
of your sample clock.
"""

import numpy as np
import numpy.typing

import nidaqmx
from nidaqmx.constants import AcquisitionType, RegenerationMode


def generate_sine_wave(
    frequency: float,
    amplitude: float,
    sampling_rate: float,
    number_of_samples: int,
    phase_in: float = 0.0,
) -> tuple[numpy.typing.NDArray[numpy.double], float]:
    """Generates a sine wave with a specified phase.

    Args:
        frequency: Specifies the frequency of the sine wave.
        amplitude: Specifies the amplitude of the sine wave.
        sampling_rate: Specifies the sampling rate of the sine wave.
        number_of_samples: Specifies the number of samples to generate.
        phase_in: Specifies the phase of the sine wave in radians.

    Returns:
        Indicates a tuple containing the generated data and the phase
        of the sine wave after generation.
    """
    duration_time = number_of_samples / sampling_rate
    duration_radians = duration_time * 2 * np.pi
    phase_out = (phase_in + duration_radians) % (2 * np.pi)
    t = np.linspace(phase_in, phase_in + duration_radians, number_of_samples, endpoint=False)

    return (amplitude * np.sin(frequency * t), phase_out)


def main():
    """Generate a continuous voltage waveform using an analog output channel of a NI-DAQmx device.

    This function sets up a task to generate a continuous voltage waveform using the specified
    analog output channel of a NI-DAQmx device. It configures the sampling rate, number of samples,
    and regeneration mode of the task. It then enters a loop where it continuously generates a
    sine wave with a specified frequency, amplitude, and phase, and writes the waveform to the
    analog output channel.
    The loop continues until the user interrupts the program by pressing Ctrl+C.

    Args:
        None

    Returns:
        None
    """
    with nidaqmx.Task() as task:
        is_first_run = True
        sampling_rate = 1000.0
        number_of_samples = 1000
        task.ao_channels.add_ao_voltage_chan("Dev1/ao0")
        task.out_stream.regen_mode = RegenerationMode.DONT_ALLOW_REGENERATION
        task.timing.cfg_samp_clk_timing(sampling_rate, sample_mode=AcquisitionType.CONTINUOUS)

        actual_sampling_rate = task.timing.samp_clk_rate
        print(f"Actual sampling rate: {actual_sampling_rate:g} S/s")

        try:
            phase = 0.0
            print("Generating voltage continuously. Press Ctrl+C to stop.")
            while True:
                data, phase = generate_sine_wave(
                    frequency=17.0,
                    amplitude=1.0,
                    sampling_rate=actual_sampling_rate,
                    number_of_samples=number_of_samples,
                    phase_in=phase,
                )
                task.write(data)
                if is_first_run:
                    is_first_run = False
                    task.start()
        except KeyboardInterrupt:
            pass
        finally:
            task.stop()


if __name__ == "__main__":
    main()
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=examples/analog_out/gen_voltage_wfm_int_clk.py sha256=346a46b41a04803f8bf359c6fcefb0fd0e9669859ea6b97807f9dabfa5787524 bytes=909 -->
## FILE: examples/analog_out/gen_voltage_wfm_int_clk.py

- repository: `ni/nidaqmx-python`
- source_path: `examples/analog_out/gen_voltage_wfm_int_clk.py`
- sha256: `346a46b41a04803f8bf359c6fcefb0fd0e9669859ea6b97807f9dabfa5787524`
- bytes: 909

````python
"""Example of analog output voltage generation.

This example demonstrates how to output a finite number of
voltage samples to an Analog Output Channel using an internal
sample clock.
"""

from nitypes.waveform import AnalogWaveform

import nidaqmx
from nidaqmx.constants import AcquisitionType

with nidaqmx.Task() as task:
    total_samples = 1000
    task.ao_channels.add_ao_voltage_chan("Dev1/ao0")
    task.timing.cfg_samp_clk_timing(
        1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=total_samples
    )

    waveform = AnalogWaveform(sample_count=total_samples)
    waveform.raw_data[:] = [5.0 * i / total_samples for i in range(total_samples)]
    waveform.units = "Volts"

    number_of_samples_written = task.write(waveform, auto_start=True)
    print(f"Generating {number_of_samples_written} voltage samples.")
    task.wait_until_done()
    task.stop()
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=examples/analog_out/voltage_update.py sha256=4c65e6b4282f16e7564e59dbad18864f351615d3d8dfec52687317a49cc8a10c bytes=384 -->
## FILE: examples/analog_out/voltage_update.py

- repository: `ni/nidaqmx-python`
- source_path: `examples/analog_out/voltage_update.py`
- sha256: `4c65e6b4282f16e7564e59dbad18864f351615d3d8dfec52687317a49cc8a10c`
- bytes: 384

````python
"""Example of analog output voltage generation.

This example demonstrates how to output a single Voltage Update
(Sample) to an Analog Output Channel.
"""

import nidaqmx

with nidaqmx.Task() as task:
    task.ao_channels.add_ao_voltage_chan("Dev1/ao0")

    number_of_samples_written = task.write(1.1)
    print(f"Generated {number_of_samples_written} voltage sample.")
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=examples/channel_properties.py sha256=f424755da9f993f9eb130c4a9e6bbe634bf3b69c057c41a65977f47189a18001 bytes=709 -->
## FILE: examples/channel_properties.py

- repository: `ni/nidaqmx-python`
- source_path: `examples/channel_properties.py`
- sha256: `f424755da9f993f9eb130c4a9e6bbe634bf3b69c057c41a65977f47189a18001`
- bytes: 709

````python
"""Example for using channel properties."""

import pprint

import nidaqmx

pp = pprint.PrettyPrinter(indent=4)


with nidaqmx.Task() as task:
    ai_channel = task.ai_channels.add_ai_voltage_chan("Dev1/ai0", max_val=0.1, min_val=-0.1)

    print(ai_channel.ai_max)
    print(ai_channel.ai_min)

    ai_channel.ai_max = 5

    print(ai_channel.ai_max)
    print(ai_channel.ai_min)

    ai_channels_1_to_3 = task.ai_channels.add_ai_voltage_chan("Dev1/ai1:3", max_val=10, min_val=-10)

    print(ai_channels_1_to_3.ai_max)
    print(ai_channels_1_to_3.ai_min)

    print(ai_channel.ai_max)
    print(ai_channel.ai_min)

    print(task.ai_channels["Dev1/ai2"].physical_channel.name)
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=examples/counter_in/cnt_dig_event.py sha256=f2643b994be6a60c77efbdf7977ff967a17a546fd17daf303bd725340e7762ba bytes=932 -->
## FILE: examples/counter_in/cnt_dig_event.py

- repository: `ni/nidaqmx-python`
- source_path: `examples/counter_in/cnt_dig_event.py`
- sha256: `f2643b994be6a60c77efbdf7977ff967a17a546fd17daf303bd725340e7762ba`
- bytes: 932

````python
"""Example of counter input edge count operation.

This example demonstrates how to count digital events on a
Counter Input Channel. The Initial Count, Count Direction, and
Edge are all configurable.
"""

import nidaqmx
from nidaqmx.constants import CountDirection, Edge

with nidaqmx.Task() as task:
    channel = task.ci_channels.add_ci_count_edges_chan(
        "Dev1/ctr0",
        edge=Edge.RISING,
        initial_count=0,
        count_direction=CountDirection.COUNT_UP,
    )
    channel.ci_count_edges_term = "/Dev1/PFI8"

    print("Continuously polling. Press Ctrl+C to stop.")
    task.start()

    try:
        edge_counts = 0
        while True:
            edge_counts = task.read()
            print(f"Acquired count: {edge_counts:n}", end="\r")
    except KeyboardInterrupt:
        pass
    finally:
        task.stop()
        print(f"\nAcquired {edge_counts:n} total counts.")
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=examples/counter_in/cont_cnt_buff_event_ext_clk.py sha256=9673a71a8412dad777254b49b86e7e2ebe0451cc31e48d409e2e704175c89fb9 bytes=1205 -->
## FILE: examples/counter_in/cont_cnt_buff_event_ext_clk.py

- repository: `ni/nidaqmx-python`
- source_path: `examples/counter_in/cont_cnt_buff_event_ext_clk.py`
- sha256: `9673a71a8412dad777254b49b86e7e2ebe0451cc31e48d409e2e704175c89fb9`
- bytes: 1205

````python
"""Example of counter input edge count operation.

This example demonstrates how to count buffered digital events
on a Counter Input Channel. The Initial Count, Count Direction,
Edge, and Sample Clock Source are all configurable.
"""

import nidaqmx
from nidaqmx.constants import AcquisitionType, CountDirection, Edge

with nidaqmx.Task() as task:
    channel = task.ci_channels.add_ci_count_edges_chan(
        "Dev1/ctr0",
        edge=Edge.RISING,
        initial_count=0,
        count_direction=CountDirection.COUNT_UP,
    )
    task.timing.cfg_samp_clk_timing(
        1000, source="/Dev1/PFI9", sample_mode=AcquisitionType.CONTINUOUS
    )
    channel.ci_count_edges_term = "/Dev1/PFI8"

    print("Continuously polling. Press Ctrl+C to stop.")
    task.start()

    try:
        total_read = 0
        while True:
            edge_counts = task.read(number_of_samples_per_channel=1000)
            total_read += len(edge_counts)
            print(f"Acquired data: {len(edge_counts)} samples. Total {total_read}.", end="\r")
    except KeyboardInterrupt:
        pass
    finally:
        task.stop()
        print(f"\nAcquired {total_read} total samples.")
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=examples/counter_in/cont_read_buff_freq.py sha256=ac97bf14fd6b65326d9898c14ffda4a809b4622846c2f15a2a70db33bfcc1746 bytes=1159 -->
## FILE: examples/counter_in/cont_read_buff_freq.py

- repository: `ni/nidaqmx-python`
- source_path: `examples/counter_in/cont_read_buff_freq.py`
- sha256: `ac97bf14fd6b65326d9898c14ffda4a809b4622846c2f15a2a70db33bfcc1746`
- bytes: 1159

````python
"""Example of counter input frequency acquisition.

This example demonstrates how to continuously measure buffered frequency
using one counter on a Counter Input Channel. The Edge, Minimum Value
and Maximum Value are all configurable.
"""

import nidaqmx
from nidaqmx.constants import AcquisitionType, Edge, FrequencyUnits


with nidaqmx.Task() as task:
    channel = task.ci_channels.add_ci_freq_chan(
        "Dev1/ctr0",
        min_val=2.0,
        max_val=100000.0,
        units=FrequencyUnits.HZ,
        edge=Edge.RISING,
    )
    channel.ci_freq_term = "/Dev1/PFI8"
    task.timing.cfg_implicit_timing(sample_mode=AcquisitionType.CONTINUOUS)

    print("Continuously polling. Press Ctrl+C to stop.")
    task.start()

    try:
        total_read = 0
        while True:
            frequencies = task.read(number_of_samples_per_channel=1000)
            total_read += len(frequencies)
            print(f"Acquired data: {len(frequencies)} samples. Total {total_read}.", end="\r")
    except KeyboardInterrupt:
        pass
    finally:
        task.stop()
        print(f"\nAcquired {total_read} total samples.")
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=examples/counter_in/read_freq.py sha256=caec6a6543ff2eebd748b590a51696d4a22371ead672e928cfefd45cfc18c7fd bytes=671 -->
## FILE: examples/counter_in/read_freq.py

- repository: `ni/nidaqmx-python`
- source_path: `examples/counter_in/read_freq.py`
- sha256: `caec6a6543ff2eebd748b590a51696d4a22371ead672e928cfefd45cfc18c7fd`
- bytes: 671

````python
"""Example of counter input frequency acquisition.

This example demonstrates how to measure frequency using one
counter on a Counter Input Channel. The Edge, Minimum Value and
Maximum Value are all configurable.
"""

import nidaqmx
from nidaqmx.constants import Edge, FrequencyUnits


with nidaqmx.Task() as task:
    channel = task.ci_channels.add_ci_freq_chan(
        "Dev1/ctr0",
        min_val=2.0,
        max_val=100000.0,
        units=FrequencyUnits.HZ,
        edge=Edge.RISING,
    )
    channel.ci_freq_term = "/Dev1/PFI8"

    task.start()

    data = task.read()
    print(f"Acquired frequency: {data:.2f} Hz")

    task.stop()
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=examples/counter_in/read_pulse_freq.py sha256=118d485a6b96a0681c96fe73af0048b4dabd6febd1f6ca8588e3751c96e1a2e6 bytes=638 -->
## FILE: examples/counter_in/read_pulse_freq.py

- repository: `ni/nidaqmx-python`
- source_path: `examples/counter_in/read_pulse_freq.py`
- sha256: `118d485a6b96a0681c96fe73af0048b4dabd6febd1f6ca8588e3751c96e1a2e6`
- bytes: 638

````python
"""Example of CI pulse frequency operation.

This example demonstrates how to configure a pulse measurement to acquire frequency and duty cycle.
"""

import nidaqmx
from nidaqmx.constants import FrequencyUnits

with nidaqmx.Task() as task:
    channel = task.ci_channels.add_ci_pulse_chan_freq(
        "Dev1/ctr0", "", min_val=2.0, max_val=100000.0, units=FrequencyUnits.HZ
    )
    channel.ci_pulse_freq_term = "/Dev1/PFI8"

    task.start()

    data = task.read()
    print(f"Acquired data:")
    print(f"Frequency: {data.freq:.2f} Hz")
    print(f"Duty cycle: {(data.duty_cycle * 100):.2f}%")

    task.stop()
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=examples/counter_out/cont_gen_dig_pulse_train.py sha256=4fb0649d1e2c78fec98281a18f8d724b985774404b111d924606edcd373b0f0f bytes=716 -->
## FILE: examples/counter_out/cont_gen_dig_pulse_train.py

- repository: `ni/nidaqmx-python`
- source_path: `examples/counter_out/cont_gen_dig_pulse_train.py`
- sha256: `4fb0649d1e2c78fec98281a18f8d724b985774404b111d924606edcd373b0f0f`
- bytes: 716

````python
"""Example for continuously generating digital pulse train.

This example demonstrates how to generate a continuous digital
pulse train from a Counter Output Channel. The Frequency, Duty
Cycle, and Idle State are all configurable.
"""

import nidaqmx
from nidaqmx.constants import AcquisitionType, Level

with nidaqmx.Task() as task:
    channel = task.co_channels.add_co_pulse_chan_freq(
        "Dev1/ctr0", idle_state=Level.LOW, initial_delay=0.0, freq=1.0, duty_cycle=0.5
    )
    channel.co_pulse_term = "/Dev1/PFI12"
    task.timing.cfg_implicit_timing(sample_mode=AcquisitionType.CONTINUOUS)
    task.start()

    input("Generating pulse train. Press Enter to stop.\n")

    task.stop()
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=examples/counter_out/cont_gen_dig_pulse_train_buff_ext_clk.py sha256=9a486c529fb467e8a822d36f2861a610416b7cc9494dc5c36edbdb304e3d0300 bytes=1276 -->
## FILE: examples/counter_out/cont_gen_dig_pulse_train_buff_ext_clk.py

- repository: `ni/nidaqmx-python`
- source_path: `examples/counter_out/cont_gen_dig_pulse_train_buff_ext_clk.py`
- sha256: `9a486c529fb467e8a822d36f2861a610416b7cc9494dc5c36edbdb304e3d0300`
- bytes: 1276

````python
"""Example for continuously generating digital pulse train with external timing.

This example demonstrates how to generate a continuous buffered
sample clocked digital pulse train from a Counter Output
Channel. The Frequency, Duty Cycle, and Idle State are all
configurable. The default data generated is a pulse train with a
fixed frequency but a duty cycle that varies based on the Duty
Cycle Max/Min and the signal type. The duty cycle will update
with each sample clock edge.
"""

import nidaqmx
from nidaqmx.constants import AcquisitionType, Level
from nidaqmx.types import CtrFreq

with nidaqmx.Task() as task:
    duty_min = 0.5
    duty_max = 0.8
    duty_step = (duty_max - duty_min) / 1000
    ctr_freq_data = [CtrFreq(1000, (duty_min + duty_step * i)) for i in range(1000)]

    channel = task.co_channels.add_co_pulse_chan_freq(
        "Dev1/ctr0", idle_state=Level.LOW, initial_delay=0.0, freq=1.0, duty_cycle=0.5
    )
    channel.co_pulse_term = "/Dev1/PFI12"
    task.timing.cfg_samp_clk_timing(1000.0, "/Dev1/PFI0", sample_mode=AcquisitionType.CONTINUOUS)
    task.out_stream.output_buf_size = 1000
    task.write(ctr_freq_data)
    task.start()

    input("Generating pulse train. Press Enter to stop.\n")

    task.stop()
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=examples/counter_out/cont_gen_dig_pulse_train_buff_implicit.py sha256=60440cf99c83886916f78d483b2481606d23be401b8b2c9c630015688bd0f23e bytes=1209 -->
## FILE: examples/counter_out/cont_gen_dig_pulse_train_buff_implicit.py

- repository: `ni/nidaqmx-python`
- source_path: `examples/counter_out/cont_gen_dig_pulse_train_buff_implicit.py`
- sha256: `60440cf99c83886916f78d483b2481606d23be401b8b2c9c630015688bd0f23e`
- bytes: 1209

````python
"""Example for continuously generating digital pulse train with implicit timing.

This example demonstrates how to generate a continuous buffered
implicit timed digital pulse train from a Counter Output
Channel. The Frequency, Duty Cycle, and Idle State are all
configurable. The default data generated is a pulse train with a
fixed frequency but a duty cycle that varies based on the Duty
Cycle Max/Min and the signal type. The duty cycle will update
with each sample generated.
"""

import nidaqmx
from nidaqmx.constants import AcquisitionType, Level
from nidaqmx.types import CtrFreq

with nidaqmx.Task() as task:
    duty_min = 0.5
    duty_max = 0.8
    duty_step = (duty_max - duty_min) / 1000
    ctr_freq_data = [CtrFreq(1000, (duty_min + duty_step * i)) for i in range(1000)]

    channel = task.co_channels.add_co_pulse_chan_freq(
        "Dev1/ctr0", idle_state=Level.LOW, initial_delay=0.0, freq=1.0, duty_cycle=0.5
    )
    channel.co_pulse_term = "/Dev1/PFI12"
    task.timing.cfg_implicit_timing(sample_mode=AcquisitionType.CONTINUOUS)
    task.write(ctr_freq_data)
    task.start()

    input("Generating pulse train. Press Enter to stop.\n")

    task.stop()
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=examples/counter_out/write_single_dig_pulse.py sha256=a201d9ce81815eab51fcac4e7da1b75aebf3b4ea6b0ea1d76e3ac9898dc1a9a5 bytes=593 -->
## FILE: examples/counter_out/write_single_dig_pulse.py

- repository: `ni/nidaqmx-python`
- source_path: `examples/counter_out/write_single_dig_pulse.py`
- sha256: `a201d9ce81815eab51fcac4e7da1b75aebf3b4ea6b0ea1d76e3ac9898dc1a9a5`
- bytes: 593

````python
"""Example for generating a single digital pulse.

This example demonstrates how to generate a single digital pulse
from a Counter Output Channel. The Initial Delay, High Time, Low
Time, and Idle State are all configurable.
"""

import nidaqmx
from nidaqmx.constants import Level

with nidaqmx.Task() as task:
    channel = task.co_channels.add_co_pulse_chan_time(
        "Dev1/ctr0", idle_state=Level.LOW, initial_delay=0.0, low_time=0.5, high_time=1.0
    )
    channel.co_pulse_term = "/Dev1/PFI12"

    task.start()
    task.wait_until_done(timeout=10)
    task.stop()
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=examples/digital_in/acq_dig_port_int_clk.py sha256=9ce53c4358bf0b3340de0067aaf6c7c13e3fafb7cd6c251b8626d05b1168413e bytes=610 -->
## FILE: examples/digital_in/acq_dig_port_int_clk.py

- repository: `ni/nidaqmx-python`
- source_path: `examples/digital_in/acq_dig_port_int_clk.py`
- sha256: `9ce53c4358bf0b3340de0067aaf6c7c13e3fafb7cd6c251b8626d05b1168413e`
- bytes: 610

````python
"""Example for reading digital signals.

This example demonstrates how to input a finite digital pattern
using the DAQ device's internal clock.
"""

import nidaqmx
from nidaqmx.constants import AcquisitionType, LineGrouping, READ_ALL_AVAILABLE


with nidaqmx.Task() as task:
    task.di_channels.add_di_chan("Dev1/port0", line_grouping=LineGrouping.CHAN_FOR_ALL_LINES)
    task.timing.cfg_samp_clk_timing(1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=50)

    data = task.read(READ_ALL_AVAILABLE)
    print("Acquired data: [" + ", ".join(f"{value:#x}" for value in data) + "]")
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=examples/digital_in/acq_dig_port_int_clk_wfm.py sha256=a8e5c517801f9b3a291791410173cdfeb5e48b93251b6cdc397f2637f7dbcadb bytes=960 -->
## FILE: examples/digital_in/acq_dig_port_int_clk_wfm.py

- repository: `ni/nidaqmx-python`
- source_path: `examples/digital_in/acq_dig_port_int_clk_wfm.py`
- sha256: `a8e5c517801f9b3a291791410173cdfeb5e48b93251b6cdc397f2637f7dbcadb`
- bytes: 960

````python
"""Example for reading digital signals.

This example demonstrates how to input a finite digital pattern
using the DAQ device's internal clock.
"""

import numpy as np

import nidaqmx
from nidaqmx.constants import (
    READ_ALL_AVAILABLE,
    AcquisitionType,
    LineGrouping,
)

np.set_printoptions(linewidth=120)  # ensure signal.data prints on a single line

with nidaqmx.Task() as task:
    task.di_channels.add_di_chan(
        "cdaqTesterMod4/port0", line_grouping=LineGrouping.CHAN_FOR_ALL_LINES
    )
    task.timing.cfg_samp_clk_timing(1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=50)

    waveform = task.read_waveform(READ_ALL_AVAILABLE)
    print("Acquired data:")
    for signal in waveform.signals:
        print(f"{signal.name}: {signal.data}")
    print(f"Channel name: {waveform.channel_name}")
    print(f"t0: {waveform.timing.start_time}")
    print(f"dt: {waveform.timing.sample_interval}")
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=examples/digital_in/cont_acq_dig_lines_int_clk.py sha256=41519832b9f4f3c5832d80ba3d0c759e0c3b994f2f8014cd0ec5343afbae3a69 bytes=952 -->
## FILE: examples/digital_in/cont_acq_dig_lines_int_clk.py

- repository: `ni/nidaqmx-python`
- source_path: `examples/digital_in/cont_acq_dig_lines_int_clk.py`
- sha256: `41519832b9f4f3c5832d80ba3d0c759e0c3b994f2f8014cd0ec5343afbae3a69`
- bytes: 952

````python
"""Example for reading digital signals.

This example demonstrates how to acquire a continuous digital
waveform using the DAQ device's internal clock.
"""

import nidaqmx
from nidaqmx.constants import AcquisitionType, LineGrouping


with nidaqmx.Task() as task:
    task.di_channels.add_di_chan("Dev1/port0/line0:3", line_grouping=LineGrouping.CHAN_PER_LINE)
    task.timing.cfg_samp_clk_timing(1000.0, sample_mode=AcquisitionType.CONTINUOUS)
    task.start()
    print("Acquiring samples continuously. Press Ctrl+C to stop.")

    try:
        total_read = 0
        while True:
            data = task.read(number_of_samples_per_channel=1000)
            read = len(data)
            total_read += read
            print(f"Acquired data: {read} samples. Total {total_read}.", end="\r")
    except KeyboardInterrupt:
        pass
    finally:
        task.stop()
        print(f"\nAcquired {total_read} total samples.")
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=examples/digital_in/read_dig_lines.py sha256=31cee2ab1ea602976407bafef780d9c6c906a71687c2e5cfb97ffd25e72b87e8 bytes=396 -->
## FILE: examples/digital_in/read_dig_lines.py

- repository: `ni/nidaqmx-python`
- source_path: `examples/digital_in/read_dig_lines.py`
- sha256: `31cee2ab1ea602976407bafef780d9c6c906a71687c2e5cfb97ffd25e72b87e8`
- bytes: 396

````python
"""Example for reading digital signals.

This example demonstrates how to read values from one or more
digital input channels.
"""

import nidaqmx
from nidaqmx.constants import LineGrouping


with nidaqmx.Task() as task:
    task.di_channels.add_di_chan("Dev1/port0/line0:3", line_grouping=LineGrouping.CHAN_PER_LINE)

    data = task.read()
    print(f"Acquired data: {data}")
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=examples/digital_in/read_dig_port.py sha256=0293e68144f2d34b01fe8571deb558e09d16aaff3a5438c4a803998b6de31ade bytes=383 -->
## FILE: examples/digital_in/read_dig_port.py

- repository: `ni/nidaqmx-python`
- source_path: `examples/digital_in/read_dig_port.py`
- sha256: `0293e68144f2d34b01fe8571deb558e09d16aaff3a5438c4a803998b6de31ade`
- bytes: 383

````python
"""Example for reading a digital signal.

This example demonstrates how to read values from a digital
input port.
"""

import nidaqmx
from nidaqmx.constants import LineGrouping


with nidaqmx.Task() as task:
    task.di_channels.add_di_chan("Dev1/port0", line_grouping=LineGrouping.CHAN_FOR_ALL_LINES)

    data = task.read()
    print(f"Acquired data: {data:#x}")
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=examples/digital_out/cont_gen_dig_port_int_clk.py sha256=f8170109991cdda1b9705eb928f852e6a6b54e7d4a3f79d758df59fdd29a11d5 bytes=838 -->
## FILE: examples/digital_out/cont_gen_dig_port_int_clk.py

- repository: `ni/nidaqmx-python`
- source_path: `examples/digital_out/cont_gen_dig_port_int_clk.py`
- sha256: `f8170109991cdda1b9705eb928f852e6a6b54e7d4a3f79d758df59fdd29a11d5`
- bytes: 838

````python
"""Example for generating digital signals.

This example demonstrates how to output a continuous digital
pattern using the DAQ device's clock.
"""

import nidaqmx
from nidaqmx.constants import AcquisitionType, LineGrouping

with nidaqmx.Task() as task:
    chan = task.do_channels.add_do_chan("Dev1/port0", line_grouping=LineGrouping.CHAN_FOR_ALL_LINES)
    task.timing.cfg_samp_clk_timing(10.0, sample_mode=AcquisitionType.CONTINUOUS)

    # Generate a walking 1's pattern.
    data = [1 << i for i in range(chan.do_num_lines)]

    print("Writing data:")
    for i, value in enumerate(data):
        print("sample {:2}: 0x{:0{width}X}".format(i, value, width=chan.do_num_lines // 4))

    task.write(data)
    task.start()

    input("Generating voltage continuously. Press Enter to stop.\n")

    task.stop()
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=examples/digital_out/cont_gen_dig_port_int_clk_wfm.py sha256=3058a3a4b398a1eaf126b6c19dcc611b9226e6ed6d81d6a8fb64a7f12df8d030 bytes=1158 -->
## FILE: examples/digital_out/cont_gen_dig_port_int_clk_wfm.py

- repository: `ni/nidaqmx-python`
- source_path: `examples/digital_out/cont_gen_dig_port_int_clk_wfm.py`
- sha256: `3058a3a4b398a1eaf126b6c19dcc611b9226e6ed6d81d6a8fb64a7f12df8d030`
- bytes: 1158

````python
"""Example for generating digital signals using the DigitalWaveform data type.

This example demonstrates how to output a continuous digital
pattern using the DAQ device's clock.
"""

import numpy as np
from nitypes.waveform import DigitalWaveform

import nidaqmx
from nidaqmx.constants import AcquisitionType, LineGrouping

np.set_printoptions(linewidth=120)  # ensure signal.data prints on a single line

with nidaqmx.Task() as task:
    chan = task.do_channels.add_do_chan("Dev1/port0", line_grouping=LineGrouping.CHAN_FOR_ALL_LINES)
    task.timing.cfg_samp_clk_timing(10.0, sample_mode=AcquisitionType.CONTINUOUS)

    # Generate a walking 1's pattern.
    waveform = DigitalWaveform.from_port(
        [1 << i for i in range(chan.do_num_lines)], mask=(1 << chan.do_num_lines) - 1
    )
    for signal in waveform.signals:
        signal.name = f"line {signal.signal_index:2}"

    print("Writing data:")
    for signal in waveform.signals:
        print(f"{signal.name}: {signal.data}")

    task.write(waveform)
    task.start()

    input("Generating voltage continuously. Press Enter to stop.\n")

    task.stop()
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=examples/digital_out/gen_dig_line_int_clk.py sha256=6103b09a0a787efa7c5566206671db30e788b072841a4134ba2cc6d7f21f37c6 bytes=723 -->
## FILE: examples/digital_out/gen_dig_line_int_clk.py

- repository: `ni/nidaqmx-python`
- source_path: `examples/digital_out/gen_dig_line_int_clk.py`
- sha256: `6103b09a0a787efa7c5566206671db30e788b072841a4134ba2cc6d7f21f37c6`
- bytes: 723

````python
"""Example for generating digital signals.

This example demonstrates how to output a finite digital
waveform using the DAQ device's internal clock.
"""

import nidaqmx
from nidaqmx.constants import AcquisitionType, LineGrouping

with nidaqmx.Task() as task:
    data = [bool(i % 2) for i in range(1000)]

    task.do_channels.add_do_chan("Dev1/port0/line0", line_grouping=LineGrouping.CHAN_PER_LINE)
    task.timing.cfg_samp_clk_timing(
        1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=len(data)
    )

    number_of_samples_written = task.write(data)
    task.start()
    print(f"Generating {number_of_samples_written} voltage samples.")
    task.wait_until_done()
    task.stop()
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=examples/digital_out/write_dig_lines.py sha256=1c4f83f713ff6476357a3c9b92b1f5d9ce93d98991e098a6cacb4b8fc21916a6 bytes=418 -->
## FILE: examples/digital_out/write_dig_lines.py

- repository: `ni/nidaqmx-python`
- source_path: `examples/digital_out/write_dig_lines.py`
- sha256: `1c4f83f713ff6476357a3c9b92b1f5d9ce93d98991e098a6cacb4b8fc21916a6`
- bytes: 418

````python
"""Example for generating digital signals.

This example demonstrates how to write values to a digital
output channel.
"""

import nidaqmx
from nidaqmx.constants import LineGrouping

with nidaqmx.Task() as task:
    data = [True, False, True, False]

    task.do_channels.add_do_chan("Dev1/port0/line0:3", line_grouping=LineGrouping.CHAN_PER_LINE)
    task.start()
    task.write(data)
    task.stop()
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=examples/digital_out/write_dig_port.py sha256=6b729cd212f8ae26f693da1ea086fd36625ff31779a0a0c2e128d2b348f903f0 bytes=396 -->
## FILE: examples/digital_out/write_dig_port.py

- repository: `ni/nidaqmx-python`
- source_path: `examples/digital_out/write_dig_port.py`
- sha256: `6b729cd212f8ae26f693da1ea086fd36625ff31779a0a0c2e128d2b348f903f0`
- bytes: 396

````python
"""Example for generating digital signals.

This example demonstrates how to write values to a digital
output port.
"""

import nidaqmx
from nidaqmx.constants import LineGrouping

with nidaqmx.Task() as task:
    data = 0xFFFFFFFF

    task.do_channels.add_do_chan("Dev1/port0", line_grouping=LineGrouping.CHAN_FOR_ALL_LINES)
    task.start()
    task.write(data)
    task.stop()
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=examples/every_n_samples_event.py sha256=7be307796f1175dd8c08601f57b473d79dd3b189eb78e5abc04cbbba4bab4b01 bytes=899 -->
## FILE: examples/every_n_samples_event.py

- repository: `ni/nidaqmx-python`
- source_path: `examples/every_n_samples_event.py`
- sha256: `7be307796f1175dd8c08601f57b473d79dd3b189eb78e5abc04cbbba4bab4b01`
- bytes: 899

````python
"""Example for reading signals for every n samples."""

import pprint

import nidaqmx
from nidaqmx.constants import AcquisitionType

pp = pprint.PrettyPrinter(indent=4)


with nidaqmx.Task() as task:
    task.ai_channels.add_ai_voltage_chan("Dev1/ai0")

    task.timing.cfg_samp_clk_timing(1000, sample_mode=AcquisitionType.CONTINUOUS)

    samples: list[float] = []

    def callback(task_handle, every_n_samples_event_type, number_of_samples, callback_data):
        """Callback function for reading signals."""
        print("Every N Samples callback invoked.")

        samples.extend(task.read(number_of_samples_per_channel=1000))

        return 0

    task.register_every_n_samples_acquired_into_buffer_event(1000, callback)

    task.start()

    input("Running task. Press Enter to stop and see number of " "accumulated samples.\n")

    print(len(samples))
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=examples/nidaqmx_warnings.py sha256=cf19edef45461dfba5c75703eafa7bf6a0f351b49cc77226b4cad3b8263ae6fb bytes=1796 -->
## FILE: examples/nidaqmx_warnings.py

- repository: `ni/nidaqmx-python`
- source_path: `examples/nidaqmx_warnings.py`
- sha256: `cf19edef45461dfba5c75703eafa7bf6a0f351b49cc77226b4cad3b8263ae6fb`
- bytes: 1796

````python
"""Example for catching warnings in DAQmx."""

import warnings

import nidaqmx
from nidaqmx.error_codes import DAQmxWarnings

# By default warnings are shown.
with nidaqmx.Task() as task:
    task.ao_channels.add_ao_voltage_chan("Dev1/ao0")
    task.timing.cfg_samp_clk_timing(1000)

    task.write([1.1, 2.2, 3.3, 4.4, 5.5], auto_start=True)
    task.stop()


# Catching warnings using the built-in warnings context manager.
with nidaqmx.Task() as task:
    task.ao_channels.add_ao_voltage_chan("Dev1/ao0")
    task.timing.cfg_samp_clk_timing(1000)

    with warnings.catch_warnings(record=True) as w:
        task.write([1.1, 2.2, 3.3, 4.4, 5.5], auto_start=True)
        task.stop()

        if not task.devices[0].is_simulated:
            # Verify some things
            assert len(w) == 1
            assert issubclass(w[-1].category, nidaqmx.DaqWarning)

        if w:
            print(f"DaqWarning caught: {w[-1].message}\n")


# Raising warnings as exceptions.
with nidaqmx.Task() as task:
    task.ao_channels.add_ao_voltage_chan("Dev1/ao0")
    task.timing.cfg_samp_clk_timing(1000)

    warnings.filterwarnings("error", category=nidaqmx.DaqWarning)

    try:
        task.write([1.1, 2.2, 3.3, 4.4, 5.5], auto_start=True)
        task.stop()
    except nidaqmx.DaqWarning as e:
        print(f"DaqWarning caught as exception: {e}\n")
        assert e.error_code == DAQmxWarnings.STOPPED_BEFORE_DONE


# Suppressing DaqWarnings.
print("Suppressing warnings.")
warnings.filterwarnings("ignore", category=nidaqmx.DaqWarning)

with nidaqmx.Task() as task:
    task.ao_channels.add_ao_voltage_chan("Dev1/ao0")
    task.timing.cfg_samp_clk_timing(1000)

    task.write([1.1, 2.2, 3.3, 4.4, 5.5], auto_start=True)
    task.stop()
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=examples/playrec.py sha256=c1c7e975314c08ddb5f70ad306915a8cf40def42015234f0fb32f9853bc9e5bb bytes=3415 -->
## FILE: examples/playrec.py

- repository: `ni/nidaqmx-python`
- source_path: `examples/playrec.py`
- sha256: `c1c7e975314c08ddb5f70ad306915a8cf40def42015234f0fb32f9853bc9e5bb`
- bytes: 3415

````python
"""Simultaneous read and write with NI USB-4431 or similar device."""

import numpy as np

import nidaqmx
import nidaqmx.system
from nidaqmx.constants import WAIT_INFINITELY


def query_devices():
    """Queries all the device information connected to the local system."""
    local = nidaqmx.system.System.local()
    for device in local.devices:
        print(f"Device Name: {device.name}, Product Type: {device.product_type}")
        print("Input channels:", [chan.name for chan in device.ai_physical_chans])
        print("Output channels:", [chan.name for chan in device.ao_physical_chans])


def play_record(data, sample_rate, input_mapping, output_mapping):
    """Simultaneous playback and recording though NI device.

    Parameters:
    -----------
    data: array_like, shape (num_samples, len(output_mapping))
      Data to be send to output channels.
    sample_rate: int
      Sample rate
    input_mapping: list of str
      Input device channels
    output_mapping: list of str
      Output device channels

    Returns
    -------
    ndarray, shape (num_samples, len(input_mapping))
      Recorded data

    """
    devices = nidaqmx.system.System.local().devices
    data = np.asarray(data).T
    num_samples = data.shape[1]

    with nidaqmx.Task() as read_task, nidaqmx.Task() as write_task:
        for i, o in enumerate(output_mapping):
            ao_channel = write_task.ao_channels.add_ao_voltage_chan(
                o,
                min_val=devices[o].ao_voltage_rngs[0],
                max_val=devices[o].ao_voltage_rngs[1],
            )
            min_data, max_data = np.min(data[i]), np.max(data[i])
            if ((max_data > ao_channel.ao_max) | (min_data < ao_channel.ao_min)).any():
                raise ValueError(
                    f"Data range ({min_data:.2f}, {max_data:.2f}) exceeds output range of "
                    f"{o} ({ao_channel.ao_min:.2f}, {ao_channel.ao_max:.2f})."
                )
        for i in input_mapping:
            read_task.ai_channels.add_ai_voltage_chan(i)

        for task in (read_task, write_task):
            task.timing.cfg_samp_clk_timing(
                rate=sample_rate, source="OnboardClock", samps_per_chan=num_samples
            )

        # trigger write_task as soon as read_task starts
        write_task.triggers.start_trigger.cfg_dig_edge_start_trig(
            read_task.triggers.start_trigger.term
        )
        # squeeze as Task.write expects 1d array for 1 channel
        write_task.write(data.squeeze(), auto_start=False)
        # write_task doesn't start at read_task's start_trigger without this
        write_task.start()
        # do not time out for long inputs
        input_data = read_task.read(num_samples, timeout=WAIT_INFINITELY)

    return np.asarray(input_data).T


if __name__ == "__main__":
    query_devices()
    # Prints in this example:
    #   Device Name: Dev2, Product Type: USB-4431
    #   Input channels: ['Dev2/ai0', 'Dev2/ai1', 'Dev2/ai2', 'Dev2/ai3']
    #   Output channels: ['Dev2/ao0']

    # excite through one output and record at three inputs
    outdata = np.random.normal(size=(5000, 1)) * 0.01
    input_data = play_record(
        outdata,
        sample_rate=96000,
        input_mapping=["Dev2/ai0", "Dev2/ai1", "Dev2/ai2"],
        output_mapping=["Dev2/ao0"],
    )
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=examples/pwr_hw_timed.py sha256=30ec7740113f4ba744985e71fbcdc21e0ae9892d1aa058a0ea9418f37b4ceb27 bytes=1565 -->
## FILE: examples/pwr_hw_timed.py

- repository: `ni/nidaqmx-python`
- source_path: `examples/pwr_hw_timed.py`
- sha256: `30ec7740113f4ba744985e71fbcdc21e0ae9892d1aa058a0ea9418f37b4ceb27`
- bytes: 1565

````python
"""Examples for hw timed power operation."""

import pprint

import nidaqmx
from nidaqmx.constants import AcquisitionType, PowerIdleOutputBehavior, Sense

pp = pprint.PrettyPrinter(indent=4)


with nidaqmx.Task() as task:
    # Channel Settings
    voltage_setpoint = 0
    current_setpoint = 0.03
    output_enable = True
    idle_output_behavior = PowerIdleOutputBehavior.OUTPUT_DISABLED
    remote_sense = Sense.LOCAL

    # Timing Settings
    sample_rate = 10.0
    number_of_samples_per_channel = 10

    chan = task.ai_channels.add_ai_power_chan(
        "TS1Mod1/power", voltage_setpoint, current_setpoint, output_enable
    )
    chan.pwr_idle_output_behavior = idle_output_behavior
    chan.pwr_remote_sense = remote_sense

    task.timing.cfg_samp_clk_timing(sample_rate, sample_mode=AcquisitionType.CONTINUOUS)

    task.start()

    try:
        print("Press Ctrl+C to stop")
        while True:
            # Note: at runtime, you can write the following channel attributes:
            # * pwr_voltage_setpoint
            # * pwr_current_setpoint
            # * pwr_output_enable

            data = task.read(number_of_samples_per_channel=number_of_samples_per_channel)

            print(f"Data:")
            pp.pprint(data)

            print(f"output state: {chan.pwr_output_state}")
            if task.in_stream.overtemperature_chans_exist:
                print(f"overtemperature chans: {task.in_stream.overtemperature_chans}")
    except KeyboardInterrupt:
        pass

    task.stop()
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=examples/pwr_hw_timed_stream.py sha256=1e21c00d1c236685c4ba895c849b9a74795a9f5f8143d90a52b29496a87c5141 bytes=2070 -->
## FILE: examples/pwr_hw_timed_stream.py

- repository: `ni/nidaqmx-python`
- source_path: `examples/pwr_hw_timed_stream.py`
- sha256: `1e21c00d1c236685c4ba895c849b9a74795a9f5f8143d90a52b29496a87c5141`
- bytes: 2070

````python
"""Examples for hw timed power stream operation."""

import pprint

import numpy

import nidaqmx
from nidaqmx.constants import AcquisitionType, PowerIdleOutputBehavior, Sense
from nidaqmx.stream_readers import PowerSingleChannelReader

pp = pprint.PrettyPrinter(indent=4)


with nidaqmx.Task() as task:
    # Channel Settings
    voltage_setpoint = 0
    current_setpoint = 0.03
    output_enable = True
    idle_output_behavior = PowerIdleOutputBehavior.OUTPUT_DISABLED
    remote_sense = Sense.LOCAL

    # Timing Settings
    sample_rate = 100.0
    number_of_samples_per_channel = 100

    chan = task.ai_channels.add_ai_power_chan(
        "TS1Mod1/power", voltage_setpoint, current_setpoint, output_enable
    )
    chan.pwr_idle_output_behavior = idle_output_behavior
    chan.pwr_remote_sense = remote_sense

    task.timing.cfg_samp_clk_timing(sample_rate, sample_mode=AcquisitionType.CONTINUOUS)

    stream = PowerSingleChannelReader(task.in_stream)
    voltage_data = numpy.zeros(number_of_samples_per_channel, dtype=numpy.float64)
    current_data = numpy.zeros(number_of_samples_per_channel, dtype=numpy.float64)

    task.start()

    try:
        print("Press Ctrl+C to stop")
        while True:
            # Note: at runtime, you can write the following channel attributes:
            # * pwr_voltage_setpoint
            # * pwr_current_setpoint
            # * pwr_output_enable

            stream.read_many_sample(
                voltage_data,
                current_data,
                number_of_samples_per_channel=number_of_samples_per_channel,
            )

            print(f"Voltage Data:")
            pp.pprint(voltage_data)

            print(f"Current Data:")
            pp.pprint(current_data)

            print(f"output state: {chan.pwr_output_state}")
            if task.in_stream.overtemperature_chans_exist:
                print(f"overtemperature chans: {task.in_stream.overtemperature_chans}")
    except KeyboardInterrupt:
        pass

    task.stop()
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=examples/pwr_sw_timed.py sha256=814bdfcc262b383ced950139862eed9fb694fdb558fbe13580c40d12acec758b bytes=1350 -->
## FILE: examples/pwr_sw_timed.py

- repository: `ni/nidaqmx-python`
- source_path: `examples/pwr_sw_timed.py`
- sha256: `814bdfcc262b383ced950139862eed9fb694fdb558fbe13580c40d12acec758b`
- bytes: 1350

````python
"""Examples for sw timed power operation."""

import pprint
import time

import nidaqmx
from nidaqmx.constants import PowerIdleOutputBehavior, Sense

pp = pprint.PrettyPrinter(indent=4)


with nidaqmx.Task() as task:
    # Channel Settings
    voltage_setpoint = 0
    current_setpoint = 0.03
    output_enable = True
    idle_output_behavior = PowerIdleOutputBehavior.OUTPUT_DISABLED
    remote_sense = Sense.LOCAL

    chan = task.ai_channels.add_ai_power_chan(
        "TS1Mod1/power", voltage_setpoint, current_setpoint, output_enable
    )
    chan.pwr_idle_output_behavior = idle_output_behavior
    chan.pwr_remote_sense = remote_sense

    task.start()

    try:
        print("Press Ctrl+C to stop")
        while True:
            # Note: at runtime, you can write the following channel attributes:
            # * pwr_voltage_setpoint
            # * pwr_current_setpoint
            # * pwr_output_enable

            data = task.read()

            print(f"Data:")
            pp.pprint(data)

            print(f"output state: {chan.pwr_output_state}")
            if task.in_stream.overtemperature_chans_exist:
                print(f"overtemperature chans: {task.in_stream.overtemperature_chans}")

            time.sleep(1)
    except KeyboardInterrupt:
        pass

    task.stop()
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=examples/synchronization/multi_function/ai_ao_sync.py sha256=934ea458704e14beb7522e51d1a37fdb52f4c1ed3df858d15ab40c8e8c657c57 bytes=3900 -->
## FILE: examples/synchronization/multi_function/ai_ao_sync.py

- repository: `ni/nidaqmx-python`
- source_path: `examples/synchronization/multi_function/ai_ao_sync.py`
- sha256: `934ea458704e14beb7522e51d1a37fdb52f4c1ed3df858d15ab40c8e8c657c57`
- bytes: 3900

````python
"""Example of analog input and output synchronization.

This example demonstrates how to continuously acquire and
generate data at the same time, synchronized with one another.
"""

import numpy as np
import numpy.typing

import nidaqmx
from nidaqmx.constants import AcquisitionType, ProductCategory


def get_terminal_name_with_dev_prefix(task: nidaqmx.Task, terminal_name: str) -> str:
    """Gets the terminal name with the device prefix.

    Args:
        task: Specifies the task to get the device name from.
        terminal_name: Specifies the terminal name to get.

    Returns:
        Indicates the terminal name with the device prefix.
    """
    for device in task.devices:
        if device.product_category not in [
            ProductCategory.C_SERIES_MODULE,
            ProductCategory.SCXI_MODULE,
        ]:
            return f"/{device.name}/{terminal_name}"

    raise RuntimeError("Suitable device not found in task.")


def generate_sine_wave(
    frequency: float,
    amplitude: float,
    sampling_rate: float,
    number_of_samples: int,
    phase_in: float = 0.0,
) -> tuple[numpy.typing.NDArray[numpy.double], float]:
    """Generates a sine wave with a specified phase.

    Args:
        frequency: Specifies the frequency of the sine wave.
        amplitude: Specifies the amplitude of the sine wave.
        sampling_rate: Specifies the sampling rate of the sine wave.
        number_of_samples: Specifies the number of samples to generate.
        phase_in: Specifies the phase of the sine wave in radians.

    Returns:
        Indicates a tuple containing the generated data and the phase
        of the sine wave after generation.
    """
    duration_time = number_of_samples / sampling_rate
    duration_radians = duration_time * 2 * np.pi
    phase_out = (phase_in + duration_radians) % (2 * np.pi)
    t = np.linspace(phase_in, phase_in + duration_radians, number_of_samples, endpoint=False)

    return (amplitude * np.sin(frequency * t), phase_out)


def main():
    """Continuously acquires and generate data at the same time."""
    total_read = 0
    number_of_samples = 1000

    with nidaqmx.Task() as ai_task, nidaqmx.Task() as ao_task:

        def callback(task_handle, every_n_samples_event_type, number_of_samples, callback_data):
            """Callback function for reading signals."""
            nonlocal total_read
            read = ai_task.read(number_of_samples_per_channel=number_of_samples)
            total_read += len(read)
            print(f"Acquired data: {len(read)} samples. Total {total_read}.", end="\r")

            return 0

        ai_task.ai_channels.add_ai_voltage_chan("Dev1/ai0")
        ai_task.timing.cfg_samp_clk_timing(1000.0, sample_mode=AcquisitionType.CONTINUOUS)
        ai_task.register_every_n_samples_acquired_into_buffer_event(1000, callback)
        terminal_name = get_terminal_name_with_dev_prefix(ai_task, "ai/StartTrigger")

        ao_task.ao_channels.add_ao_voltage_chan("Dev1/ao0")
        ao_task.timing.cfg_samp_clk_timing(1000.0, sample_mode=AcquisitionType.CONTINUOUS)
        ao_task.triggers.start_trigger.cfg_dig_edge_start_trig(terminal_name)

        actual_sampling_rate = ao_task.timing.samp_clk_rate
        print(f"Actual sampling rate: {actual_sampling_rate:g} S/s")

        ao_data, _ = generate_sine_wave(
            frequency=10.0,
            amplitude=1.0,
            sampling_rate=actual_sampling_rate,
            number_of_samples=number_of_samples,
        )

        ao_task.write(ao_data)
        ao_task.start()
        ai_task.start()

        input("Acquiring samples continuously. Press Enter to stop.\n")

        ai_task.stop()
        ao_task.stop()

        print(f"\nAcquired {total_read} total samples.")


if __name__ == "__main__":
    main()
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=examples/synchronization/multi_function/cont_ai_ci_tdms_sync.py sha256=31a3b591b670a41176eaa3117730cd471dcb0f86ad9a0003e0f87ca1a15f8d5e bytes=8771 -->
## FILE: examples/synchronization/multi_function/cont_ai_ci_tdms_sync.py

- repository: `ni/nidaqmx-python`
- source_path: `examples/synchronization/multi_function/cont_ai_ci_tdms_sync.py`
- sha256: `31a3b591b670a41176eaa3117730cd471dcb0f86ad9a0003e0f87ca1a15f8d5e`
- bytes: 8771

````python
"""Example of logging multiple synchronized tasks to a single TDMS file using a queue.

This example demonstrates how to:
1. Synchronize multiple DAQmx tasks using a shared clock
2. Use a producer-consumer pattern with a queue
3. Log data from multiple tasks to a single TDMS file
"""

from __future__ import annotations

import os
import queue
import threading
import time
from collections.abc import Sequence
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import numpy as np
from nitypes.waveform import AnalogWaveform
from nptdms import ChannelObject, GroupObject, RootObject, TdmsFile, TdmsWriter

import nidaqmx
from nidaqmx.constants import (
    AcquisitionType,
    Edge,
)
from nidaqmx.stream_readers import AnalogMultiChannelReader, CounterReader

# Configuration
SAMPLE_RATE = 1000
SAMPLES_PER_CHANNEL = 1000
TIMEOUT = 10.0
# Note: This example currently assumes all tasks run on a single synchronized device.
# To make this example work across multiple devices, share the sample clock
# between devices using the PXI trigger bus or a PFI line.
DEVICE_NAME = "Dev1"

TaskData = tuple[
    Sequence[AnalogWaveform[np.float64]],  # Analog input: sequence of waveforms
    AnalogWaveform[np.float64],  # Counter input: waveform
]

data_queue: queue.Queue[TaskData | None] = queue.Queue(maxsize=10)


def producer(
    tasks: Sequence[nidaqmx.Task],
    data_queue: queue.Queue[TaskData | None],
    stop_event: threading.Event,
) -> None:
    """Producer function that reads data from DAQmx tasks and puts it in the queue."""
    # The queue holds a tuple with task data:
    # (
    #   Sequence[AnalogWaveform],  # Element 0: AI data - sequence of waveform objects
    #   AnalogWaveform,            # Element 1: Counter data - single waveform object
    # )
    ai_reader = AnalogMultiChannelReader(tasks[0].in_stream)
    counter_reader = CounterReader(tasks[1].in_stream)

    num_ai_channels = len(tasks[0].ai_channels.all)

    try:
        while not stop_event.is_set():

            ai_waveforms = [
                AnalogWaveform(sample_count=SAMPLES_PER_CHANNEL) for _ in range(num_ai_channels)
            ]
            counter_waveform = AnalogWaveform(sample_count=SAMPLES_PER_CHANNEL)

            ai_reader.read_waveforms(
                ai_waveforms, number_of_samples_per_channel=SAMPLES_PER_CHANNEL, timeout=TIMEOUT
            )

            counter_reader.read_many_sample_double(
                counter_waveform.raw_data,
                number_of_samples_per_channel=SAMPLES_PER_CHANNEL,
                timeout=TIMEOUT,
            )
            counter_waveform.timing = ai_waveforms[0].timing
            counter_waveform.channel_name = tasks[1].channel_names[0]

            data_queue.put((ai_waveforms, counter_waveform))

    except Exception as e:
        print(f"Error in producer: {e}")
        stop_event.set()
    finally:
        data_queue.put(None)


def consumer(
    data_queue: queue.Queue[TaskData | None],
    tdms_path: str,
    group_names: Sequence[str],
    channel_names: Sequence[Sequence[str]],
    stop_event: threading.Event,
) -> None:
    """Consumer function that writes data from the queue to a TDMS file."""
    with TdmsWriter(tdms_path) as tdms_writer:
        while not stop_event.is_set():
            try:
                data = data_queue.get(timeout=TIMEOUT)

            except queue.Empty:
                continue

            if data is None:
                break

            ai_waveforms, counter_waveform = data

            sample_rate = 1.0 / ai_waveforms[0].timing.sample_interval.total_seconds()

            root_object = RootObject(
                properties={"Creation Time": time.strftime("%Y-%m-%d %H:%M:%S")}
            )

            objects_to_write = [root_object]

            ai_group = GroupObject("AI_Task", properties={"Sample Rate": sample_rate})
            objects_to_write.append(ai_group)

            for chan_idx, waveform in enumerate(ai_waveforms):

                channel = ChannelObject(
                    "AI_Task",
                    f"Channel{chan_idx + 1:02d}",
                    waveform.raw_data,
                    properties={
                        "Sample Rate": sample_rate,
                        "wf_increment": waveform.timing.sample_interval.total_seconds(),
                        "wf_samples": len(waveform.raw_data),
                        "wf_start_offset": 0.0,
                        "wf_start_time": waveform.timing.to_datetime().start_time.strftime(
                            "%Y-%m-%d %H:%M:%S"
                        ),
                    },
                )
                objects_to_write.append(channel)

            ci_group = GroupObject("CI_Task", properties={"Sample Rate": sample_rate})
            objects_to_write.append(ci_group)

            channel = ChannelObject(
                "CI_Task",
                "Counter0",
                counter_waveform.raw_data,
                properties={
                    "Sample Rate": sample_rate,
                    "wf_increment": counter_waveform.timing.sample_interval.total_seconds(),
                    "wf_samples": len(counter_waveform.raw_data),
                    "wf_start_offset": 0.0,
                    "wf_start_time": counter_waveform.timing.to_datetime().start_time.strftime(
                        "%Y-%m-%d %H:%M:%S"
                    ),
                },
            )
            objects_to_write.append(channel)

            # Write all objects to TDMS file
            tdms_writer.write_segment(objects_to_write)


def main():
    """Run the synchronized data acquisition and logging example.

    Creates multiple synchronized DAQmx tasks:
    - A counter output task for the sample clock
    - An analog input task reading from two voltage channels
    - A counter input task counting edges

    Data is acquired continuously until user presses Enter, then saved to a TDMS file
    using a producer-consumer pattern with a queue for thread-safe data transfer.
    """
    data_queue: queue.Queue[TaskData | None] = queue.Queue(maxsize=10)
    stop_event = threading.Event()

    ai_task = nidaqmx.Task()
    ci_task = nidaqmx.Task()

    script_dir = Path(__file__).resolve().parent
    tdms_filepath = script_dir / "multi_task_data.tdms"

    try:

        ai_task.ai_channels.add_ai_voltage_chan(f"{DEVICE_NAME}/ai0", "Channel01")
        ai_task.ai_channels.add_ai_voltage_chan(f"{DEVICE_NAME}/ai1", "Channel02")
        ai_task.timing.cfg_samp_clk_timing(
            SAMPLE_RATE, sample_mode=AcquisitionType.CONTINUOUS, samps_per_chan=SAMPLES_PER_CHANNEL
        )

        ci_chan = ci_task.ci_channels.add_ci_count_edges_chan(
            f"{DEVICE_NAME}/ctr0", "Counter0", edge=Edge.RISING, initial_count=0
        )
        ci_chan.ci_count_edges_term = f"{DEVICE_NAME}/PFI0"
        ci_task.timing.cfg_samp_clk_timing(
            SAMPLE_RATE,
            f"/{DEVICE_NAME}/ai/SampleClock",
            sample_mode=AcquisitionType.CONTINUOUS,
            samps_per_chan=SAMPLES_PER_CHANNEL,
        )

        #  Start the Analog task last since the Counter task is using its clock
        ci_task.start()
        ai_task.start()

        with ThreadPoolExecutor(max_workers=2) as executor:
            producer_future = executor.submit(producer, [ai_task, ci_task], data_queue, stop_event)
            consumer_future = executor.submit(
                consumer,
                data_queue,
                str(tdms_filepath),
                ["AI_Task", "CI_Task"],
                [["Channel01", "Channel02"], ["Counter0"]],
                stop_event,
            )

            print("Acquiring and logging data. Press Enter to stop...")
            input()

            stop_event.set()

            producer_future.result()
            consumer_future.result()

    finally:
        for task in [ai_task, ci_task]:
            if task:
                task.stop()
                task.close()

    print("\nAcquisition complete. Data saved to multi_task_data.tdms")

    if os.path.exists("multi_task_data.tdms_index"):
        os.remove("multi_task_data.tdms_index")

    with TdmsFile.open(tdms_filepath) as tdms_file:
        for group in tdms_file.groups():
            print("Group:", group.name)
            for channel in group.channels():
                data = channel[:]
                print(f"\nFirst 10 samples from {group.name}/{channel.name}:")
                print(data[:10])


if __name__ == "__main__":
    main()
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=examples/synchronization/multi_function/cont_ai_di_acq.py sha256=29633f9ee1e4c4596bf3b791597edee0738204d32f098f14bccacb21d1acd118 bytes=2753 -->
## FILE: examples/synchronization/multi_function/cont_ai_di_acq.py

- repository: `ni/nidaqmx-python`
- source_path: `examples/synchronization/multi_function/cont_ai_di_acq.py`
- sha256: `29633f9ee1e4c4596bf3b791597edee0738204d32f098f14bccacb21d1acd118`
- bytes: 2753

````python
"""Example of analog and digital data acquisition at the same time.

This example demonstrates how to continuously acquire analog and
digital data at the same time, synchronized with one another on
the same device.
"""

import nidaqmx
from nidaqmx.constants import AcquisitionType, LineGrouping, ProductCategory


def get_terminal_name_with_dev_prefix(task: nidaqmx.Task, terminal_name: str) -> str:
    """Gets the terminal name with the device prefix.

    Args:
        task: Specifies the task to get the device name from.
        terminal_name: Specifies the terminal name to get.

    Returns:
        Indicates the terminal name with the device prefix.
    """
    for device in task.devices:
        if device.product_category not in [
            ProductCategory.C_SERIES_MODULE,
            ProductCategory.SCXI_MODULE,
        ]:
            return f"/{device.name}/{terminal_name}"

    raise RuntimeError("Suitable device not found in task.")


def main():
    """Continuously acquire analog and digital data at the same time."""
    total_ai_read = 0
    total_di_read = 0

    with nidaqmx.Task() as ai_task, nidaqmx.Task() as di_task:

        def callback(task_handle, every_n_samples_event_type, number_of_samples, callback_data):
            """Callback function for reading signals."""
            nonlocal total_ai_read
            nonlocal total_di_read
            ai_read = ai_task.read(number_of_samples_per_channel=number_of_samples)
            di_read = di_task.read(number_of_samples_per_channel=number_of_samples)
            total_ai_read += len(ai_read)
            total_di_read += len(di_read)
            print(f"\t{len(ai_read)}\t{len(di_read)}\t\t{total_ai_read}\t{total_di_read}", end="\r")

            return 0

        ai_task.ai_channels.add_ai_voltage_chan("Dev1/ai0")
        ai_task.timing.cfg_samp_clk_timing(1000.0, sample_mode=AcquisitionType.CONTINUOUS)
        ai_task.register_every_n_samples_acquired_into_buffer_event(1000, callback)
        terminal_name = get_terminal_name_with_dev_prefix(ai_task, "ai/SampleClock")

        di_task.di_channels.add_di_chan("Dev1/port0", line_grouping=LineGrouping.CHAN_FOR_ALL_LINES)
        di_task.timing.cfg_samp_clk_timing(
            1000.0, terminal_name, sample_mode=AcquisitionType.CONTINUOUS
        )

        di_task.start()
        ai_task.start()

        print("Acquiring samples continuously. Press Enter to stop.\n")
        print("Read:\tAI\tDI\tTotal:\tAI\tDI")
        input()

        ai_task.stop()
        di_task.stop()

        print(f"\nAcquired {total_ai_read} total AI samples and {total_di_read} total DI samples.")


if __name__ == "__main__":
    main()
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=examples/system_properties.py sha256=befeeca70eec00ab3e5a0f7e0e8b1a0d61a269f820736b402765ad71e98708db bytes=556 -->
## FILE: examples/system_properties.py

- repository: `ni/nidaqmx-python`
- source_path: `examples/system_properties.py`
- sha256: `befeeca70eec00ab3e5a0f7e0e8b1a0d61a269f820736b402765ad71e98708db`
- bytes: 556

````python
"""Examples for using system properties in DAQmx."""

import nidaqmx.system

local_system = nidaqmx.system.System.local()
driver_version = local_system.driver_version

print(
    "DAQmx {}.{}.{}".format(
        driver_version.major_version,
        driver_version.minor_version,
        driver_version.update_version,
    )
)

for device in local_system.devices:
    print(
        "Device Name: {}, Product Category: {}, Product Type: {}".format(
            device.name, device.product_category, device.product_type
        )
    )
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=generated/nidaqmx/__init__.py sha256=78d20b68146d3c4f1015e88ff2cf90ff090ef94c45654f945d9e438215b66081 bytes=909 -->
## FILE: generated/nidaqmx/__init__.py

- repository: `ni/nidaqmx-python`
- source_path: `generated/nidaqmx/__init__.py`
- sha256: `78d20b68146d3c4f1015e88ff2cf90ff090ef94c45654f945d9e438215b66081`
- bytes: 909

````python
"""The NI-DAQmx API for Python."""

from importlib.metadata import version

from nidaqmx.errors import (
    DaqError,
    DaqReadError,
    DaqResourceWarning,
    DaqWarning,
    DaqWriteError,
)
from nidaqmx.grpc_session_options import *  # noqa: F403 - 'from nidaqmx.grpc_session_options import *' used; unable to detect undefined names (auto-generated noqa)
from nidaqmx.scale import Scale
from nidaqmx.task import Task
from nidaqmx.types import CtrFreq, CtrTick, CtrTime

__version__ = version(__name__)

__all__ = [  # noqa: F405 - 'errors' may be undefined, or defined from star imports: nidaqmx.grpc_session_options (auto-generated noqa)
    "errors",
    "scale",
    "stream_readers",
    "stream_writers",
    "task",
]

# Do not add a null logging handler. If the application has not configured logging, the
# default behavior is to log warnings and errors to stderr.
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=generated/nidaqmx/__main__.py sha256=d505bb4d4c32c9bdfb171e1b5483d889cd0770311f1330e8bd0d411873f997e7 bytes=1021 -->
## FILE: generated/nidaqmx/__main__.py

- repository: `ni/nidaqmx-python`
- source_path: `generated/nidaqmx/__main__.py`
- sha256: `d505bb4d4c32c9bdfb171e1b5483d889cd0770311f1330e8bd0d411873f997e7`
- bytes: 1021

````python
"""'nidaqmx' command line utility."""

from __future__ import annotations

import logging

import click

from nidaqmx import _install_daqmx


@click.group("nidaqmx")
@click.option(
    "-v",
    "--verbose",
    "verbosity",
    count=True,
    help="Enable verbose logging. Repeat to increase verbosity.",
)
def main(  # noqa: D103 - Missing docstring in public function (auto-generated noqa)
    verbosity: int,
) -> None:
    _configure_logging(verbosity)


@main.command()
def installdriver():  # noqa: D103 - Missing docstring in public function (auto-generated noqa)
    _install_daqmx.installdriver()


def _configure_logging(verbosity: int) -> None:
    """Configure logging for this process."""
    if verbosity > 1:
        level = logging.DEBUG
    elif verbosity == 1:
        level = logging.INFO
    else:
        level = logging.WARNING
    logging.basicConfig(format="%(asctime)s %(levelname)s: %(message)s", level=level)


if __name__ == "__main__":
    main()
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=generated/nidaqmx/_base_interpreter.py sha256=3252c09e40761edfa0dcac2b7a90b1841304ecc997bec8cc6e623d2146d2d2eb bytes=68689 -->
## FILE: generated/nidaqmx/_base_interpreter.py

- repository: `ni/nidaqmx-python`
- source_path: `generated/nidaqmx/_base_interpreter.py`
- sha256: `3252c09e40761edfa0dcac2b7a90b1841304ecc997bec8cc6e623d2146d2d2eb`
- bytes: 68689

````python
# Do not edit this file; it was automatically generated.
from __future__ import annotations

import abc
import numpy
from nitypes.waveform import AnalogWaveform, DigitalWaveform
from typing import Any

from collections.abc import Sequence
from nidaqmx.constants import WaveformAttributeMode


class BaseEventHandler(abc.ABC):
    """Interpreter-specific object that is returned from register_*_event()."""
    __slots__ = ()

    @abc.abstractmethod
    def close(self) -> None:
        """Release resources used by the event handler.

        After releasing the resources, this method may report handler-specific errors
        (e.g. gRPC stream errors) by raising an exception.
        """
        raise NotImplementedError


class BaseInterpreter(abc.ABC):
    """
    Contains signature of functions for all DAQmx APIs.
    """
    __slots__ = ()

    @abc.abstractmethod
    def add_cdaq_sync_connection(self, port_list):
        raise NotImplementedError

    @abc.abstractmethod
    def add_global_chans_to_task(self, task, channel_names):
        raise NotImplementedError

    @abc.abstractmethod
    def add_network_device(
            self, ip_address, device_name, attempt_reservation, timeout):
        raise NotImplementedError

    @abc.abstractmethod
    def are_configured_cdaq_sync_ports_disconnected(
            self, chassis_devices_ports, timeout):
        raise NotImplementedError

    @abc.abstractmethod
    def auto_configure_cdaq_sync_connections(
            self, chassis_devices_ports, timeout):
        raise NotImplementedError

    @abc.abstractmethod
    def calculate_reverse_poly_coeff(
            self, forward_coeffs, min_val_x, max_val_x, num_points_to_compute,
            reverse_poly_order):
        raise NotImplementedError

    @abc.abstractmethod
    def cfg_anlg_edge_ref_trig(
            self, task, trigger_source, pretrigger_samples, trigger_slope,
            trigger_level):
        raise NotImplementedError

    @abc.abstractmethod
    def cfg_anlg_edge_start_trig(
            self, task, trigger_source, trigger_slope, trigger_level):
        raise NotImplementedError

    @abc.abstractmethod
    def cfg_anlg_multi_edge_ref_trig(
            self, task, trigger_sources, pretrigger_samples,
            trigger_slope_array, trigger_level_array):
        raise NotImplementedError

    @abc.abstractmethod
    def cfg_anlg_multi_edge_start_trig(
            self, task, trigger_sources, trigger_slope_array,
            trigger_level_array):
        raise NotImplementedError

    @abc.abstractmethod
    def cfg_anlg_window_ref_trig(
            self, task, trigger_source, window_top, window_bottom,
            pretrigger_samples, trigger_when):
        raise NotImplementedError

    @abc.abstractmethod
    def cfg_anlg_window_start_trig(
            self, task, window_top, window_bottom, trigger_source,
            trigger_when):
        raise NotImplementedError

    @abc.abstractmethod
    def cfg_burst_handshaking_timing_export_clock(
            self, task, sample_clk_rate, sample_clk_outp_term, sample_mode,
            samps_per_chan, sample_clk_pulse_polarity, pause_when,
            ready_event_active_level):
        raise NotImplementedError

    @abc.abstractmethod
    def cfg_burst_handshaking_timing_import_clock(
            self, task, sample_clk_rate, sample_clk_src, sample_mode,
            samps_per_chan, sample_clk_active_edge, pause_when,
            ready_event_active_level):
        raise NotImplementedError

    @abc.abstractmethod
    def cfg_change_detection_timing(
            self, task, rising_edge_chan, falling_edge_chan, sample_mode,
            samps_per_chan):
        raise NotImplementedError

    @abc.abstractmethod
    def cfg_dig_edge_ref_trig(
            self, task, trigger_source, pretrigger_samples, trigger_edge):
        raise NotImplementedError

    @abc.abstractmethod
    def cfg_dig_edge_start_trig(self, task, trigger_source, trigger_edge):
        raise NotImplementedError

    @abc.abstractmethod
    def cfg_dig_pattern_ref_trig(
            self, task, trigger_source, trigger_pattern, pretrigger_samples,
            trigger_when):
        raise NotImplementedError

    @abc.abstractmethod
    def cfg_dig_pattern_start_trig(
            self, task, trigger_source, trigger_pattern, trigger_when):
        raise NotImplementedError

    @abc.abstractmethod
    def cfg_handshaking_timing(self, task, sample_mode, samps_per_chan):
        raise NotImplementedError

    @abc.abstractmethod
    def cfg_implicit_timing(self, task, sample_mode, samps_per_chan):
        raise NotImplementedError

    @abc.abstractmethod
    def cfg_pipelined_samp_clk_timing(
            self, task, rate, source, active_edge, sample_mode,
            samps_per_chan):
        raise NotImplementedError

    @abc.abstractmethod
    def cfg_samp_clk_timing(
            self, task, rate, source, active_edge, sample_mode,
            samps_per_chan):
        raise NotImplementedError

    @abc.abstractmethod
    def cfg_time_start_trig(self, task, when, timescale):
        raise NotImplementedError

    @abc.abstractmethod
    def cfg_watchdog_ao_expir_states(
            self, task, channel_names, expir_state_array, output_type_array):
        raise NotImplementedError

    @abc.abstractmethod
    def cfg_watchdog_co_expir_states(
            self, task, channel_names, expir_state_array):
        raise NotImplementedError

    @abc.abstractmethod
    def cfg_watchdog_do_expir_states(
            self, task, channel_names, expir_state_array):
        raise NotImplementedError

    @abc.abstractmethod
    def clear_task(self, task):
        raise NotImplementedError

    @abc.abstractmethod
    def clear_teds(self, physical_channel):
        raise NotImplementedError

    @abc.abstractmethod
    def configure_logging(
            self, task, file_path, logging_mode, group_name, operation):
        raise NotImplementedError

    @abc.abstractmethod
    def configure_teds(self, physical_channel, file_path):
        raise NotImplementedError

    @abc.abstractmethod
    def connect_terms(
            self, source_terminal, destination_terminal, signal_modifiers):
        raise NotImplementedError

    @abc.abstractmethod
    def control_watchdog_task(self, task, action):
        raise NotImplementedError

    @abc.abstractmethod
    def create_ai_accel4_wire_dc_voltage_chan(
            self, task, physical_channel, name_to_assign_to_channel,
            terminal_config, min_val, max_val, units, sensitivity,
            sensitivity_units, voltage_excit_source, voltage_excit_val,
            use_excit_for_scaling, custom_scale_name):
        raise NotImplementedError

    @abc.abstractmethod
    def create_ai_accel_chan(
            self, task, physical_channel, name_to_assign_to_channel,
            terminal_config, min_val, max_val, units, sensitivity,
            sensitivity_units, current_excit_source, current_excit_val,
            custom_scale_name):
        raise NotImplementedError

    @abc.abstractmethod
    def create_ai_accel_charge_chan(
            self, task, physical_channel, name_to_assign_to_channel,
            terminal_config, min_val, max_val, units, sensitivity,
            sensitivity_units, custom_scale_name):
        raise NotImplementedError

    @abc.abstractmethod
    def create_ai_bridge_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, bridge_config, voltage_excit_source,
            voltage_excit_val, nominal_bridge_resistance, custom_scale_name):
        raise NotImplementedError

    @abc.abstractmethod
    def create_ai_calculated_power_chan(
            self, task, voltage_physical_channel, current_physical_channel,
            name_to_assign_to_channel, terminal_config, voltage_min_val,
            voltage_max_val, current_min_val, current_max_val, units,
            shunt_resistor_loc, ext_shunt_resistor_val, custom_scale_name):
        raise NotImplementedError

    @abc.abstractmethod
    def create_ai_charge_chan(
            self, task, physical_channel, name_to_assign_to_channel,
            terminal_config, min_val, max_val, units, custom_scale_name):
        raise NotImplementedError

    @abc.abstractmethod
    def create_ai_current_chan(
            self, task, physical_channel, name_to_assign_to_channel,
            terminal_config, min_val, max_val, units, shunt_resistor_loc,
            ext_shunt_resistor_val, custom_scale_name):
        raise NotImplementedError

    @abc.abstractmethod
    def create_ai_current_rms_chan(
            self, task, physical_channel, name_to_assign_to_channel,
            terminal_config, min_val, max_val, units, shunt_resistor_loc,
            ext_shunt_resistor_val, custom_scale_name):
        raise NotImplementedError

    @abc.abstractmethod
    def create_ai_force_bridge_polynomial_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, bridge_config, voltage_excit_source,
            voltage_excit_val, nominal_bridge_resistance, forward_coeffs,
            reverse_coeffs, electrical_units, physical_units,
            custom_scale_name):
        raise NotImplementedError

    @abc.abstractmethod
    def create_ai_force_bridge_table_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, bridge_config, voltage_excit_source,
            voltage_excit_val, nominal_bridge_resistance, electrical_vals,
            electrical_units, physical_vals, physical_units,
            custom_scale_name):
        raise NotImplementedError

    @abc.abstractmethod
    def create_ai_force_bridge_two_point_lin_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, bridge_config, voltage_excit_source,
            voltage_excit_val, nominal_bridge_resistance,
            first_electrical_val, second_electrical_val, electrical_units,
            first_physical_val, second_physical_val, physical_units,
            custom_scale_name):
        raise NotImplementedError

    @abc.abstractmethod
    def create_ai_force_iepe_chan(
            self, task, physical_channel, name_to_assign_to_channel,
            terminal_config, min_val, max_val, units, sensitivity,
            sensitivity_units, current_excit_source, current_excit_val,
            custom_scale_name):
        raise NotImplementedError

    @abc.abstractmethod
    def create_ai_freq_voltage_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, threshold_level, hysteresis, custom_scale_name):
        raise NotImplementedError

    @abc.abstractmethod
    def create_ai_microphone_chan(
            self, task, physical_channel, name_to_assign_to_channel,
            terminal_config, units, mic_sensitivity, max_snd_press_level,
            current_excit_source, current_excit_val, custom_scale_name):
        raise NotImplementedError

    @abc.abstractmethod
    def create_ai_pos_eddy_curr_prox_probe_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, sensitivity, sensitivity_units,
            custom_scale_name):
        raise NotImplementedError

    @abc.abstractmethod
    def create_ai_pos_lvdt_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, sensitivity, sensitivity_units,
            voltage_excit_source, voltage_excit_val, voltage_excit_freq,
            ac_excit_wire_mode, custom_scale_name):
        raise NotImplementedError

    @abc.abstractmethod
    def create_ai_pos_rvdt_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, sensitivity, sensitivity_units,
            voltage_excit_source, voltage_excit_val, voltage_excit_freq,
            ac_excit_wire_mode, custom_scale_name):
        raise NotImplementedError

    @abc.abstractmethod
    def create_ai_power_chan(
            self, task, physical_channel, voltage_setpoint, current_setpoint,
            output_enable, name_to_assign_to_channel):
        raise NotImplementedError

    @abc.abstractmethod
    def create_ai_pressure_bridge_polynomial_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, bridge_config, voltage_excit_source,
            voltage_excit_val, nominal_bridge_resistance, forward_coeffs,
            reverse_coeffs, electrical_units, physical_units,
            custom_scale_name):
        raise NotImplementedError

    @abc.abstractmethod
    def create_ai_pressure_bridge_table_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, bridge_config, voltage_excit_source,
            voltage_excit_val, nominal_bridge_resistance, electrical_vals,
            electrical_units, physical_vals, physical_units,
            custom_scale_name):
        raise NotImplementedError

    @abc.abstractmethod
    def create_ai_pressure_bridge_two_point_lin_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, bridge_config, voltage_excit_source,
            voltage_excit_val, nominal_bridge_resistance,
            first_electrical_val, second_electrical_val, electrical_units,
            first_physical_val, second_physical_val, physical_units,
            custom_scale_name):
        raise NotImplementedError

    @abc.abstractmethod
    def create_ai_resistance_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, resistance_config, current_excit_source,
            current_excit_val, custom_scale_name):
        raise NotImplementedError

    @abc.abstractmethod
    def create_ai_rosette_strain_gage_chan(
            self, task, physical_channel, rosette_type, gage_orientation,
            rosette_meas_types, name_to_assign_to_channel, min_val, max_val,
            strain_config, voltage_excit_source, voltage_excit_val,
            gage_factor, nominal_gage_resistance, poisson_ratio,
            lead_wire_resistance):
        raise NotImplementedError

    @abc.abstractmethod
    def create_ai_strain_gage_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, strain_config, voltage_excit_source,
            voltage_excit_val, gage_factor, initial_bridge_voltage,
            nominal_gage_resistance, poisson_ratio, lead_wire_resistance,
            custom_scale_name):
        raise NotImplementedError

    @abc.abstractmethod
    def create_ai_temp_built_in_sensor_chan(
            self, task, physical_channel, name_to_assign_to_channel, units):
        raise NotImplementedError

    @abc.abstractmethod
    def create_ai_thrmcpl_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, thermocouple_type, cjc_source, cjc_val,
            cjc_channel):
        raise NotImplementedError

    @abc.abstractmethod
    def create_ai_thrmstr_chan_iex(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, resistance_config, current_excit_source,
            current_excit_val, a, b, c):
        raise NotImplementedError

    @abc.abstractmethod
    def create_ai_thrmstr_chan_vex(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, resistance_config, voltage_excit_source,
            voltage_excit_val, a, b, c, r_1):
        raise NotImplementedError

    @abc.abstractmethod
    def create_ai_torque_bridge_polynomial_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, bridge_config, voltage_excit_source,
            voltage_excit_val, nominal_bridge_resistance, forward_coeffs,
            reverse_coeffs, electrical_units, physical_units,
            custom_scale_name):
        raise NotImplementedError

    @abc.abstractmethod
    def create_ai_torque_bridge_table_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, bridge_config, voltage_excit_source,
            voltage_excit_val, nominal_bridge_resistance, electrical_vals,
            electrical_units, physical_vals, physical_units,
            custom_scale_name):
        raise NotImplementedError

    @abc.abstractmethod
    def create_ai_torque_bridge_two_point_lin_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, bridge_config, voltage_excit_source,
            voltage_excit_val, nominal_bridge_resistance,
            first_electrical_val, second_electrical_val, electrical_units,
            first_physical_val, second_physical_val, physical_units,
            custom_scale_name):
        raise NotImplementedError

    @abc.abstractmethod
    def create_ai_velocity_iepe_chan(
            self, task, physical_channel, name_to_assign_to_channel,
            terminal_config, min_val, max_val, units, sensitivity,
            sensitivity_units, current_excit_source, current_excit_val,
            custom_scale_name):
        raise NotImplementedError

    @abc.abstractmethod
    def create_ai_voltage_chan(
            self, task, physical_channel, name_to_assign_to_channel,
            terminal_config, min_val, max_val, units, custom_scale_name):
        raise NotImplementedError

    @abc.abstractmethod
    def create_ai_voltage_chan_with_excit(
            self, task, physical_channel, name_to_assign_to_channel,
            terminal_config, min_val, max_val, units, bridge_config,
            voltage_excit_source, voltage_excit_val, use_excit_for_scaling,
            custom_scale_name):
        raise NotImplementedError

    @abc.abstractmethod
    def create_ai_voltage_rms_chan(
            self, task, physical_channel, name_to_assign_to_channel,
            terminal_config, min_val, max_val, units, custom_scale_name):
        raise NotImplementedError

    @abc.abstractmethod
    def create_airtd_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, rtd_type, resistance_config, current_excit_source,
            current_excit_val, r_0):
        raise NotImplementedError

    @abc.abstractmethod
    def create_ao_current_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, custom_scale_name):
        raise NotImplementedError

    @abc.abstractmethod
    def create_ao_func_gen_chan(
            self, task, physical_channel, name_to_assign_to_channel, type,
            freq, amplitude, offset):
        raise NotImplementedError

    @abc.abstractmethod
    def create_ao_voltage_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, custom_scale_name):
        raise NotImplementedError

    @abc.abstractmethod
    def create_ci_ang_encoder_chan(
            self, task, counter, name_to_assign_to_channel, decoding_type,
            zidx_enable, zidx_val, zidx_phase, units, pulses_per_rev,
            initial_angle, custom_scale_name):
        raise NotImplementedError

    @abc.abstractmethod
    def create_ci_ang_velocity_chan(
            self, task, counter, name_to_assign_to_channel, min_val, max_val,
            decoding_type, units, pulses_per_rev, custom_scale_name):
        raise NotImplementedError

    @abc.abstractmethod
    def create_ci_count_edges_chan(
            self, task, counter, name_to_assign_to_channel, edge,
            initial_count, count_direction):
        raise NotImplementedError

    @abc.abstractmethod
    def create_ci_duty_cycle_chan(
            self, task, counter, name_to_assign_to_channel, min_freq,
            max_freq, edge, custom_scale_name):
        raise NotImplementedError

    @abc.abstractmethod
    def create_ci_freq_chan(
            self, task, counter, name_to_assign_to_channel, min_val, max_val,
            units, edge, meas_method, meas_time, divisor, custom_scale_name):
        raise NotImplementedError

    @abc.abstractmethod
    def create_ci_lin_encoder_chan(
            self, task, counter, name_to_assign_to_channel, decoding_type,
            zidx_enable, zidx_val, zidx_phase, units, dist_per_pulse,
            initial_pos, custom_scale_name):
        raise NotImplementedError

    @abc.abstractmethod
    def create_ci_lin_velocity_chan(
            self, task, counter, name_to_assign_to_channel, min_val, max_val,
            decoding_type, units, dist_per_pulse, custom_scale_name):
        raise NotImplementedError

    @abc.abstractmethod
    def create_ci_period_chan(
            self, task, counter, name_to_assign_to_channel, min_val, max_val,
            units, edge, meas_method, meas_time, divisor, custom_scale_name):
        raise NotImplementedError

    @abc.abstractmethod
    def create_ci_pulse_chan_freq(
            self, task, counter, name_to_assign_to_channel, min_val, max_val,
            units):
        raise NotImplementedError

    @abc.abstractmethod
    def create_ci_pulse_chan_ticks(
            self, task, counter, name_to_assign_to_channel, source_terminal,
            min_val, max_val):
        raise NotImplementedError

    @abc.abstractmethod
    def create_ci_pulse_chan_time(
            self, task, counter, name_to_assign_to_channel, min_val, max_val,
            units):
        raise NotImplementedError

    @abc.abstractmethod
    def create_ci_pulse_width_chan(
            self, task, counter, name_to_assign_to_channel, min_val, max_val,
            units, starting_edge, custom_scale_name):
        raise NotImplementedError

    @abc.abstractmethod
    def create_ci_semi_period_chan(
            self, task, counter, name_to_assign_to_channel, min_val, max_val,
            units, custom_scale_name):
        raise NotImplementedError

    @abc.abstractmethod
    def create_ci_two_edge_sep_chan(
            self, task, counter, name_to_assign_to_channel, min_val, max_val,
            units, first_edge, second_edge, custom_scale_name):
        raise NotImplementedError

    @abc.abstractmethod
    def create_cigps_timestamp_chan(
            self, task, counter, name_to_assign_to_channel, units,
            sync_method, custom_scale_name):
        raise NotImplementedError

    @abc.abstractmethod
    def create_co_pulse_chan_freq(
            self, task, counter, name_to_assign_to_channel, units, idle_state,
            initial_delay, freq, duty_cycle):
        raise NotImplementedError

    @abc.abstractmethod
    def create_co_pulse_chan_ticks(
            self, task, counter, source_terminal, name_to_assign_to_channel,
            idle_state, initial_delay, low_ticks, high_ticks):
        raise NotImplementedError

    @abc.abstractmethod
    def create_co_pulse_chan_time(
            self, task, counter, name_to_assign_to_channel, units, idle_state,
            initial_delay, low_time, high_time):
        raise NotImplementedError

    @abc.abstractmethod
    def create_di_chan(
            self, task, lines, name_to_assign_to_lines, line_grouping):
        raise NotImplementedError

    @abc.abstractmethod
    def create_do_chan(
            self, task, lines, name_to_assign_to_lines, line_grouping):
        raise NotImplementedError

    @abc.abstractmethod
    def create_lin_scale(
            self, name, slope, y_intercept, pre_scaled_units, scaled_units):
        raise NotImplementedError

    @abc.abstractmethod
    def create_map_scale(
            self, name, prescaled_min, prescaled_max, scaled_min, scaled_max,
            pre_scaled_units, scaled_units):
        raise NotImplementedError

    @abc.abstractmethod
    def create_polynomial_scale(
            self, name, forward_coeffs, reverse_coeffs, pre_scaled_units,
            scaled_units):
        raise NotImplementedError

    @abc.abstractmethod
    def create_table_scale(
            self, name, prescaled_vals, scaled_vals, pre_scaled_units,
            scaled_units):
        raise NotImplementedError

    @abc.abstractmethod
    def create_task(self, session_name):
        raise NotImplementedError

    @abc.abstractmethod
    def create_tedsai_accel_chan(
            self, task, physical_channel, name_to_assign_to_channel,
            terminal_config, min_val, max_val, units, current_excit_source,
            current_excit_val, custom_scale_name):
        raise NotImplementedError

    @abc.abstractmethod
    def create_tedsai_bridge_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, voltage_excit_source, voltage_excit_val,
            custom_scale_name):
        raise NotImplementedError

    @abc.abstractmethod
    def create_tedsai_current_chan(
            self, task, physical_channel, name_to_assign_to_channel,
            terminal_config, min_val, max_val, units, shunt_resistor_loc,
            ext_shunt_resistor_val, custom_scale_name):
        raise NotImplementedError

    @abc.abstractmethod
    def create_tedsai_force_bridge_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, voltage_excit_source, voltage_excit_val,
            custom_scale_name):
        raise NotImplementedError

    @abc.abstractmethod
    def create_tedsai_force_iepe_chan(
            self, task, physical_channel, name_to_assign_to_channel,
            terminal_config, min_val, max_val, units, current_excit_source,
            current_excit_val, custom_scale_name):
        raise NotImplementedError

    @abc.abstractmethod
    def create_tedsai_microphone_chan(
            self, task, physical_channel, name_to_assign_to_channel,
            terminal_config, units, max_snd_press_level, current_excit_source,
            current_excit_val, custom_scale_name):
        raise NotImplementedError

    @abc.abstractmethod
    def create_tedsai_pos_lvdt_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, voltage_excit_source, voltage_excit_val,
            voltage_excit_freq, ac_excit_wire_mode, custom_scale_name):
        raise NotImplementedError

    @abc.abstractmethod
    def create_tedsai_pos_rvdt_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, voltage_excit_source, voltage_excit_val,
            voltage_excit_freq, ac_excit_wire_mode, custom_scale_name):
        raise NotImplementedError

    @abc.abstractmethod
    def create_tedsai_pressure_bridge_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, voltage_excit_source, voltage_excit_val,
            custom_scale_name):
        raise NotImplementedError

    @abc.abstractmethod
    def create_tedsai_resistance_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, resistance_config, current_excit_source,
            current_excit_val, custom_scale_name):
        raise NotImplementedError

    @abc.abstractmethod
    def create_tedsai_strain_gage_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, voltage_excit_source, voltage_excit_val,
            initial_bridge_voltage, lead_wire_resistance, custom_scale_name):
        raise NotImplementedError

    @abc.abstractmethod
    def create_tedsai_thrmcpl_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, cjc_source, cjc_val, cjc_channel):
        raise NotImplementedError

    @abc.abstractmethod
    def create_tedsai_thrmstr_chan_iex(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, resistance_config, current_excit_source,
            current_excit_val):
        raise NotImplementedError

    @abc.abstractmethod
    def create_tedsai_thrmstr_chan_vex(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, resistance_config, voltage_excit_source,
            voltage_excit_val, r_1):
        raise NotImplementedError

    @abc.abstractmethod
    def create_tedsai_torque_bridge_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, voltage_excit_source, voltage_excit_val,
            custom_scale_name):
        raise NotImplementedError

    @abc.abstractmethod
    def create_tedsai_voltage_chan(
            self, task, physical_channel, name_to_assign_to_channel,
            terminal_config, min_val, max_val, units, custom_scale_name):
        raise NotImplementedError

    @abc.abstractmethod
    def create_tedsai_voltage_chan_with_excit(
            self, task, physical_channel, name_to_assign_to_channel,
            terminal_config, min_val, max_val, units, voltage_excit_source,
            voltage_excit_val, custom_scale_name):
        raise NotImplementedError

    @abc.abstractmethod
    def create_tedsairtd_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, resistance_config, current_excit_source,
            current_excit_val):
        raise NotImplementedError

    @abc.abstractmethod
    def create_watchdog_timer_task_ex(
            self, device_name, session_name, timeout):
        raise NotImplementedError

    @abc.abstractmethod
    def delete_network_device(self, device_name):
        raise NotImplementedError

    @abc.abstractmethod
    def delete_saved_global_chan(self, channel_name):
        raise NotImplementedError

    @abc.abstractmethod
    def delete_saved_scale(self, scale_name):
        raise NotImplementedError

    @abc.abstractmethod
    def delete_saved_task(self, task_name):
        raise NotImplementedError

    @abc.abstractmethod
    def device_supports_cal(self, device_name):
        raise NotImplementedError

    @abc.abstractmethod
    def disable_ref_trig(self, task):
        raise NotImplementedError

    @abc.abstractmethod
    def disable_start_trig(self, task):
        raise NotImplementedError

    @abc.abstractmethod
    def disconnect_terms(self, source_terminal, destination_terminal):
        raise NotImplementedError

    @abc.abstractmethod
    def export_signal(self, task, signal_id, output_terminal):
        raise NotImplementedError

    @abc.abstractmethod
    def get_analog_power_up_states_with_output_type(
            self, channel_names, array_size):
        raise NotImplementedError

    @abc.abstractmethod
    def get_auto_configured_cdaq_sync_connections(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_buffer_attribute_uint32(self, task, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_cal_info_attribute_bool(self, device_name, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_cal_info_attribute_double(self, device_name, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_cal_info_attribute_string(self, device_name, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_cal_info_attribute_uint32(self, device_name, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_chan_attribute_bool(self, task, channel, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_chan_attribute_double(self, task, channel, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_chan_attribute_double_array(self, task, channel, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_chan_attribute_int32(self, task, channel, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_chan_attribute_string(self, task, channel, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_chan_attribute_uint32(self, task, channel, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_device_attribute_bool(self, device_name, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_device_attribute_double(self, device_name, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_device_attribute_double_array(self, device_name, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_device_attribute_int32(self, device_name, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_device_attribute_int32_array(self, device_name, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_device_attribute_string(self, device_name, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_device_attribute_uint32(self, device_name, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_device_attribute_uint32_array(self, device_name, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_digital_logic_family_power_up_state(self, device_name):
        raise NotImplementedError

    @abc.abstractmethod
    def get_digital_power_up_states(self, device_name, channel_name):
        raise NotImplementedError

    @abc.abstractmethod
    def get_digital_pull_up_pull_down_states(self, device_name, channel_name):
        raise NotImplementedError

    @abc.abstractmethod
    def get_disconnected_cdaq_sync_ports(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_error_string(self, error_code):
        raise NotImplementedError

    @abc.abstractmethod
    def get_exported_signal_attribute_bool(self, task, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_exported_signal_attribute_double(self, task, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_exported_signal_attribute_int32(self, task, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_exported_signal_attribute_string(self, task, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_exported_signal_attribute_uint32(self, task, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_ext_cal_last_date_and_time(self, device_name):
        raise NotImplementedError

    @abc.abstractmethod
    def get_persisted_chan_attribute_bool(self, channel, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_persisted_chan_attribute_string(self, channel, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_persisted_scale_attribute_bool(self, scale_name, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_persisted_scale_attribute_string(self, scale_name, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_persisted_task_attribute_bool(self, task_name, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_persisted_task_attribute_string(self, task_name, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_physical_chan_attribute_bool(self, physical_channel, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_physical_chan_attribute_bytes(self, physical_channel, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_physical_chan_attribute_double(self, physical_channel, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_physical_chan_attribute_double_array(
            self, physical_channel, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_physical_chan_attribute_int32(self, physical_channel, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_physical_chan_attribute_int32_array(
            self, physical_channel, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_physical_chan_attribute_string(self, physical_channel, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_physical_chan_attribute_uint32(self, physical_channel, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_physical_chan_attribute_uint32_array(
            self, physical_channel, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_read_attribute_bool(self, task, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_read_attribute_double(self, task, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_read_attribute_int32(self, task, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_read_attribute_string(self, task, attribute, size_hint=0):
        raise NotImplementedError

    @abc.abstractmethod
    def get_read_attribute_uint32(self, task, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_read_attribute_uint64(self, task, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_scale_attribute_double(self, scale_name, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_scale_attribute_double_array(self, scale_name, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_scale_attribute_int32(self, scale_name, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_scale_attribute_string(self, scale_name, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_self_cal_last_date_and_time(self, device_name):
        raise NotImplementedError

    @abc.abstractmethod
    def get_system_info_attribute_string(self, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_system_info_attribute_uint32(self, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_task_attribute_bool(self, task, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_task_attribute_string(self, task, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_task_attribute_uint32(self, task, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_timing_attribute_bool(self, task, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_timing_attribute_double(self, task, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_timing_attribute_ex_bool(self, task, device_names, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_timing_attribute_ex_double(self, task, device_names, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_timing_attribute_ex_int32(self, task, device_names, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_timing_attribute_ex_string(self, task, device_names, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_timing_attribute_ex_uint32(self, task, device_names, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_timing_attribute_ex_uint64(self, task, device_names, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_timing_attribute_int32(self, task, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_timing_attribute_string(self, task, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_timing_attribute_timestamp(self, task, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_timing_attribute_uint32(self, task, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_timing_attribute_uint64(self, task, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_trig_attribute_bool(self, task, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_trig_attribute_double(self, task, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_trig_attribute_double_array(self, task, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_trig_attribute_int32(self, task, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_trig_attribute_int32_array(self, task, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_trig_attribute_string(self, task, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_trig_attribute_timestamp(self, task, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_trig_attribute_uint32(self, task, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_watchdog_attribute_bool(self, task, lines, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_watchdog_attribute_double(self, task, lines, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_watchdog_attribute_int32(self, task, lines, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_watchdog_attribute_string(self, task, lines, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_write_attribute_bool(self, task, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_write_attribute_double(self, task, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_write_attribute_int32(self, task, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_write_attribute_string(self, task, attribute, size_hint=0):
        raise NotImplementedError

    @abc.abstractmethod
    def get_write_attribute_uint32(self, task, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def get_write_attribute_uint64(self, task, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def internal_get_last_created_chan(self):
        raise NotImplementedError

    @abc.abstractmethod
    def is_task_done(self, task):
        raise NotImplementedError

    @abc.abstractmethod
    def load_task(self, session_name):
        raise NotImplementedError

    @abc.abstractmethod
    def perform_bridge_offset_nulling_cal_ex(
            self, task, channel, skip_unsupported_channels):
        raise NotImplementedError

    @abc.abstractmethod
    def perform_bridge_shunt_cal_ex(
            self, task, channel, shunt_resistor_value,
            shunt_resistor_location, shunt_resistor_select,
            shunt_resistor_source, bridge_resistance,
            skip_unsupported_channels):
        raise NotImplementedError

    @abc.abstractmethod
    def perform_strain_shunt_cal_ex(
            self, task, channel, shunt_resistor_value,
            shunt_resistor_location, shunt_resistor_select,
            shunt_resistor_source, skip_unsupported_channels):
        raise NotImplementedError

    @abc.abstractmethod
    def perform_thrmcpl_lead_offset_nulling_cal(
            self, task, channel, skip_unsupported_channels):
        raise NotImplementedError

    @abc.abstractmethod
    def read_analog_f64(
            self, task, num_samps_per_chan, timeout, fill_mode, read_array):
        raise NotImplementedError

    @abc.abstractmethod
    def read_analog_scalar_f64(self, task, timeout):
        raise NotImplementedError

    @abc.abstractmethod
    def read_binary_i16(
            self, task, num_samps_per_chan, timeout, fill_mode, read_array):
        raise NotImplementedError

    @abc.abstractmethod
    def read_binary_i32(
            self, task, num_samps_per_chan, timeout, fill_mode, read_array):
        raise NotImplementedError

    @abc.abstractmethod
    def read_binary_u16(
            self, task, num_samps_per_chan, timeout, fill_mode, read_array):
        raise NotImplementedError

    @abc.abstractmethod
    def read_binary_u32(
            self, task, num_samps_per_chan, timeout, fill_mode, read_array):
        raise NotImplementedError

    @abc.abstractmethod
    def read_counter_f64(self, task, num_samps_per_chan, timeout, read_array):
        raise NotImplementedError

    @abc.abstractmethod
    def read_counter_f64_ex(
            self, task, num_samps_per_chan, timeout, fill_mode, read_array):
        raise NotImplementedError

    @abc.abstractmethod
    def read_counter_scalar_f64(self, task, timeout):
        raise NotImplementedError

    @abc.abstractmethod
    def read_counter_scalar_u32(self, task, timeout):
        raise NotImplementedError

    @abc.abstractmethod
    def read_counter_u32(self, task, num_samps_per_chan, timeout, read_array):
        raise NotImplementedError

    @abc.abstractmethod
    def read_counter_u32_ex(
            self, task, num_samps_per_chan, timeout, fill_mode, read_array):
        raise NotImplementedError

    @abc.abstractmethod
    def read_ctr_freq(
            self, task, num_samps_per_chan, timeout, interleaved,
            read_array_frequency, read_array_duty_cycle):
        raise NotImplementedError

    @abc.abstractmethod
    def read_ctr_freq_scalar(self, task, timeout):
        raise NotImplementedError

    @abc.abstractmethod
    def read_ctr_ticks(
            self, task, num_samps_per_chan, timeout, interleaved,
            read_array_high_ticks, read_array_low_ticks):
        raise NotImplementedError

    @abc.abstractmethod
    def read_ctr_ticks_scalar(self, task, timeout):
        raise NotImplementedError

    @abc.abstractmethod
    def read_ctr_time(
            self, task, num_samps_per_chan, timeout, interleaved,
            read_array_high_time, read_array_low_time):
        raise NotImplementedError

    @abc.abstractmethod
    def read_ctr_time_scalar(self, task, timeout):
        raise NotImplementedError

    @abc.abstractmethod
    def read_digital_lines(
            self, task, num_samps_per_chan, timeout, fill_mode, read_array):
        raise NotImplementedError

    @abc.abstractmethod
    def read_digital_scalar_u32(self, task, timeout):
        raise NotImplementedError

    @abc.abstractmethod
    def read_digital_u16(
            self, task, num_samps_per_chan, timeout, fill_mode, read_array):
        raise NotImplementedError

    @abc.abstractmethod
    def read_digital_u32(
            self, task, num_samps_per_chan, timeout, fill_mode, read_array):
        raise NotImplementedError

    @abc.abstractmethod
    def read_digital_u8(
            self, task, num_samps_per_chan, timeout, fill_mode, read_array):
        raise NotImplementedError

    @abc.abstractmethod
    def read_id_pin_memory(self, device_name, id_pin_name):
        raise NotImplementedError

    @abc.abstractmethod
    def read_power_binary_i16(
            self, task, num_samps_per_chan, timeout, fill_mode,
            read_array_voltage, read_array_current):
        raise NotImplementedError

    @abc.abstractmethod
    def read_power_f64(
            self, task, num_samps_per_chan, timeout, fill_mode,
            read_array_voltage, read_array_current):
        raise NotImplementedError

    @abc.abstractmethod
    def read_power_scalar_f64(self, task, timeout):
        raise NotImplementedError

    @abc.abstractmethod
    def read_raw(self, task, num_samps_per_chan, timeout, read_array):
        raise NotImplementedError

    @abc.abstractmethod
    def register_done_event(
            self, task, options, callback_function, callback_data):
        raise NotImplementedError

    @abc.abstractmethod
    def register_every_n_samples_event(
            self, task, every_n_samples_event_type, n_samples, options,
            callback_function, callback_data):
        raise NotImplementedError

    @abc.abstractmethod
    def register_signal_event(
            self, task, signal_id, options, callback_function, callback_data):
        raise NotImplementedError

    @abc.abstractmethod
    def remove_cdaq_sync_connection(self, port_list):
        raise NotImplementedError

    @abc.abstractmethod
    def reserve_network_device(self, device_name, override_reservation):
        raise NotImplementedError

    @abc.abstractmethod
    def reset_buffer_attribute(self, task, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def reset_chan_attribute(self, task, channel, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def reset_device(self, device_name):
        raise NotImplementedError

    @abc.abstractmethod
    def reset_exported_signal_attribute(self, task, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def reset_read_attribute(self, task, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def reset_timing_attribute(self, task, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def reset_timing_attribute_ex(self, task, device_names, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def reset_trig_attribute(self, task, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def reset_watchdog_attribute(self, task, lines, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def reset_write_attribute(self, task, attribute):
        raise NotImplementedError

    @abc.abstractmethod
    def restore_last_ext_cal_const(self, device_name):
        raise NotImplementedError

    @abc.abstractmethod
    def save_global_chan(self, task, channel_name, save_as, author, options):
        raise NotImplementedError

    @abc.abstractmethod
    def save_scale(self, scale_name, save_as, author, options):
        raise NotImplementedError

    @abc.abstractmethod
    def save_task(self, task, save_as, author, options):
        raise NotImplementedError

    @abc.abstractmethod
    def self_cal(self, device_name):
        raise NotImplementedError

    @abc.abstractmethod
    def self_test_device(self, device_name):
        raise NotImplementedError

    @abc.abstractmethod
    def set_analog_power_up_states(
            self, device_name, channel_names, state, channel_type):
        raise NotImplementedError

    @abc.abstractmethod
    def set_analog_power_up_states_with_output_type(
            self, channel_names, state_array, channel_type_array):
        raise NotImplementedError

    @abc.abstractmethod
    def set_buffer_attribute_uint32(self, task, attribute, value):
        raise NotImplementedError

    @abc.abstractmethod
    def set_cal_info_attribute_bool(self, device_name, attribute, value):
        raise NotImplementedError

    @abc.abstractmethod
    def set_cal_info_attribute_double(self, device_name, attribute, value):
        raise NotImplementedError

    @abc.abstractmethod
    def set_cal_info_attribute_string(self, device_name, attribute, value):
        raise NotImplementedError

    @abc.abstractmethod
    def set_cal_info_attribute_uint32(self, device_name, attribute, value):
        raise NotImplementedError

    @abc.abstractmethod
    def set_chan_attribute_bool(self, task, channel, attribute, value):
        raise NotImplementedError

    @abc.abstractmethod
    def set_chan_attribute_double(self, task, channel, attribute, value):
        raise NotImplementedError

    @abc.abstractmethod
    def set_chan_attribute_double_array(self, task, channel, attribute, value):
        raise NotImplementedError

    @abc.abstractmethod
    def set_chan_attribute_int32(self, task, channel, attribute, value):
        raise NotImplementedError

    @abc.abstractmethod
    def set_chan_attribute_string(self, task, channel, attribute, value):
        raise NotImplementedError

    @abc.abstractmethod
    def set_chan_attribute_uint32(self, task, channel, attribute, value):
        raise NotImplementedError

    @abc.abstractmethod
    def set_digital_logic_family_power_up_state(
            self, device_name, logic_family):
        raise NotImplementedError

    @abc.abstractmethod
    def set_digital_power_up_states(self, device_name, channel_names, state):
        raise NotImplementedError

    @abc.abstractmethod
    def set_digital_pull_up_pull_down_states(
            self, device_name, channel_names, state):
        raise NotImplementedError

    @abc.abstractmethod
    def set_exported_signal_attribute_bool(self, task, attribute, value):
        raise NotImplementedError

    @abc.abstractmethod
    def set_exported_signal_attribute_double(self, task, attribute, value):
        raise NotImplementedError

    @abc.abstractmethod
    def set_exported_signal_attribute_int32(self, task, attribute, value):
        raise NotImplementedError

    @abc.abstractmethod
    def set_exported_signal_attribute_string(self, task, attribute, value):
        raise NotImplementedError

    @abc.abstractmethod
    def set_exported_signal_attribute_uint32(self, task, attribute, value):
        raise NotImplementedError

    @abc.abstractmethod
    def set_read_attribute_bool(self, task, attribute, value):
        raise NotImplementedError

    @abc.abstractmethod
    def set_read_attribute_double(self, task, attribute, value):
        raise NotImplementedError

    @abc.abstractmethod
    def set_read_attribute_int32(self, task, attribute, value):
        raise NotImplementedError

    @abc.abstractmethod
    def set_read_attribute_string(self, task, attribute, value):
        raise NotImplementedError

    @abc.abstractmethod
    def set_read_attribute_uint32(self, task, attribute, value):
        raise NotImplementedError

    @abc.abstractmethod
    def set_read_attribute_uint64(self, task, attribute, value):
        raise NotImplementedError

    @abc.abstractmethod
    def set_runtime_environment(
            self, environment, environment_version, reserved_1, reserved_2):
        raise NotImplementedError

    @abc.abstractmethod
    def set_scale_attribute_double(self, scale_name, attribute, value):
        raise NotImplementedError

    @abc.abstractmethod
    def set_scale_attribute_double_array(self, scale_name, attribute, value):
        raise NotImplementedError

    @abc.abstractmethod
    def set_scale_attribute_int32(self, scale_name, attribute, value):
        raise NotImplementedError

    @abc.abstractmethod
    def set_scale_attribute_string(self, scale_name, attribute, value):
        raise NotImplementedError

    @abc.abstractmethod
    def set_timing_attribute_bool(self, task, attribute, value):
        raise NotImplementedError

    @abc.abstractmethod
    def set_timing_attribute_double(self, task, attribute, value):
        raise NotImplementedError

    @abc.abstractmethod
    def set_timing_attribute_ex_bool(
            self, task, device_names, attribute, value):
        raise NotImplementedError

    @abc.abstractmethod
    def set_timing_attribute_ex_double(
            self, task, device_names, attribute, value):
        raise NotImplementedError

    @abc.abstractmethod
    def set_timing_attribute_ex_int32(
            self, task, device_names, attribute, value):
        raise NotImplementedError

    @abc.abstractmethod
    def set_timing_attribute_ex_string(
            self, task, device_names, attribute, value):
        raise NotImplementedError

    @abc.abstractmethod
    def set_timing_attribute_ex_uint32(
            self, task, device_names, attribute, value):
        raise NotImplementedError

    @abc.abstractmethod
    def set_timing_attribute_ex_uint64(
            self, task, device_names, attribute, value):
        raise NotImplementedError

    @abc.abstractmethod
    def set_timing_attribute_int32(self, task, attribute, value):
        raise NotImplementedError

    @abc.abstractmethod
    def set_timing_attribute_string(self, task, attribute, value):
        raise NotImplementedError

    @abc.abstractmethod
    def set_timing_attribute_uint32(self, task, attribute, value):
        raise NotImplementedError

    @abc.abstractmethod
    def set_timing_attribute_uint64(self, task, attribute, value):
        raise NotImplementedError

    @abc.abstractmethod
    def set_trig_attribute_bool(self, task, attribute, value):
        raise NotImplementedError

    @abc.abstractmethod
    def set_trig_attribute_double(self, task, attribute, value):
        raise NotImplementedError

    @abc.abstractmethod
    def set_trig_attribute_double_array(self, task, attribute, value):
        raise NotImplementedError

    @abc.abstractmethod
    def set_trig_attribute_int32(self, task, attribute, value):
        raise NotImplementedError

    @abc.abstractmethod
    def set_trig_attribute_int32_array(self, task, attribute, value):
        raise NotImplementedError

    @abc.abstractmethod
    def set_trig_attribute_string(self, task, attribute, value):
        raise NotImplementedError

    @abc.abstractmethod
    def set_trig_attribute_timestamp(self, task, attribute, value):
        raise NotImplementedError

    @abc.abstractmethod
    def set_trig_attribute_uint32(self, task, attribute, value):
        raise NotImplementedError

    @abc.abstractmethod
    def set_watchdog_attribute_bool(self, task, lines, attribute, value):
        raise NotImplementedError

    @abc.abstractmethod
    def set_watchdog_attribute_double(self, task, lines, attribute, value):
        raise NotImplementedError

    @abc.abstractmethod
    def set_watchdog_attribute_int32(self, task, lines, attribute, value):
        raise NotImplementedError

    @abc.abstractmethod
    def set_watchdog_attribute_string(self, task, lines, attribute, value):
        raise NotImplementedError

    @abc.abstractmethod
    def set_write_attribute_bool(self, task, attribute, value):
        raise NotImplementedError

    @abc.abstractmethod
    def set_write_attribute_double(self, task, attribute, value):
        raise NotImplementedError

    @abc.abstractmethod
    def set_write_attribute_int32(self, task, attribute, value):
        raise NotImplementedError

    @abc.abstractmethod
    def set_write_attribute_string(self, task, attribute, value):
        raise NotImplementedError

    @abc.abstractmethod
    def set_write_attribute_uint32(self, task, attribute, value):
        raise NotImplementedError

    @abc.abstractmethod
    def set_write_attribute_uint64(self, task, attribute, value):
        raise NotImplementedError

    @abc.abstractmethod
    def start_new_file(self, task, file_path):
        raise NotImplementedError

    @abc.abstractmethod
    def start_task(self, task):
        raise NotImplementedError

    @abc.abstractmethod
    def stop_task(self, task):
        raise NotImplementedError

    @abc.abstractmethod
    def task_control(self, task, action):
        raise NotImplementedError

    @abc.abstractmethod
    def tristate_output_term(self, output_terminal):
        raise NotImplementedError

    @abc.abstractmethod
    def unregister_done_event(self, task):
        raise NotImplementedError

    @abc.abstractmethod
    def unregister_every_n_samples_event(
            self, task, every_n_samples_event_type):
        raise NotImplementedError

    @abc.abstractmethod
    def unregister_signal_event(self, task, signal_id):
        raise NotImplementedError

    @abc.abstractmethod
    def unreserve_network_device(self, device_name):
        raise NotImplementedError

    @abc.abstractmethod
    def wait_for_valid_timestamp(self, task, timestamp_event, timeout):
        raise NotImplementedError

    @abc.abstractmethod
    def wait_until_task_done(self, task, time_to_wait):
        raise NotImplementedError

    @abc.abstractmethod
    def write_analog_f64(
            self, task, num_samps_per_chan, auto_start, timeout, data_layout,
            write_array):
        raise NotImplementedError

    @abc.abstractmethod
    def write_analog_scalar_f64(self, task, auto_start, timeout, value):
        raise NotImplementedError

    @abc.abstractmethod
    def write_binary_i16(
            self, task, num_samps_per_chan, auto_start, timeout, data_layout,
            write_array):
        raise NotImplementedError

    @abc.abstractmethod
    def write_binary_i32(
            self, task, num_samps_per_chan, auto_start, timeout, data_layout,
            write_array):
        raise NotImplementedError

    @abc.abstractmethod
    def write_binary_u16(
            self, task, num_samps_per_chan, auto_start, timeout, data_layout,
            write_array):
        raise NotImplementedError

    @abc.abstractmethod
    def write_binary_u32(
            self, task, num_samps_per_chan, auto_start, timeout, data_layout,
            write_array):
        raise NotImplementedError

    @abc.abstractmethod
    def write_ctr_freq(
            self, task, num_samps_per_chan, auto_start, timeout, data_layout,
            frequency, duty_cycle):
        raise NotImplementedError

    @abc.abstractmethod
    def write_ctr_freq_scalar(
            self, task, auto_start, timeout, frequency, duty_cycle):
        raise NotImplementedError

    @abc.abstractmethod
    def write_ctr_ticks(
            self, task, num_samps_per_chan, auto_start, timeout, data_layout,
            high_ticks, low_ticks):
        raise NotImplementedError

    @abc.abstractmethod
    def write_ctr_ticks_scalar(
            self, task, auto_start, timeout, high_ticks, low_ticks):
        raise NotImplementedError

    @abc.abstractmethod
    def write_ctr_time(
            self, task, num_samps_per_chan, auto_start, timeout, data_layout,
            high_time, low_time):
        raise NotImplementedError

    @abc.abstractmethod
    def write_ctr_time_scalar(
            self, task, auto_start, timeout, high_time, low_time):
        raise NotImplementedError

    @abc.abstractmethod
    def write_digital_lines(
            self, task, num_samps_per_chan, auto_start, timeout, data_layout,
            write_array):
        raise NotImplementedError

    @abc.abstractmethod
    def write_digital_scalar_u32(self, task, auto_start, timeout, value):
        raise NotImplementedError

    @abc.abstractmethod
    def write_digital_u16(
            self, task, num_samps_per_chan, auto_start, timeout, data_layout,
            write_array):
        raise NotImplementedError

    @abc.abstractmethod
    def write_digital_u32(
            self, task, num_samps_per_chan, auto_start, timeout, data_layout,
            write_array):
        raise NotImplementedError

    @abc.abstractmethod
    def write_digital_u8(
            self, task, num_samps_per_chan, auto_start, timeout, data_layout,
            write_array):
        raise NotImplementedError

    @abc.abstractmethod
    def write_id_pin_memory(self, device_name, id_pin_name, data, format_code):
        raise NotImplementedError

    @abc.abstractmethod
    def write_raw(self, task, num_samps, auto_start, timeout, write_array):
        raise NotImplementedError

    @abc.abstractmethod
    def write_to_teds_from_array(
            self, physical_channel, bit_stream, basic_teds_options):
        raise NotImplementedError

    @abc.abstractmethod
    def write_to_teds_from_file(
            self, physical_channel, file_path, basic_teds_options):
        raise NotImplementedError

    @abc.abstractmethod
    def hash_task_handle(self, task_handle):
        raise NotImplementedError

    @property
    @abc.abstractmethod
    def driver_version(self):
        raise NotImplementedError

    @abc.abstractmethod
    def read_analog_waveform(
        self,
        task_handle: object,
        number_of_samples_per_channel: int,
        timeout: float,
        waveform: AnalogWaveform[numpy.float64],
        waveform_attribute_mode: WaveformAttributeMode
    ) -> int:
        raise NotImplementedError

    @abc.abstractmethod
    def read_analog_waveforms(
        self,
        task_handle: object,
        number_of_samples_per_channel: int,
        timeout: float,
        waveforms: Sequence[AnalogWaveform[numpy.float64]],
        waveform_attribute_mode: WaveformAttributeMode
    ) -> int:
        raise NotImplementedError

    @abc.abstractmethod
    def read_digital_waveform(
        self,
        task_handle: object,
        number_of_samples_per_channel: int,
        timeout: float,
        waveform: DigitalWaveform[Any],
        waveform_attribute_mode: WaveformAttributeMode
    ) -> int:
        raise NotImplementedError

    @abc.abstractmethod
    def read_digital_waveforms(
        self,
        task_handle: object,
        channel_count: int,
        number_of_samples_per_channel: int,
        number_of_signals_per_sample: int,
        timeout: float,
        waveforms: Sequence[DigitalWaveform[Any]],
        waveform_attribute_mode: WaveformAttributeMode,
    ) -> int:
        raise NotImplementedError

    @abc.abstractmethod
    def read_new_digital_waveforms(
        self,
        task_handle: object,
        channel_count: int,
        number_of_samples_per_channel: int,
        number_of_signals_per_sample: int,
        timeout: float,
        waveform_attribute_mode: WaveformAttributeMode,
    ) -> Sequence[DigitalWaveform[numpy.uint8]]:
        raise NotImplementedError

    @abc.abstractmethod
    def write_analog_waveform(
        self,
        task_handle: object,
        waveform: AnalogWaveform[Any],
        auto_start: bool,
        timeout: float
    ) -> int:
        raise NotImplementedError

    @abc.abstractmethod
    def write_analog_waveforms(
        self,
        task_handle: object,
        waveforms: Sequence[AnalogWaveform[Any]],
        auto_start: bool,
        timeout: float
    ) -> int:
        raise NotImplementedError

    @abc.abstractmethod
    def write_digital_waveform(
        self,
        task_handle: object,
        waveform: DigitalWaveform[Any],
        auto_start: bool,
        timeout: float,
    ) -> int:
        raise NotImplementedError

    def write_digital_waveforms(
        self,
        task_handle: object,
        waveform: Sequence[DigitalWaveform[Any]],
        auto_start: bool,
        timeout: float,
    ) -> int:
        raise NotImplementedError
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=generated/nidaqmx/_bitfield_utils.py sha256=c1205b4672ce4d0acf149e5c800414f015b021a85500e309f5f3c82c12fb6ff6 bytes=1440 -->
## FILE: generated/nidaqmx/_bitfield_utils.py

- repository: `ni/nidaqmx-python`
- source_path: `generated/nidaqmx/_bitfield_utils.py`
- sha256: `c1205b4672ce4d0acf149e5c800414f015b021a85500e309f5f3c82c12fb6ff6`
- bytes: 1440

````python
def enum_bitfield_to_list(bitfield_value, bitfield_enum_type, actual_enum_type):
    """Converts a bitfield value to a list of enums.

    Args:
        bitfield_value (int): Specifies the value of the bitfield.
        bitfield_enum_type (enum.Enum): Specifies the bitfield enum type
            from which to mask and extract the enum values.
        actual_enum_type (enum.Enum): Specifies the actual enum type.

    Returns:
        List[enum.Enum]: Indicates the converted list of enums.
    """
    supported_values = []
    for bitfield_mask in bitfield_enum_type:
        if bitfield_value & bitfield_mask.value:
            enum_value = next(e for e in actual_enum_type if e.name == bitfield_mask.name)
            supported_values.append(enum_value)

    return supported_values


def enum_list_to_bitfield(enum_list, bitfield_enum_type):
    """Converts a list of enums to a bitfield value.

    Args:
        enum_list (List[enum.Enum]): Specifies the list of enums.
        bitfield_enum_type (enum.Enum): Specifies the bitfield enum type
            from which to mask and extract the enum values.

    Returns:
        int: Indicates the value of the bitfield.
    """
    bitfield_value = 0
    for enum_value in enum_list:
        bitfield_mask = next(b for b in bitfield_enum_type if b.name == enum_value.name)
        bitfield_value |= bitfield_mask.value

    return bitfield_value
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=generated/nidaqmx/_dotenv_path.py sha256=d604cfae5b35b0ceda93e2e034c1e075b16beb8cfc792e42a212402d4c627404 bytes=2377 -->
## FILE: generated/nidaqmx/_dotenv_path.py

- repository: `ni/nidaqmx-python`
- source_path: `generated/nidaqmx/_dotenv_path.py`
- sha256: `d604cfae5b35b0ceda93e2e034c1e075b16beb8cfc792e42a212402d4c627404`
- bytes: 2377

````python
from __future__ import annotations

import inspect
import sys
import traceback
from pathlib import Path


def get_dotenv_search_path() -> Path:
    """Get the search path for loading the `.env` file."""
    # Prefer to load the `.env` file from the current directory or its parents.
    # If the current directory doesn't have a `.env` file, fall back to the
    # script/EXE path or the TestStand code module path.
    cwd = Path.cwd()
    if not _has_dotenv_file(cwd):
        if script_or_exe_path := _get_script_or_exe_path():
            return script_or_exe_path.resolve().parent
        if caller_path := _get_caller_path():
            return caller_path.resolve().parent
    return cwd


def _has_dotenv_file(dir: Path) -> bool:
    """Check whether the dir or its parents contains a `.env` file."""
    return (dir / ".env").exists() or any((p / ".env").exists() for p in dir.parents)


def _get_script_or_exe_path() -> Path | None:
    """Get the path of the top-level script or PyInstaller EXE, if possible."""
    if getattr(sys, "frozen", False):
        return Path(sys.executable)

    main_module = sys.modules.get("__main__")
    if main_module:
        script_path = getattr(main_module, "__file__", "")
        if script_path:
            return Path(script_path)

    return None


def _get_caller_path() -> Path | None:
    """Get the path of the module calling into this package, if possible."""
    package_path = _get_package_path()
    for frame, _ in traceback.walk_stack(inspect.currentframe()):
        if frame.f_code.co_filename:
            module_path = Path(frame.f_code.co_filename)
            if _exists(module_path) and not module_path.is_relative_to(package_path):
                return module_path

    return None


# Path.exists() throws OSError when the path has invalid file characters.
# https://github.com/python/cpython/issues/79487
if sys.version_info >= (3, 10):

    def _exists(path: Path) -> bool:
        return path.exists()

else:

    def _exists(path: Path) -> bool:
        import os

        return os.path.exists(path)


def _get_package_path() -> Path:
    """Get the path of this package."""
    module = sys.modules[__package__]
    assert module.__file__ and module.__file__.endswith("__init__.py")
    return Path(module.__file__).parent
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=generated/nidaqmx/_feature_toggles.py sha256=1d45e17aaa91e0d3648960dd6ef7fd1f64105ad5ceb496bffc68b84e4ffd9c53 bytes=4969 -->
## FILE: generated/nidaqmx/_feature_toggles.py

- repository: `ni/nidaqmx-python`
- source_path: `generated/nidaqmx/_feature_toggles.py`
- sha256: `1d45e17aaa91e0d3648960dd6ef7fd1f64105ad5ceb496bffc68b84e4ffd9c53`
- bytes: 4969

````python
"""nidaqmx feature toggles."""

# mypy: no-warn-unreachable
from __future__ import annotations

import functools
from collections.abc import Callable
from enum import Enum
from typing import TYPE_CHECKING, TypeVar

from decouple import AutoConfig, Undefined, undefined

from nidaqmx._dotenv_path import get_dotenv_search_path
from nidaqmx.errors import FeatureNotSupportedError

if TYPE_CHECKING:
    from typing_extensions import ParamSpec, Self

    _P = ParamSpec("_P")
    _T = TypeVar("_T")

_PREFIX = "NIDAQMX"

if TYPE_CHECKING:
    # Work around decouple's lack of type hints.
    def _config(
        option: str,
        default: _T | Undefined = undefined,
        cast: Callable[[str], _T] | Undefined = undefined,
    ) -> _T: ...

else:
    _config = AutoConfig(str(get_dotenv_search_path()))


# Based on the recipe at https://docs.python.org/3/howto/enum.html
class _OrderedEnum(Enum):
    def __ge__(self, other: Self) -> bool:
        if self.__class__ is other.__class__:
            return self.value >= other.value
        return NotImplemented

    def __gt__(self, other: Self) -> bool:
        if self.__class__ is other.__class__:
            return self.value > other.value
        return NotImplemented

    def __le__(self, other: Self) -> bool:
        if self.__class__ is other.__class__:
            return self.value <= other.value
        return NotImplemented

    def __lt__(self, other: Self) -> bool:
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented


class CodeReadiness(_OrderedEnum):
    """Indicates whether code is ready to be supported."""

    RELEASE = 0
    NEXT_RELEASE = 1
    INCOMPLETE = 2
    PROTOTYPE = 3


def _init_code_readiness_level() -> CodeReadiness:
    if _config(f"{_PREFIX}_ALLOW_INCOMPLETE", default=False, cast=bool):
        return CodeReadiness.INCOMPLETE
    elif _config(f"{_PREFIX}_ALLOW_NEXT_RELEASE", default=False, cast=bool):
        return CodeReadiness.NEXT_RELEASE
    else:
        return CodeReadiness.RELEASE


# This is not public because `from _feature_toggles import CODE_READINESS_LEVEL`
# is incompatible with the patching performed by the use_code_readiness mark.
_CODE_READINESS_LEVEL = _init_code_readiness_level()


def get_code_readiness_level() -> CodeReadiness:
    """Get the current code readiness level.

    You can override this in tests by specifying the ``use_code_readiness``
    mark.
    """
    return _CODE_READINESS_LEVEL


class FeatureToggle:
    """A run-time feature toggle."""

    name: str
    """The name of the feature."""

    readiness: CodeReadiness
    """The code readiness at which this feature is enabled."""

    def __init__(self, name: str, readiness: CodeReadiness) -> None:
        """Initialize the feature toggle."""
        assert name == name.upper()
        self.name = name
        self.readiness = readiness
        self._is_enabled_override = None
        # Only read the env var at initialization time.
        if _config(f"{_PREFIX}_ENABLE_{name}", default=False, cast=bool):
            self._is_enabled_override = True

    @property
    def is_enabled(self) -> bool:
        """Indicates whether the feature is currently enabled.

        You can enable/disable features in tests by specifying the
        ``enable_feature_toggle`` or ``disable_feature_toggle`` marks.
        """
        if self._is_enabled_override is not None:
            return self._is_enabled_override
        return self.readiness <= get_code_readiness_level()

    def raise_if_disabled(self) -> None:
        """Raises an error if the feature is disabled."""
        if self.is_enabled:
            return

        env_vars = f"{_PREFIX}_ENABLE_{self.name}"
        if self.readiness in [CodeReadiness.NEXT_RELEASE, CodeReadiness.INCOMPLETE]:
            env_vars += f" or {_PREFIX}_ALLOW_{self.readiness.name}"
        message = (
            f"The {self.name} feature is not supported at the current code readiness level. "
            f" To enable it, set {env_vars}."
        )
        raise FeatureNotSupportedError(message)


def requires_feature(
    feature_toggle: FeatureToggle,
) -> Callable[[Callable[_P, _T]], Callable[_P, _T]]:
    """Decorator specifying that the function requires the specified feature toggle."""

    def decorator(func: Callable[_P, _T]) -> Callable[_P, _T]:
        @functools.wraps(func)
        def wrapper(*args: _P.args, **kwargs: _P.kwargs) -> _T:
            feature_toggle.raise_if_disabled()
            return func(*args, **kwargs)

        return wrapper

    return decorator


# --------------------------------------
# Define feature toggle constants here:
# --------------------------------------

WAVEFORM_SUPPORT = FeatureToggle("WAVEFORM_SUPPORT", CodeReadiness.RELEASE)
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=generated/nidaqmx/_grpc_interpreter.py sha256=330c24d06a5e3f4821080da120a504f6d394a364478efde533dd2d1b74270782 bytes=186668 -->
## FILE: generated/nidaqmx/_grpc_interpreter.py

- repository: `ni/nidaqmx-python`
- source_path: `generated/nidaqmx/_grpc_interpreter.py`
- sha256: `330c24d06a5e3f4821080da120a504f6d394a364478efde533dd2d1b74270782`
- bytes: 186668

````python
# Do not edit this file; it was automatically generated.

from __future__ import annotations
import logging
import threading
import typing
import warnings
from nitypes.waveform import AnalogWaveform, DigitalWaveform
from typing import Any, Generic, TypeVar

from collections.abc import Callable, Sequence

import google.protobuf.message
import grpc
import numpy

from . import errors as errors
from nidaqmx._base_interpreter import BaseEventHandler, BaseInterpreter
from nidaqmx._stubs import nidaqmx_pb2 as grpc_types
from nidaqmx._stubs import nidaqmx_pb2_grpc as nidaqmx_grpc
from ni.protobuf.types.waveform_conversion import (
    digital_waveform_from_protobuf,
    digital_waveform_to_protobuf,
    float64_analog_waveform_from_protobuf,
    float64_analog_waveform_to_protobuf
)
from nidaqmx.constants import WaveformAttributeMode
from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.types import DriverVersion
from nidaqmx._grpc_time import convert_time_to_timestamp, convert_timestamp_to_time
from nidaqmx._waveform_utils import get_num_samps_per_chan
from session_pb2 import Session

_logger = logging.getLogger(__name__)

_UNABLE_TO_LOCATE_ERROR_RESOURCES_ERROR_MESSAGE = (
    "Error code could not be found. Reinstalling the driver might fix the issue. "
    "Otherwise, contact National Instruments technical support."
)


TEventResponse = TypeVar("TEventResponse", bound=google.protobuf.message.Message)

class GrpcEventHandler(BaseEventHandler, Generic[TEventResponse]):
    """Manage the lifetime of a gRPC event stream."""
    __slots__ = [
        "_event_name",
        "_interpreter",
        "_event_stream",
        "_event_callback",
        "_event_stream_exception",
        "_thread",
    ]

    def __init__(
        self,
        event_name: str,
        interpreter: GrpcStubInterpreter,
        event_stream: grpc._CallIterator[TEventResponse],
        event_callback: Callable[[TEventResponse], None],
    ) -> None:
        self._event_name = event_name
        self._interpreter = interpreter
        self._event_stream = event_stream
        self._event_callback = event_callback
        self._event_stream_exception: Exception | None = None
        self._thread = threading.Thread(target=self._thread_main, name=f"nidaqmx {event_name} thread")

        self._thread.start()

    def close(self) -> None:
        self._event_stream.cancel()
        self._thread.join()
        if self._event_stream_exception is not None:
            raise self._event_stream_exception

    def _thread_main(self) -> None:
        try:
            for event_response in self._event_stream:
                self._event_callback(event_response)
        except Exception as ex:
            if _is_cancelled(ex):
                return
            _logger.exception(
                "Unhandled exception raised while reading nidaqmx %s stream.", self._event_name
            )
            # Save the exception and re-raise it at the end of close().
            self._event_stream_exception = ex
            return


class GrpcStubInterpreter(BaseInterpreter):
    '''Interpreter for interacting with a gRPC Stub class'''
    # Do not add per-task state to the interpreter class.
    __slots__ = [
        '_grpc_options',
        '_client',
        '_driver_version',
    ]

    def __init__(self, grpc_options):
        self._grpc_options = grpc_options
        self._client = nidaqmx_grpc.NiDAQmxStub(grpc_options.grpc_channel)
        try:
            major_version = self.get_system_info_attribute_uint32(0x1272)
            minor_version = self.get_system_info_attribute_uint32(0x1923)
            update_version = self.get_system_info_attribute_uint32(0x2f22)
        except Exception:
            major_version = 0
            minor_version = 0
            update_version = 0
        self._driver_version = DriverVersion(major_version, minor_version, update_version)

    def _invoke(self, func, request, metadata=None):
        try:
            response = func(request, metadata=metadata)
        except grpc.RpcError as rpc_error:
            self._handle_rpc_error(rpc_error)
        return response

    def _handle_rpc_error(self, rpc_error):
        error_message = rpc_error.details()
        error_code = None
        samps_per_chan_read = None
        samps_per_chan_written = None
        for entry in rpc_error.trailing_metadata() or []:
            if entry.key == 'ni-error':
                try:
                    error_code = int(typing.cast(str, entry.value))
                except ValueError:
                    error_message += f'\nError status: {entry.value}'
            elif entry.key == "ni-samps-per-chan-read":
                try:
                    samps_per_chan_read = int(typing.cast(str, entry.value))
                except ValueError:
                    error_message += f'\nSamples per channel read: {entry.value}'
            elif entry.key == "ni-samps-per-chan-written":
                try:
                    samps_per_chan_written = int(typing.cast(str, entry.value))
                except ValueError:
                    error_message += f'\nSamples per channel written: {entry.value}'
        grpc_error = rpc_error.code()
        if grpc_error == grpc.StatusCode.UNAVAILABLE:
            error_message = 'Failed to connect to server'
        elif grpc_error == grpc.StatusCode.UNIMPLEMENTED:
            error_message = (
                'This operation is not supported by the NI gRPC Device Server being used. Upgrade NI gRPC Device Server.'
            )
        if error_code is None:
            raise errors.RpcError(grpc_error, error_message) from None
        else:
            self._raise_error(error_code, error_message, samps_per_chan_written, samps_per_chan_read)

    def _check_for_error_from_response(self, error_code, samps_per_chan_written=None, samps_per_chan_read=None):
        if error_code != 0:
            # This is an optimization for the partial read operation.
            error_message = _ERROR_MESSAGES.get(error_code, None)
            if not error_message:
                error_message = self.get_error_string(error_code)
            self._raise_error(error_code, error_message, samps_per_chan_written=samps_per_chan_written, samps_per_chan_read=samps_per_chan_read)

    def _raise_error(self, error_code, error_message, samps_per_chan_written=None, samps_per_chan_read=None):
        if error_code < 0:
            if samps_per_chan_read is not None:
                raise errors.DaqReadError(error_message, error_code, samps_per_chan_read) from None
            elif samps_per_chan_written is not None:
                raise errors.DaqWriteError(error_message, error_code, samps_per_chan_written) from None
            else:
                raise errors.DaqError(error_message, error_code) from None
        elif error_code > 0:
            if not error_message:
                error_message = self.get_error_string(error_code)
            warnings.warn(errors.DaqWarning(error_message, error_code))

    def _check_for_event_registration_error(self, event_stream):
        try:
            # Wait for initial metadata to ensure that the server has received the event
            # registration request and called the event registration function. Otherwise,
            # there is no guarantee that the event registration function is called before
            # the application sends the next RPC request (e.g. start_task).
            _ = event_stream.initial_metadata()

            # When the event registration function returns an error, the server should close
            # the event stream with an error before sending initial metadata. This behavior
            # requires NI gRPC Device Server version 2.2 or later.
            if event_stream.done() and event_stream.exception() is not None:
                raise event_stream.exception()
        except grpc.RpcError as rpc_error:
            self._handle_rpc_error(rpc_error)

    @property
    def driver_version(self):
        return self._driver_version

    def add_cdaq_sync_connection(self, port_list):
        response = self._invoke(
            self._client.AddCDAQSyncConnection,
            grpc_types.AddCDAQSyncConnectionRequest(port_list=port_list))

    def add_global_chans_to_task(self, task, channel_names):
        response = self._invoke(
            self._client.AddGlobalChansToTask,
            grpc_types.AddGlobalChansToTaskRequest(task=task, channel_names=channel_names))

    def add_network_device(
            self, ip_address, device_name, attempt_reservation, timeout):
        response = self._invoke(
            self._client.AddNetworkDevice,
            grpc_types.AddNetworkDeviceRequest(
                ip_address=ip_address, device_name=device_name,
                attempt_reservation=attempt_reservation, timeout=timeout))
        return response.device_name_out

    def are_configured_cdaq_sync_ports_disconnected(
            self, chassis_devices_ports, timeout):
        response = self._invoke(
            self._client.AreConfiguredCDAQSyncPortsDisconnected,
            grpc_types.AreConfiguredCDAQSyncPortsDisconnectedRequest(
                chassis_devices_ports=chassis_devices_ports, timeout=timeout))
        return response.disconnected_ports_exist

    def auto_configure_cdaq_sync_connections(
            self, chassis_devices_ports, timeout):
        response = self._invoke(
            self._client.AutoConfigureCDAQSyncConnections,
            grpc_types.AutoConfigureCDAQSyncConnectionsRequest(
                chassis_devices_ports=chassis_devices_ports, timeout=timeout))

    def calculate_reverse_poly_coeff(
            self, forward_coeffs, min_val_x, max_val_x, num_points_to_compute,
            reverse_poly_order):
        response = self._invoke(
            self._client.CalculateReversePolyCoeff,
            grpc_types.CalculateReversePolyCoeffRequest(
                forward_coeffs=forward_coeffs, min_val_x=min_val_x,
                max_val_x=max_val_x,
                num_points_to_compute=num_points_to_compute,
                reverse_poly_order=reverse_poly_order))
        return list(response.reverse_coeffs)

    def cfg_anlg_edge_ref_trig(
            self, task, trigger_source, pretrigger_samples, trigger_slope,
            trigger_level):
        response = self._invoke(
            self._client.CfgAnlgEdgeRefTrig,
            grpc_types.CfgAnlgEdgeRefTrigRequest(
                task=task, trigger_source=trigger_source,
                pretrigger_samples=pretrigger_samples,
                trigger_slope_raw=trigger_slope, trigger_level=trigger_level))

    def cfg_anlg_edge_start_trig(
            self, task, trigger_source, trigger_slope, trigger_level):
        response = self._invoke(
            self._client.CfgAnlgEdgeStartTrig,
            grpc_types.CfgAnlgEdgeStartTrigRequest(
                task=task, trigger_source=trigger_source,
                trigger_slope_raw=trigger_slope, trigger_level=trigger_level))

    def cfg_anlg_multi_edge_ref_trig(
            self, task, trigger_sources, pretrigger_samples,
            trigger_slope_array, trigger_level_array):
        response = self._invoke(
            self._client.CfgAnlgMultiEdgeRefTrig,
            grpc_types.CfgAnlgMultiEdgeRefTrigRequest(
                task=task, trigger_sources=trigger_sources,
                pretrigger_samples=pretrigger_samples,
                trigger_slope_array=trigger_slope_array,
                trigger_level_array=trigger_level_array))

    def cfg_anlg_multi_edge_start_trig(
            self, task, trigger_sources, trigger_slope_array,
            trigger_level_array):
        response = self._invoke(
            self._client.CfgAnlgMultiEdgeStartTrig,
            grpc_types.CfgAnlgMultiEdgeStartTrigRequest(
                task=task, trigger_sources=trigger_sources,
                trigger_slope_array=trigger_slope_array,
                trigger_level_array=trigger_level_array))

    def cfg_anlg_window_ref_trig(
            self, task, trigger_source, window_top, window_bottom,
            pretrigger_samples, trigger_when):
        response = self._invoke(
            self._client.CfgAnlgWindowRefTrig,
            grpc_types.CfgAnlgWindowRefTrigRequest(
                task=task, trigger_source=trigger_source,
                window_top=window_top, window_bottom=window_bottom,
                pretrigger_samples=pretrigger_samples,
                trigger_when_raw=trigger_when))

    def cfg_anlg_window_start_trig(
            self, task, window_top, window_bottom, trigger_source,
            trigger_when):
        response = self._invoke(
            self._client.CfgAnlgWindowStartTrig,
            grpc_types.CfgAnlgWindowStartTrigRequest(
                task=task, window_top=window_top, window_bottom=window_bottom,
                trigger_source=trigger_source, trigger_when_raw=trigger_when))

    def cfg_burst_handshaking_timing_export_clock(
            self, task, sample_clk_rate, sample_clk_outp_term, sample_mode,
            samps_per_chan, sample_clk_pulse_polarity, pause_when,
            ready_event_active_level):
        response = self._invoke(
            self._client.CfgBurstHandshakingTimingExportClock,
            grpc_types.CfgBurstHandshakingTimingExportClockRequest(
                task=task, sample_clk_rate=sample_clk_rate,
                sample_clk_outp_term=sample_clk_outp_term,
                sample_mode_raw=sample_mode, samps_per_chan=samps_per_chan,
                sample_clk_pulse_polarity_raw=sample_clk_pulse_polarity,
                pause_when_raw=pause_when,
                ready_event_active_level_raw=ready_event_active_level))

    def cfg_burst_handshaking_timing_import_clock(
            self, task, sample_clk_rate, sample_clk_src, sample_mode,
            samps_per_chan, sample_clk_active_edge, pause_when,
            ready_event_active_level):
        response = self._invoke(
            self._client.CfgBurstHandshakingTimingImportClock,
            grpc_types.CfgBurstHandshakingTimingImportClockRequest(
                task=task, sample_clk_rate=sample_clk_rate,
                sample_clk_src=sample_clk_src, sample_mode_raw=sample_mode,
                samps_per_chan=samps_per_chan,
                sample_clk_active_edge_raw=sample_clk_active_edge,
                pause_when_raw=pause_when,
                ready_event_active_level_raw=ready_event_active_level))

    def cfg_change_detection_timing(
            self, task, rising_edge_chan, falling_edge_chan, sample_mode,
            samps_per_chan):
        response = self._invoke(
            self._client.CfgChangeDetectionTiming,
            grpc_types.CfgChangeDetectionTimingRequest(
                task=task, rising_edge_chan=rising_edge_chan,
                falling_edge_chan=falling_edge_chan,
                sample_mode_raw=sample_mode, samps_per_chan=samps_per_chan))

    def cfg_dig_edge_ref_trig(
            self, task, trigger_source, pretrigger_samples, trigger_edge):
        response = self._invoke(
            self._client.CfgDigEdgeRefTrig,
            grpc_types.CfgDigEdgeRefTrigRequest(
                task=task, trigger_source=trigger_source,
                pretrigger_samples=pretrigger_samples,
                trigger_edge_raw=trigger_edge))

    def cfg_dig_edge_start_trig(self, task, trigger_source, trigger_edge):
        response = self._invoke(
            self._client.CfgDigEdgeStartTrig,
            grpc_types.CfgDigEdgeStartTrigRequest(
                task=task, trigger_source=trigger_source,
                trigger_edge_raw=trigger_edge))

    def cfg_dig_pattern_ref_trig(
            self, task, trigger_source, trigger_pattern, pretrigger_samples,
            trigger_when):
        response = self._invoke(
            self._client.CfgDigPatternRefTrig,
            grpc_types.CfgDigPatternRefTrigRequest(
                task=task, trigger_source=trigger_source,
                trigger_pattern=trigger_pattern,
                pretrigger_samples=pretrigger_samples,
                trigger_when_raw=trigger_when))

    def cfg_dig_pattern_start_trig(
            self, task, trigger_source, trigger_pattern, trigger_when):
        response = self._invoke(
            self._client.CfgDigPatternStartTrig,
            grpc_types.CfgDigPatternStartTrigRequest(
                task=task, trigger_source=trigger_source,
                trigger_pattern=trigger_pattern,
                trigger_when_raw=trigger_when))

    def cfg_handshaking_timing(self, task, sample_mode, samps_per_chan):
        response = self._invoke(
            self._client.CfgHandshakingTiming,
            grpc_types.CfgHandshakingTimingRequest(
                task=task, sample_mode_raw=sample_mode,
                samps_per_chan=samps_per_chan))

    def cfg_implicit_timing(self, task, sample_mode, samps_per_chan):
        response = self._invoke(
            self._client.CfgImplicitTiming,
            grpc_types.CfgImplicitTimingRequest(
                task=task, sample_mode_raw=sample_mode,
                samps_per_chan=samps_per_chan))

    def cfg_pipelined_samp_clk_timing(
            self, task, rate, source, active_edge, sample_mode,
            samps_per_chan):
        response = self._invoke(
            self._client.CfgPipelinedSampClkTiming,
            grpc_types.CfgPipelinedSampClkTimingRequest(
                task=task, rate=rate, source=source,
                active_edge_raw=active_edge, sample_mode_raw=sample_mode,
                samps_per_chan=samps_per_chan))

    def cfg_samp_clk_timing(
            self, task, rate, source, active_edge, sample_mode,
            samps_per_chan):
        response = self._invoke(
            self._client.CfgSampClkTiming,
            grpc_types.CfgSampClkTimingRequest(
                task=task, rate=rate, source=source,
                active_edge_raw=active_edge, sample_mode_raw=sample_mode,
                samps_per_chan=samps_per_chan))

    def cfg_time_start_trig(self, task, when, timescale):
        response = self._invoke(
            self._client.CfgTimeStartTrig,
            grpc_types.CfgTimeStartTrigRequest(
                task=task, when=convert_time_to_timestamp(when),
                timescale_raw=timescale))

    def cfg_watchdog_ao_expir_states(
            self, task, channel_names, expir_state_array, output_type_array):
        response = self._invoke(
            self._client.CfgWatchdogAOExpirStates,
            grpc_types.CfgWatchdogAOExpirStatesRequest(
                task=task, channel_names=channel_names,
                expir_state_array=expir_state_array,
                output_type_array=output_type_array))

    def cfg_watchdog_co_expir_states(
            self, task, channel_names, expir_state_array):
        response = self._invoke(
            self._client.CfgWatchdogCOExpirStates,
            grpc_types.CfgWatchdogCOExpirStatesRequest(
                task=task, channel_names=channel_names,
                expir_state_array=expir_state_array))

    def cfg_watchdog_do_expir_states(
            self, task, channel_names, expir_state_array):
        response = self._invoke(
            self._client.CfgWatchdogDOExpirStates,
            grpc_types.CfgWatchdogDOExpirStatesRequest(
                task=task, channel_names=channel_names,
                expir_state_array=expir_state_array))

    def clear_task(self, task):
        response = self._invoke(
            self._client.ClearTask,
            grpc_types.ClearTaskRequest(task=task))

    def clear_teds(self, physical_channel):
        response = self._invoke(
            self._client.ClearTEDS,
            grpc_types.ClearTEDSRequest(physical_channel=physical_channel))

    def configure_logging(
            self, task, file_path, logging_mode, group_name, operation):
        response = self._invoke(
            self._client.ConfigureLogging,
            grpc_types.ConfigureLoggingRequest(
                task=task, file_path=file_path, logging_mode_raw=logging_mode,
                group_name=group_name, operation_raw=operation))

    def configure_teds(self, physical_channel, file_path):
        response = self._invoke(
            self._client.ConfigureTEDS,
            grpc_types.ConfigureTEDSRequest(physical_channel=physical_channel, file_path=file_path))

    def connect_terms(
            self, source_terminal, destination_terminal, signal_modifiers):
        response = self._invoke(
            self._client.ConnectTerms,
            grpc_types.ConnectTermsRequest(
                source_terminal=source_terminal,
                destination_terminal=destination_terminal,
                signal_modifiers_raw=signal_modifiers))

    def control_watchdog_task(self, task, action):
        response = self._invoke(
            self._client.ControlWatchdogTask,
            grpc_types.ControlWatchdogTaskRequest(task=task, action_raw=action))

    def create_ai_accel4_wire_dc_voltage_chan(
            self, task, physical_channel, name_to_assign_to_channel,
            terminal_config, min_val, max_val, units, sensitivity,
            sensitivity_units, voltage_excit_source, voltage_excit_val,
            use_excit_for_scaling, custom_scale_name):
        response = self._invoke(
            self._client.CreateAIAccel4WireDCVoltageChan,
            grpc_types.CreateAIAccel4WireDCVoltageChanRequest(
                task=task, physical_channel=physical_channel,
                name_to_assign_to_channel=name_to_assign_to_channel,
                terminal_config_raw=terminal_config, min_val=min_val,
                max_val=max_val, units_raw=units, sensitivity=sensitivity,
                sensitivity_units_raw=sensitivity_units,
                voltage_excit_source_raw=voltage_excit_source,
                voltage_excit_val=voltage_excit_val,
                use_excit_for_scaling=use_excit_for_scaling,
                custom_scale_name=custom_scale_name))

    def create_ai_accel_chan(
            self, task, physical_channel, name_to_assign_to_channel,
            terminal_config, min_val, max_val, units, sensitivity,
            sensitivity_units, current_excit_source, current_excit_val,
            custom_scale_name):
        response = self._invoke(
            self._client.CreateAIAccelChan,
            grpc_types.CreateAIAccelChanRequest(
                task=task, physical_channel=physical_channel,
                name_to_assign_to_channel=name_to_assign_to_channel,
                terminal_config_raw=terminal_config, min_val=min_val,
                max_val=max_val, units_raw=units, sensitivity=sensitivity,
                sensitivity_units_raw=sensitivity_units,
                current_excit_source_raw=current_excit_source,
                current_excit_val=current_excit_val,
                custom_scale_name=custom_scale_name))

    def create_ai_accel_charge_chan(
            self, task, physical_channel, name_to_assign_to_channel,
            terminal_config, min_val, max_val, units, sensitivity,
            sensitivity_units, custom_scale_name):
        response = self._invoke(
            self._client.CreateAIAccelChargeChan,
            grpc_types.CreateAIAccelChargeChanRequest(
                task=task, physical_channel=physical_channel,
                name_to_assign_to_channel=name_to_assign_to_channel,
                terminal_config_raw=terminal_config, min_val=min_val,
                max_val=max_val, units_raw=units, sensitivity=sensitivity,
                sensitivity_units_raw=sensitivity_units,
                custom_scale_name=custom_scale_name))

    def create_ai_bridge_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, bridge_config, voltage_excit_source,
            voltage_excit_val, nominal_bridge_resistance, custom_scale_name):
        response = self._invoke(
            self._client.CreateAIBridgeChan,
            grpc_types.CreateAIBridgeChanRequest(
                task=task, physical_channel=physical_channel,
                name_to_assign_to_channel=name_to_assign_to_channel,
                min_val=min_val, max_val=max_val, units_raw=units,
                bridge_config_raw=bridge_config,
                voltage_excit_source_raw=voltage_excit_source,
                voltage_excit_val=voltage_excit_val,
                nominal_bridge_resistance=nominal_bridge_resistance,
                custom_scale_name=custom_scale_name))

    def create_ai_calculated_power_chan(
            self, task, voltage_physical_channel, current_physical_channel,
            name_to_assign_to_channel, terminal_config, voltage_min_val,
            voltage_max_val, current_min_val, current_max_val, units,
            shunt_resistor_loc, ext_shunt_resistor_val, custom_scale_name):
        response = self._invoke(
            self._client.CreateAICalculatedPowerChan,
            grpc_types.CreateAICalculatedPowerChanRequest(
                task=task, voltage_physical_channel=voltage_physical_channel,
                current_physical_channel=current_physical_channel,
                name_to_assign_to_channel=name_to_assign_to_channel,
                terminal_config_raw=terminal_config,
                voltage_min_val=voltage_min_val,
                voltage_max_val=voltage_max_val,
                current_min_val=current_min_val,
                current_max_val=current_max_val, units_raw=units,
                shunt_resistor_loc_raw=shunt_resistor_loc,
                ext_shunt_resistor_val=ext_shunt_resistor_val,
                custom_scale_name=custom_scale_name))

    def create_ai_charge_chan(
            self, task, physical_channel, name_to_assign_to_channel,
            terminal_config, min_val, max_val, units, custom_scale_name):
        response = self._invoke(
            self._client.CreateAIChargeChan,
            grpc_types.CreateAIChargeChanRequest(
                task=task, physical_channel=physical_channel,
                name_to_assign_to_channel=name_to_assign_to_channel,
                terminal_config_raw=terminal_config, min_val=min_val,
                max_val=max_val, units_raw=units,
                custom_scale_name=custom_scale_name))

    def create_ai_current_chan(
            self, task, physical_channel, name_to_assign_to_channel,
            terminal_config, min_val, max_val, units, shunt_resistor_loc,
            ext_shunt_resistor_val, custom_scale_name):
        response = self._invoke(
            self._client.CreateAICurrentChan,
            grpc_types.CreateAICurrentChanRequest(
                task=task, physical_channel=physical_channel,
                name_to_assign_to_channel=name_to_assign_to_channel,
                terminal_config_raw=terminal_config, min_val=min_val,
                max_val=max_val, units_raw=units,
                shunt_resistor_loc_raw=shunt_resistor_loc,
                ext_shunt_resistor_val=ext_shunt_resistor_val,
                custom_scale_name=custom_scale_name))

    def create_ai_current_rms_chan(
            self, task, physical_channel, name_to_assign_to_channel,
            terminal_config, min_val, max_val, units, shunt_resistor_loc,
            ext_shunt_resistor_val, custom_scale_name):
        response = self._invoke(
            self._client.CreateAICurrentRMSChan,
            grpc_types.CreateAICurrentRMSChanRequest(
                task=task, physical_channel=physical_channel,
                name_to_assign_to_channel=name_to_assign_to_channel,
                terminal_config_raw=terminal_config, min_val=min_val,
                max_val=max_val, units_raw=units,
                shunt_resistor_loc_raw=shunt_resistor_loc,
                ext_shunt_resistor_val=ext_shunt_resistor_val,
                custom_scale_name=custom_scale_name))

    def create_ai_force_bridge_polynomial_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, bridge_config, voltage_excit_source,
            voltage_excit_val, nominal_bridge_resistance, forward_coeffs,
            reverse_coeffs, electrical_units, physical_units,
            custom_scale_name):
        response = self._invoke(
            self._client.CreateAIForceBridgePolynomialChan,
            grpc_types.CreateAIForceBridgePolynomialChanRequest(
                task=task, physical_channel=physical_channel,
                name_to_assign_to_channel=name_to_assign_to_channel,
                min_val=min_val, max_val=max_val, units_raw=units,
                bridge_config_raw=bridge_config,
                voltage_excit_source_raw=voltage_excit_source,
                voltage_excit_val=voltage_excit_val,
                nominal_bridge_resistance=nominal_bridge_resistance,
                forward_coeffs=forward_coeffs, reverse_coeffs=reverse_coeffs,
                electrical_units_raw=electrical_units,
                physical_units_raw=physical_units,
                custom_scale_name=custom_scale_name))

    def create_ai_force_bridge_table_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, bridge_config, voltage_excit_source,
            voltage_excit_val, nominal_bridge_resistance, electrical_vals,
            electrical_units, physical_vals, physical_units,
            custom_scale_name):
        response = self._invoke(
            self._client.CreateAIForceBridgeTableChan,
            grpc_types.CreateAIForceBridgeTableChanRequest(
                task=task, physical_channel=physical_channel,
                name_to_assign_to_channel=name_to_assign_to_channel,
                min_val=min_val, max_val=max_val, units_raw=units,
                bridge_config_raw=bridge_config,
                voltage_excit_source_raw=voltage_excit_source,
                voltage_excit_val=voltage_excit_val,
                nominal_bridge_resistance=nominal_bridge_resistance,
                electrical_vals=electrical_vals,
                electrical_units_raw=electrical_units,
                physical_vals=physical_vals,
                physical_units_raw=physical_units,
                custom_scale_name=custom_scale_name))

    def create_ai_force_bridge_two_point_lin_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, bridge_config, voltage_excit_source,
            voltage_excit_val, nominal_bridge_resistance,
            first_electrical_val, second_electrical_val, electrical_units,
            first_physical_val, second_physical_val, physical_units,
            custom_scale_name):
        response = self._invoke(
            self._client.CreateAIForceBridgeTwoPointLinChan,
            grpc_types.CreateAIForceBridgeTwoPointLinChanRequest(
                task=task, physical_channel=physical_channel,
                name_to_assign_to_channel=name_to_assign_to_channel,
                min_val=min_val, max_val=max_val, units_raw=units,
                bridge_config_raw=bridge_config,
                voltage_excit_source_raw=voltage_excit_source,
                voltage_excit_val=voltage_excit_val,
                nominal_bridge_resistance=nominal_bridge_resistance,
                first_electrical_val=first_electrical_val,
                second_electrical_val=second_electrical_val,
                electrical_units_raw=electrical_units,
                first_physical_val=first_physical_val,
                second_physical_val=second_physical_val,
                physical_units_raw=physical_units,
                custom_scale_name=custom_scale_name))

    def create_ai_force_iepe_chan(
            self, task, physical_channel, name_to_assign_to_channel,
            terminal_config, min_val, max_val, units, sensitivity,
            sensitivity_units, current_excit_source, current_excit_val,
            custom_scale_name):
        response = self._invoke(
            self._client.CreateAIForceIEPEChan,
            grpc_types.CreateAIForceIEPEChanRequest(
                task=task, physical_channel=physical_channel,
                name_to_assign_to_channel=name_to_assign_to_channel,
                terminal_config_raw=terminal_config, min_val=min_val,
                max_val=max_val, units_raw=units, sensitivity=sensitivity,
                sensitivity_units_raw=sensitivity_units,
                current_excit_source_raw=current_excit_source,
                current_excit_val=current_excit_val,
                custom_scale_name=custom_scale_name))

    def create_ai_freq_voltage_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, threshold_level, hysteresis, custom_scale_name):
        response = self._invoke(
            self._client.CreateAIFreqVoltageChan,
            grpc_types.CreateAIFreqVoltageChanRequest(
                task=task, physical_channel=physical_channel,
                name_to_assign_to_channel=name_to_assign_to_channel,
                min_val=min_val, max_val=max_val, units_raw=units,
                threshold_level=threshold_level, hysteresis=hysteresis,
                custom_scale_name=custom_scale_name))

    def create_ai_microphone_chan(
            self, task, physical_channel, name_to_assign_to_channel,
            terminal_config, units, mic_sensitivity, max_snd_press_level,
            current_excit_source, current_excit_val, custom_scale_name):
        response = self._invoke(
            self._client.CreateAIMicrophoneChan,
            grpc_types.CreateAIMicrophoneChanRequest(
                task=task, physical_channel=physical_channel,
                name_to_assign_to_channel=name_to_assign_to_channel,
                terminal_config_raw=terminal_config, units_raw=units,
                mic_sensitivity=mic_sensitivity,
                max_snd_press_level=max_snd_press_level,
                current_excit_source_raw=current_excit_source,
                current_excit_val=current_excit_val,
                custom_scale_name=custom_scale_name))

    def create_ai_pos_eddy_curr_prox_probe_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, sensitivity, sensitivity_units,
            custom_scale_name):
        response = self._invoke(
            self._client.CreateAIPosEddyCurrProxProbeChan,
            grpc_types.CreateAIPosEddyCurrProxProbeChanRequest(
                task=task, physical_channel=physical_channel,
                name_to_assign_to_channel=name_to_assign_to_channel,
                min_val=min_val, max_val=max_val, units_raw=units,
                sensitivity=sensitivity,
                sensitivity_units_raw=sensitivity_units,
                custom_scale_name=custom_scale_name))

    def create_ai_pos_lvdt_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, sensitivity, sensitivity_units,
            voltage_excit_source, voltage_excit_val, voltage_excit_freq,
            ac_excit_wire_mode, custom_scale_name):
        response = self._invoke(
            self._client.CreateAIPosLVDTChan,
            grpc_types.CreateAIPosLVDTChanRequest(
                task=task, physical_channel=physical_channel,
                name_to_assign_to_channel=name_to_assign_to_channel,
                min_val=min_val, max_val=max_val, units_raw=units,
                sensitivity=sensitivity,
                sensitivity_units_raw=sensitivity_units,
                voltage_excit_source_raw=voltage_excit_source,
                voltage_excit_val=voltage_excit_val,
                voltage_excit_freq=voltage_excit_freq,
                ac_excit_wire_mode_raw=ac_excit_wire_mode,
                custom_scale_name=custom_scale_name))

    def create_ai_pos_rvdt_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, sensitivity, sensitivity_units,
            voltage_excit_source, voltage_excit_val, voltage_excit_freq,
            ac_excit_wire_mode, custom_scale_name):
        response = self._invoke(
            self._client.CreateAIPosRVDTChan,
            grpc_types.CreateAIPosRVDTChanRequest(
                task=task, physical_channel=physical_channel,
                name_to_assign_to_channel=name_to_assign_to_channel,
                min_val=min_val, max_val=max_val, units_raw=units,
                sensitivity=sensitivity,
                sensitivity_units_raw=sensitivity_units,
                voltage_excit_source_raw=voltage_excit_source,
                voltage_excit_val=voltage_excit_val,
                voltage_excit_freq=voltage_excit_freq,
                ac_excit_wire_mode_raw=ac_excit_wire_mode,
                custom_scale_name=custom_scale_name))

    def create_ai_power_chan(
            self, task, physical_channel, voltage_setpoint, current_setpoint,
            output_enable, name_to_assign_to_channel):
        response = self._invoke(
            self._client.CreateAIPowerChan,
            grpc_types.CreateAIPowerChanRequest(
                task=task, physical_channel=physical_channel,
                voltage_setpoint=voltage_setpoint,
                current_setpoint=current_setpoint,
                output_enable=output_enable,
                name_to_assign_to_channel=name_to_assign_to_channel))

    def create_ai_pressure_bridge_polynomial_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, bridge_config, voltage_excit_source,
            voltage_excit_val, nominal_bridge_resistance, forward_coeffs,
            reverse_coeffs, electrical_units, physical_units,
            custom_scale_name):
        response = self._invoke(
            self._client.CreateAIPressureBridgePolynomialChan,
            grpc_types.CreateAIPressureBridgePolynomialChanRequest(
                task=task, physical_channel=physical_channel,
                name_to_assign_to_channel=name_to_assign_to_channel,
                min_val=min_val, max_val=max_val, units_raw=units,
                bridge_config_raw=bridge_config,
                voltage_excit_source_raw=voltage_excit_source,
                voltage_excit_val=voltage_excit_val,
                nominal_bridge_resistance=nominal_bridge_resistance,
                forward_coeffs=forward_coeffs, reverse_coeffs=reverse_coeffs,
                electrical_units_raw=electrical_units,
                physical_units_raw=physical_units,
                custom_scale_name=custom_scale_name))

    def create_ai_pressure_bridge_table_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, bridge_config, voltage_excit_source,
            voltage_excit_val, nominal_bridge_resistance, electrical_vals,
            electrical_units, physical_vals, physical_units,
            custom_scale_name):
        response = self._invoke(
            self._client.CreateAIPressureBridgeTableChan,
            grpc_types.CreateAIPressureBridgeTableChanRequest(
                task=task, physical_channel=physical_channel,
                name_to_assign_to_channel=name_to_assign_to_channel,
                min_val=min_val, max_val=max_val, units_raw=units,
                bridge_config_raw=bridge_config,
                voltage_excit_source_raw=voltage_excit_source,
                voltage_excit_val=voltage_excit_val,
                nominal_bridge_resistance=nominal_bridge_resistance,
                electrical_vals=electrical_vals,
                electrical_units_raw=electrical_units,
                physical_vals=physical_vals,
                physical_units_raw=physical_units,
                custom_scale_name=custom_scale_name))

    def create_ai_pressure_bridge_two_point_lin_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, bridge_config, voltage_excit_source,
            voltage_excit_val, nominal_bridge_resistance,
            first_electrical_val, second_electrical_val, electrical_units,
            first_physical_val, second_physical_val, physical_units,
            custom_scale_name):
        response = self._invoke(
            self._client.CreateAIPressureBridgeTwoPointLinChan,
            grpc_types.CreateAIPressureBridgeTwoPointLinChanRequest(
                task=task, physical_channel=physical_channel,
                name_to_assign_to_channel=name_to_assign_to_channel,
                min_val=min_val, max_val=max_val, units_raw=units,
                bridge_config_raw=bridge_config,
                voltage_excit_source_raw=voltage_excit_source,
                voltage_excit_val=voltage_excit_val,
                nominal_bridge_resistance=nominal_bridge_resistance,
                first_electrical_val=first_electrical_val,
                second_electrical_val=second_electrical_val,
                electrical_units_raw=electrical_units,
                first_physical_val=first_physical_val,
                second_physical_val=second_physical_val,
                physical_units_raw=physical_units,
                custom_scale_name=custom_scale_name))

    def create_ai_resistance_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, resistance_config, current_excit_source,
            current_excit_val, custom_scale_name):
        response = self._invoke(
            self._client.CreateAIResistanceChan,
            grpc_types.CreateAIResistanceChanRequest(
                task=task, physical_channel=physical_channel,
                name_to_assign_to_channel=name_to_assign_to_channel,
                min_val=min_val, max_val=max_val, units_raw=units,
                resistance_config_raw=resistance_config,
                current_excit_source_raw=current_excit_source,
                current_excit_val=current_excit_val,
                custom_scale_name=custom_scale_name))

    def create_ai_rosette_strain_gage_chan(
            self, task, physical_channel, rosette_type, gage_orientation,
            rosette_meas_types, name_to_assign_to_channel, min_val, max_val,
            strain_config, voltage_excit_source, voltage_excit_val,
            gage_factor, nominal_gage_resistance, poisson_ratio,
            lead_wire_resistance):
        response = self._invoke(
            self._client.CreateAIRosetteStrainGageChan,
            grpc_types.CreateAIRosetteStrainGageChanRequest(
                task=task, physical_channel=physical_channel,
                rosette_type_raw=rosette_type,
                gage_orientation=gage_orientation,
                rosette_meas_types=rosette_meas_types,
                name_to_assign_to_channel=name_to_assign_to_channel,
                min_val=min_val, max_val=max_val,
                strain_config_raw=strain_config,
                voltage_excit_source_raw=voltage_excit_source,
                voltage_excit_val=voltage_excit_val, gage_factor=gage_factor,
                nominal_gage_resistance=nominal_gage_resistance,
                poisson_ratio=poisson_ratio,
                lead_wire_resistance=lead_wire_resistance))

    def create_ai_strain_gage_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, strain_config, voltage_excit_source,
            voltage_excit_val, gage_factor, initial_bridge_voltage,
            nominal_gage_resistance, poisson_ratio, lead_wire_resistance,
            custom_scale_name):
        response = self._invoke(
            self._client.CreateAIStrainGageChan,
            grpc_types.CreateAIStrainGageChanRequest(
                task=task, physical_channel=physical_channel,
                name_to_assign_to_channel=name_to_assign_to_channel,
                min_val=min_val, max_val=max_val, units_raw=units,
                strain_config_raw=strain_config,
                voltage_excit_source_raw=voltage_excit_source,
                voltage_excit_val=voltage_excit_val, gage_factor=gage_factor,
                initial_bridge_voltage=initial_bridge_voltage,
                nominal_gage_resistance=nominal_gage_resistance,
                poisson_ratio=poisson_ratio,
                lead_wire_resistance=lead_wire_resistance,
                custom_scale_name=custom_scale_name))

    def create_ai_temp_built_in_sensor_chan(
            self, task, physical_channel, name_to_assign_to_channel, units):
        response = self._invoke(
            self._client.CreateAITempBuiltInSensorChan,
            grpc_types.CreateAITempBuiltInSensorChanRequest(
                task=task, physical_channel=physical_channel,
                name_to_assign_to_channel=name_to_assign_to_channel,
                units_raw=units))

    def create_ai_thrmcpl_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, thermocouple_type, cjc_source, cjc_val,
            cjc_channel):
        response = self._invoke(
            self._client.CreateAIThrmcplChan,
            grpc_types.CreateAIThrmcplChanRequest(
                task=task, physical_channel=physical_channel,
                name_to_assign_to_channel=name_to_assign_to_channel,
                min_val=min_val, max_val=max_val, units_raw=units,
                thermocouple_type_raw=thermocouple_type,
                cjc_source_raw=cjc_source, cjc_val=cjc_val,
                cjc_channel=cjc_channel))

    def create_ai_thrmstr_chan_iex(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, resistance_config, current_excit_source,
            current_excit_val, a, b, c):
        response = self._invoke(
            self._client.CreateAIThrmstrChanIex,
            grpc_types.CreateAIThrmstrChanIexRequest(
                task=task, physical_channel=physical_channel,
                name_to_assign_to_channel=name_to_assign_to_channel,
                min_val=min_val, max_val=max_val, units_raw=units,
                resistance_config_raw=resistance_config,
                current_excit_source_raw=current_excit_source,
                current_excit_val=current_excit_val, a=a, b=b, c=c))

    def create_ai_thrmstr_chan_vex(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, resistance_config, voltage_excit_source,
            voltage_excit_val, a, b, c, r_1):
        response = self._invoke(
            self._client.CreateAIThrmstrChanVex,
            grpc_types.CreateAIThrmstrChanVexRequest(
                task=task, physical_channel=physical_channel,
                name_to_assign_to_channel=name_to_assign_to_channel,
                min_val=min_val, max_val=max_val, units_raw=units,
                resistance_config_raw=resistance_config,
                voltage_excit_source_raw=voltage_excit_source,
                voltage_excit_val=voltage_excit_val, a=a, b=b, c=c, r1=r_1))

    def create_ai_torque_bridge_polynomial_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, bridge_config, voltage_excit_source,
            voltage_excit_val, nominal_bridge_resistance, forward_coeffs,
            reverse_coeffs, electrical_units, physical_units,
            custom_scale_name):
        response = self._invoke(
            self._client.CreateAITorqueBridgePolynomialChan,
            grpc_types.CreateAITorqueBridgePolynomialChanRequest(
                task=task, physical_channel=physical_channel,
                name_to_assign_to_channel=name_to_assign_to_channel,
                min_val=min_val, max_val=max_val, units_raw=units,
                bridge_config_raw=bridge_config,
                voltage_excit_source_raw=voltage_excit_source,
                voltage_excit_val=voltage_excit_val,
                nominal_bridge_resistance=nominal_bridge_resistance,
                forward_coeffs=forward_coeffs, reverse_coeffs=reverse_coeffs,
                electrical_units_raw=electrical_units,
                physical_units_raw=physical_units,
                custom_scale_name=custom_scale_name))

    def create_ai_torque_bridge_table_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, bridge_config, voltage_excit_source,
            voltage_excit_val, nominal_bridge_resistance, electrical_vals,
            electrical_units, physical_vals, physical_units,
            custom_scale_name):
        response = self._invoke(
            self._client.CreateAITorqueBridgeTableChan,
            grpc_types.CreateAITorqueBridgeTableChanRequest(
                task=task, physical_channel=physical_channel,
                name_to_assign_to_channel=name_to_assign_to_channel,
                min_val=min_val, max_val=max_val, units_raw=units,
                bridge_config_raw=bridge_config,
                voltage_excit_source_raw=voltage_excit_source,
                voltage_excit_val=voltage_excit_val,
                nominal_bridge_resistance=nominal_bridge_resistance,
                electrical_vals=electrical_vals,
                electrical_units_raw=electrical_units,
                physical_vals=physical_vals,
                physical_units_raw=physical_units,
                custom_scale_name=custom_scale_name))

    def create_ai_torque_bridge_two_point_lin_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, bridge_config, voltage_excit_source,
            voltage_excit_val, nominal_bridge_resistance,
            first_electrical_val, second_electrical_val, electrical_units,
            first_physical_val, second_physical_val, physical_units,
            custom_scale_name):
        response = self._invoke(
            self._client.CreateAITorqueBridgeTwoPointLinChan,
            grpc_types.CreateAITorqueBridgeTwoPointLinChanRequest(
                task=task, physical_channel=physical_channel,
                name_to_assign_to_channel=name_to_assign_to_channel,
                min_val=min_val, max_val=max_val, units_raw=units,
                bridge_config_raw=bridge_config,
                voltage_excit_source_raw=voltage_excit_source,
                voltage_excit_val=voltage_excit_val,
                nominal_bridge_resistance=nominal_bridge_resistance,
                first_electrical_val=first_electrical_val,
                second_electrical_val=second_electrical_val,
                electrical_units_raw=electrical_units,
                first_physical_val=first_physical_val,
                second_physical_val=second_physical_val,
                physical_units_raw=physical_units,
                custom_scale_name=custom_scale_name))

    def create_ai_velocity_iepe_chan(
            self, task, physical_channel, name_to_assign_to_channel,
            terminal_config, min_val, max_val, units, sensitivity,
            sensitivity_units, current_excit_source, current_excit_val,
            custom_scale_name):
        response = self._invoke(
            self._client.CreateAIVelocityIEPEChan,
            grpc_types.CreateAIVelocityIEPEChanRequest(
                task=task, physical_channel=physical_channel,
                name_to_assign_to_channel=name_to_assign_to_channel,
                terminal_config_raw=terminal_config, min_val=min_val,
                max_val=max_val, units_raw=units, sensitivity=sensitivity,
                sensitivity_units_raw=sensitivity_units,
                current_excit_source_raw=current_excit_source,
                current_excit_val=current_excit_val,
                custom_scale_name=custom_scale_name))

    def create_ai_voltage_chan(
            self, task, physical_channel, name_to_assign_to_channel,
            terminal_config, min_val, max_val, units, custom_scale_name):
        response = self._invoke(
            self._client.CreateAIVoltageChan,
            grpc_types.CreateAIVoltageChanRequest(
                task=task, physical_channel=physical_channel,
                name_to_assign_to_channel=name_to_assign_to_channel,
                terminal_config_raw=terminal_config, min_val=min_val,
                max_val=max_val, units_raw=units,
                custom_scale_name=custom_scale_name))

    def create_ai_voltage_chan_with_excit(
            self, task, physical_channel, name_to_assign_to_channel,
            terminal_config, min_val, max_val, units, bridge_config,
            voltage_excit_source, voltage_excit_val, use_excit_for_scaling,
            custom_scale_name):
        response = self._invoke(
            self._client.CreateAIVoltageChanWithExcit,
            grpc_types.CreateAIVoltageChanWithExcitRequest(
                task=task, physical_channel=physical_channel,
                name_to_assign_to_channel=name_to_assign_to_channel,
                terminal_config_raw=terminal_config, min_val=min_val,
                max_val=max_val, units_raw=units,
                bridge_config_raw=bridge_config,
                voltage_excit_source_raw=voltage_excit_source,
                voltage_excit_val=voltage_excit_val,
                use_excit_for_scaling=use_excit_for_scaling,
                custom_scale_name=custom_scale_name))

    def create_ai_voltage_rms_chan(
            self, task, physical_channel, name_to_assign_to_channel,
            terminal_config, min_val, max_val, units, custom_scale_name):
        response = self._invoke(
            self._client.CreateAIVoltageRMSChan,
            grpc_types.CreateAIVoltageRMSChanRequest(
                task=task, physical_channel=physical_channel,
                name_to_assign_to_channel=name_to_assign_to_channel,
                terminal_config_raw=terminal_config, min_val=min_val,
                max_val=max_val, units_raw=units,
                custom_scale_name=custom_scale_name))

    def create_airtd_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, rtd_type, resistance_config, current_excit_source,
            current_excit_val, r_0):
        response = self._invoke(
            self._client.CreateAIRTDChan,
            grpc_types.CreateAIRTDChanRequest(
                task=task, physical_channel=physical_channel,
                name_to_assign_to_channel=name_to_assign_to_channel,
                min_val=min_val, max_val=max_val, units_raw=units,
                rtd_type_raw=rtd_type,
                resistance_config_raw=resistance_config,
                current_excit_source_raw=current_excit_source,
                current_excit_val=current_excit_val, r0=r_0))

    def create_ao_current_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, custom_scale_name):
        response = self._invoke(
            self._client.CreateAOCurrentChan,
            grpc_types.CreateAOCurrentChanRequest(
                task=task, physical_channel=physical_channel,
                name_to_assign_to_channel=name_to_assign_to_channel,
                min_val=min_val, max_val=max_val, units_raw=units,
                custom_scale_name=custom_scale_name))

    def create_ao_func_gen_chan(
            self, task, physical_channel, name_to_assign_to_channel, type,
            freq, amplitude, offset):
        response = self._invoke(
            self._client.CreateAOFuncGenChan,
            grpc_types.CreateAOFuncGenChanRequest(
                task=task, physical_channel=physical_channel,
                name_to_assign_to_channel=name_to_assign_to_channel,
                type_raw=type, freq=freq, amplitude=amplitude, offset=offset))

    def create_ao_voltage_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, custom_scale_name):
        response = self._invoke(
            self._client.CreateAOVoltageChan,
            grpc_types.CreateAOVoltageChanRequest(
                task=task, physical_channel=physical_channel,
                name_to_assign_to_channel=name_to_assign_to_channel,
                min_val=min_val, max_val=max_val, units_raw=units,
                custom_scale_name=custom_scale_name))

    def create_ci_ang_encoder_chan(
            self, task, counter, name_to_assign_to_channel, decoding_type,
            zidx_enable, zidx_val, zidx_phase, units, pulses_per_rev,
            initial_angle, custom_scale_name):
        response = self._invoke(
            self._client.CreateCIAngEncoderChan,
            grpc_types.CreateCIAngEncoderChanRequest(
                task=task, counter=counter,
                name_to_assign_to_channel=name_to_assign_to_channel,
                decoding_type_raw=decoding_type, zidx_enable=zidx_enable,
                zidx_val=zidx_val, zidx_phase_raw=zidx_phase, units_raw=units,
                pulses_per_rev=pulses_per_rev, initial_angle=initial_angle,
                custom_scale_name=custom_scale_name))

    def create_ci_ang_velocity_chan(
            self, task, counter, name_to_assign_to_channel, min_val, max_val,
            decoding_type, units, pulses_per_rev, custom_scale_name):
        response = self._invoke(
            self._client.CreateCIAngVelocityChan,
            grpc_types.CreateCIAngVelocityChanRequest(
                task=task, counter=counter,
                name_to_assign_to_channel=name_to_assign_to_channel,
                min_val=min_val, max_val=max_val,
                decoding_type_raw=decoding_type, units_raw=units,
                pulses_per_rev=pulses_per_rev,
                custom_scale_name=custom_scale_name))

    def create_ci_count_edges_chan(
            self, task, counter, name_to_assign_to_channel, edge,
            initial_count, count_direction):
        response = self._invoke(
            self._client.CreateCICountEdgesChan,
            grpc_types.CreateCICountEdgesChanRequest(
                task=task, counter=counter,
                name_to_assign_to_channel=name_to_assign_to_channel,
                edge_raw=edge, initial_count=initial_count,
                count_direction_raw=count_direction))

    def create_ci_duty_cycle_chan(
            self, task, counter, name_to_assign_to_channel, min_freq,
            max_freq, edge, custom_scale_name):
        response = self._invoke(
            self._client.CreateCIDutyCycleChan,
            grpc_types.CreateCIDutyCycleChanRequest(
                task=task, counter=counter,
                name_to_assign_to_channel=name_to_assign_to_channel,
                min_freq=min_freq, max_freq=max_freq, edge_raw=edge,
                custom_scale_name=custom_scale_name))

    def create_ci_freq_chan(
            self, task, counter, name_to_assign_to_channel, min_val, max_val,
            units, edge, meas_method, meas_time, divisor, custom_scale_name):
        response = self._invoke(
            self._client.CreateCIFreqChan,
            grpc_types.CreateCIFreqChanRequest(
                task=task, counter=counter,
                name_to_assign_to_channel=name_to_assign_to_channel,
                min_val=min_val, max_val=max_val, units_raw=units,
                edge_raw=edge, meas_method_raw=meas_method,
                meas_time=meas_time, divisor=divisor,
                custom_scale_name=custom_scale_name))

    def create_ci_lin_encoder_chan(
            self, task, counter, name_to_assign_to_channel, decoding_type,
            zidx_enable, zidx_val, zidx_phase, units, dist_per_pulse,
            initial_pos, custom_scale_name):
        response = self._invoke(
            self._client.CreateCILinEncoderChan,
            grpc_types.CreateCILinEncoderChanRequest(
                task=task, counter=counter,
                name_to_assign_to_channel=name_to_assign_to_channel,
                decoding_type_raw=decoding_type, zidx_enable=zidx_enable,
                zidx_val=zidx_val, zidx_phase_raw=zidx_phase, units_raw=units,
                dist_per_pulse=dist_per_pulse, initial_pos=initial_pos,
                custom_scale_name=custom_scale_name))

    def create_ci_lin_velocity_chan(
            self, task, counter, name_to_assign_to_channel, min_val, max_val,
            decoding_type, units, dist_per_pulse, custom_scale_name):
        response = self._invoke(
            self._client.CreateCILinVelocityChan,
            grpc_types.CreateCILinVelocityChanRequest(
                task=task, counter=counter,
                name_to_assign_to_channel=name_to_assign_to_channel,
                min_val=min_val, max_val=max_val,
                decoding_type_raw=decoding_type, units_raw=units,
                dist_per_pulse=dist_per_pulse,
                custom_scale_name=custom_scale_name))

    def create_ci_period_chan(
            self, task, counter, name_to_assign_to_channel, min_val, max_val,
            units, edge, meas_method, meas_time, divisor, custom_scale_name):
        response = self._invoke(
            self._client.CreateCIPeriodChan,
            grpc_types.CreateCIPeriodChanRequest(
                task=task, counter=counter,
                name_to_assign_to_channel=name_to_assign_to_channel,
                min_val=min_val, max_val=max_val, units_raw=units,
                edge_raw=edge, meas_method_raw=meas_method,
                meas_time=meas_time, divisor=divisor,
                custom_scale_name=custom_scale_name))

    def create_ci_pulse_chan_freq(
            self, task, counter, name_to_assign_to_channel, min_val, max_val,
            units):
        response = self._invoke(
            self._client.CreateCIPulseChanFreq,
            grpc_types.CreateCIPulseChanFreqRequest(
                task=task, counter=counter,
                name_to_assign_to_channel=name_to_assign_to_channel,
                min_val=min_val, max_val=max_val, units_raw=units))

    def create_ci_pulse_chan_ticks(
            self, task, counter, name_to_assign_to_channel, source_terminal,
            min_val, max_val):
        response = self._invoke(
            self._client.CreateCIPulseChanTicks,
            grpc_types.CreateCIPulseChanTicksRequest(
                task=task, counter=counter,
                name_to_assign_to_channel=name_to_assign_to_channel,
                source_terminal=source_terminal, min_val=min_val,
                max_val=max_val))

    def create_ci_pulse_chan_time(
            self, task, counter, name_to_assign_to_channel, min_val, max_val,
            units):
        response = self._invoke(
            self._client.CreateCIPulseChanTime,
            grpc_types.CreateCIPulseChanTimeRequest(
                task=task, counter=counter,
                name_to_assign_to_channel=name_to_assign_to_channel,
                min_val=min_val, max_val=max_val, units_raw=units))

    def create_ci_pulse_width_chan(
            self, task, counter, name_to_assign_to_channel, min_val, max_val,
            units, starting_edge, custom_scale_name):
        response = self._invoke(
            self._client.CreateCIPulseWidthChan,
            grpc_types.CreateCIPulseWidthChanRequest(
                task=task, counter=counter,
                name_to_assign_to_channel=name_to_assign_to_channel,
                min_val=min_val, max_val=max_val, units_raw=units,
                starting_edge_raw=starting_edge,
                custom_scale_name=custom_scale_name))

    def create_ci_semi_period_chan(
            self, task, counter, name_to_assign_to_channel, min_val, max_val,
            units, custom_scale_name):
        response = self._invoke(
            self._client.CreateCISemiPeriodChan,
            grpc_types.CreateCISemiPeriodChanRequest(
                task=task, counter=counter,
                name_to_assign_to_channel=name_to_assign_to_channel,
                min_val=min_val, max_val=max_val, units_raw=units,
                custom_scale_name=custom_scale_name))

    def create_ci_two_edge_sep_chan(
            self, task, counter, name_to_assign_to_channel, min_val, max_val,
            units, first_edge, second_edge, custom_scale_name):
        response = self._invoke(
            self._client.CreateCITwoEdgeSepChan,
            grpc_types.CreateCITwoEdgeSepChanRequest(
                task=task, counter=counter,
                name_to_assign_to_channel=name_to_assign_to_channel,
                min_val=min_val, max_val=max_val, units_raw=units,
                first_edge_raw=first_edge, second_edge_raw=second_edge,
                custom_scale_name=custom_scale_name))

    def create_cigps_timestamp_chan(
            self, task, counter, name_to_assign_to_channel, units,
            sync_method, custom_scale_name):
        response = self._invoke(
            self._client.CreateCIGPSTimestampChan,
            grpc_types.CreateCIGPSTimestampChanRequest(
                task=task, counter=counter,
                name_to_assign_to_channel=name_to_assign_to_channel,
                units_raw=units, sync_method_raw=sync_method,
                custom_scale_name=custom_scale_name))

    def create_co_pulse_chan_freq(
            self, task, counter, name_to_assign_to_channel, units, idle_state,
            initial_delay, freq, duty_cycle):
        response = self._invoke(
            self._client.CreateCOPulseChanFreq,
            grpc_types.CreateCOPulseChanFreqRequest(
                task=task, counter=counter,
                name_to_assign_to_channel=name_to_assign_to_channel,
                units_raw=units, idle_state_raw=idle_state,
                initial_delay=initial_delay, freq=freq, duty_cycle=duty_cycle))

    def create_co_pulse_chan_ticks(
            self, task, counter, source_terminal, name_to_assign_to_channel,
            idle_state, initial_delay, low_ticks, high_ticks):
        response = self._invoke(
            self._client.CreateCOPulseChanTicks,
            grpc_types.CreateCOPulseChanTicksRequest(
                task=task, counter=counter, source_terminal=source_terminal,
                name_to_assign_to_channel=name_to_assign_to_channel,
                idle_state_raw=idle_state, initial_delay=initial_delay,
                low_ticks=low_ticks, high_ticks=high_ticks))

    def create_co_pulse_chan_time(
            self, task, counter, name_to_assign_to_channel, units, idle_state,
            initial_delay, low_time, high_time):
        response = self._invoke(
            self._client.CreateCOPulseChanTime,
            grpc_types.CreateCOPulseChanTimeRequest(
                task=task, counter=counter,
                name_to_assign_to_channel=name_to_assign_to_channel,
                units_raw=units, idle_state_raw=idle_state,
                initial_delay=initial_delay, low_time=low_time,
                high_time=high_time))

    def create_di_chan(
            self, task, lines, name_to_assign_to_lines, line_grouping):
        response = self._invoke(
            self._client.CreateDIChan,
            grpc_types.CreateDIChanRequest(
                task=task, lines=lines,
                name_to_assign_to_lines=name_to_assign_to_lines,
                line_grouping_raw=line_grouping))

    def create_do_chan(
            self, task, lines, name_to_assign_to_lines, line_grouping):
        response = self._invoke(
            self._client.CreateDOChan,
            grpc_types.CreateDOChanRequest(
                task=task, lines=lines,
                name_to_assign_to_lines=name_to_assign_to_lines,
                line_grouping_raw=line_grouping))

    def create_lin_scale(
            self, name, slope, y_intercept, pre_scaled_units, scaled_units):
        response = self._invoke(
            self._client.CreateLinScale,
            grpc_types.CreateLinScaleRequest(
                name=name, slope=slope, y_intercept=y_intercept,
                pre_scaled_units_raw=pre_scaled_units,
                scaled_units=scaled_units))

    def create_map_scale(
            self, name, prescaled_min, prescaled_max, scaled_min, scaled_max,
            pre_scaled_units, scaled_units):
        response = self._invoke(
            self._client.CreateMapScale,
            grpc_types.CreateMapScaleRequest(
                name=name, prescaled_min=prescaled_min,
                prescaled_max=prescaled_max, scaled_min=scaled_min,
                scaled_max=scaled_max, pre_scaled_units_raw=pre_scaled_units,
                scaled_units=scaled_units))

    def create_polynomial_scale(
            self, name, forward_coeffs, reverse_coeffs, pre_scaled_units,
            scaled_units):
        response = self._invoke(
            self._client.CreatePolynomialScale,
            grpc_types.CreatePolynomialScaleRequest(
                name=name, forward_coeffs=forward_coeffs,
                reverse_coeffs=reverse_coeffs,
                pre_scaled_units_raw=pre_scaled_units,
                scaled_units=scaled_units))

    def create_table_scale(
            self, name, prescaled_vals, scaled_vals, pre_scaled_units,
            scaled_units):
        response = self._invoke(
            self._client.CreateTableScale,
            grpc_types.CreateTableScaleRequest(
                name=name, prescaled_vals=prescaled_vals,
                scaled_vals=scaled_vals,
                pre_scaled_units_raw=pre_scaled_units,
                scaled_units=scaled_units))

    def create_task(self, session_name):
        metadata = (
            ('ni-api-key', self._grpc_options.api_key),
        )
        response = self._invoke(
            self._client.CreateTask,
            grpc_types.CreateTaskRequest(
                session_name=session_name,
                initialization_behavior=self._grpc_options.initialization_behavior),
            metadata=metadata)
        return response.task, response.new_session_initialized

    def create_tedsai_accel_chan(
            self, task, physical_channel, name_to_assign_to_channel,
            terminal_config, min_val, max_val, units, current_excit_source,
            current_excit_val, custom_scale_name):
        response = self._invoke(
            self._client.CreateTEDSAIAccelChan,
            grpc_types.CreateTEDSAIAccelChanRequest(
                task=task, physical_channel=physical_channel,
                name_to_assign_to_channel=name_to_assign_to_channel,
                terminal_config_raw=terminal_config, min_val=min_val,
                max_val=max_val, units_raw=units,
                current_excit_source_raw=current_excit_source,
                current_excit_val=current_excit_val,
                custom_scale_name=custom_scale_name))

    def create_tedsai_bridge_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, voltage_excit_source, voltage_excit_val,
            custom_scale_name):
        response = self._invoke(
            self._client.CreateTEDSAIBridgeChan,
            grpc_types.CreateTEDSAIBridgeChanRequest(
                task=task, physical_channel=physical_channel,
                name_to_assign_to_channel=name_to_assign_to_channel,
                min_val=min_val, max_val=max_val, units_raw=units,
                voltage_excit_source_raw=voltage_excit_source,
                voltage_excit_val=voltage_excit_val,
                custom_scale_name=custom_scale_name))

    def create_tedsai_current_chan(
            self, task, physical_channel, name_to_assign_to_channel,
            terminal_config, min_val, max_val, units, shunt_resistor_loc,
            ext_shunt_resistor_val, custom_scale_name):
        response = self._invoke(
            self._client.CreateTEDSAICurrentChan,
            grpc_types.CreateTEDSAICurrentChanRequest(
                task=task, physical_channel=physical_channel,
                name_to_assign_to_channel=name_to_assign_to_channel,
                terminal_config_raw=terminal_config, min_val=min_val,
                max_val=max_val, units_raw=units,
                shunt_resistor_loc_raw=shunt_resistor_loc,
                ext_shunt_resistor_val=ext_shunt_resistor_val,
                custom_scale_name=custom_scale_name))

    def create_tedsai_force_bridge_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, voltage_excit_source, voltage_excit_val,
            custom_scale_name):
        response = self._invoke(
            self._client.CreateTEDSAIForceBridgeChan,
            grpc_types.CreateTEDSAIForceBridgeChanRequest(
                task=task, physical_channel=physical_channel,
                name_to_assign_to_channel=name_to_assign_to_channel,
                min_val=min_val, max_val=max_val, units_raw=units,
                voltage_excit_source_raw=voltage_excit_source,
                voltage_excit_val=voltage_excit_val,
                custom_scale_name=custom_scale_name))

    def create_tedsai_force_iepe_chan(
            self, task, physical_channel, name_to_assign_to_channel,
            terminal_config, min_val, max_val, units, current_excit_source,
            current_excit_val, custom_scale_name):
        response = self._invoke(
            self._client.CreateTEDSAIForceIEPEChan,
            grpc_types.CreateTEDSAIForceIEPEChanRequest(
                task=task, physical_channel=physical_channel,
                name_to_assign_to_channel=name_to_assign_to_channel,
                terminal_config_raw=terminal_config, min_val=min_val,
                max_val=max_val, units_raw=units,
                current_excit_source_raw=current_excit_source,
                current_excit_val=current_excit_val,
                custom_scale_name=custom_scale_name))

    def create_tedsai_microphone_chan(
            self, task, physical_channel, name_to_assign_to_channel,
            terminal_config, units, max_snd_press_level, current_excit_source,
            current_excit_val, custom_scale_name):
        response = self._invoke(
            self._client.CreateTEDSAIMicrophoneChan,
            grpc_types.CreateTEDSAIMicrophoneChanRequest(
                task=task, physical_channel=physical_channel,
                name_to_assign_to_channel=name_to_assign_to_channel,
                terminal_config_raw=terminal_config, units_raw=units,
                max_snd_press_level=max_snd_press_level,
                current_excit_source_raw=current_excit_source,
                current_excit_val=current_excit_val,
                custom_scale_name=custom_scale_name))

    def create_tedsai_pos_lvdt_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, voltage_excit_source, voltage_excit_val,
            voltage_excit_freq, ac_excit_wire_mode, custom_scale_name):
        response = self._invoke(
            self._client.CreateTEDSAIPosLVDTChan,
            grpc_types.CreateTEDSAIPosLVDTChanRequest(
                task=task, physical_channel=physical_channel,
                name_to_assign_to_channel=name_to_assign_to_channel,
                min_val=min_val, max_val=max_val, units_raw=units,
                voltage_excit_source_raw=voltage_excit_source,
                voltage_excit_val=voltage_excit_val,
                voltage_excit_freq=voltage_excit_freq,
                ac_excit_wire_mode_raw=ac_excit_wire_mode,
                custom_scale_name=custom_scale_name))

    def create_tedsai_pos_rvdt_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, voltage_excit_source, voltage_excit_val,
            voltage_excit_freq, ac_excit_wire_mode, custom_scale_name):
        response = self._invoke(
            self._client.CreateTEDSAIPosRVDTChan,
            grpc_types.CreateTEDSAIPosRVDTChanRequest(
                task=task, physical_channel=physical_channel,
                name_to_assign_to_channel=name_to_assign_to_channel,
                min_val=min_val, max_val=max_val, units_raw=units,
                voltage_excit_source_raw=voltage_excit_source,
                voltage_excit_val=voltage_excit_val,
                voltage_excit_freq=voltage_excit_freq,
                ac_excit_wire_mode_raw=ac_excit_wire_mode,
                custom_scale_name=custom_scale_name))

    def create_tedsai_pressure_bridge_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, voltage_excit_source, voltage_excit_val,
            custom_scale_name):
        response = self._invoke(
            self._client.CreateTEDSAIPressureBridgeChan,
            grpc_types.CreateTEDSAIPressureBridgeChanRequest(
                task=task, physical_channel=physical_channel,
                name_to_assign_to_channel=name_to_assign_to_channel,
                min_val=min_val, max_val=max_val, units_raw=units,
                voltage_excit_source_raw=voltage_excit_source,
                voltage_excit_val=voltage_excit_val,
                custom_scale_name=custom_scale_name))

    def create_tedsai_resistance_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, resistance_config, current_excit_source,
            current_excit_val, custom_scale_name):
        response = self._invoke(
            self._client.CreateTEDSAIResistanceChan,
            grpc_types.CreateTEDSAIResistanceChanRequest(
                task=task, physical_channel=physical_channel,
                name_to_assign_to_channel=name_to_assign_to_channel,
                min_val=min_val, max_val=max_val, units_raw=units,
                resistance_config_raw=resistance_config,
                current_excit_source_raw=current_excit_source,
                current_excit_val=current_excit_val,
                custom_scale_name=custom_scale_name))

    def create_tedsai_strain_gage_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, voltage_excit_source, voltage_excit_val,
            initial_bridge_voltage, lead_wire_resistance, custom_scale_name):
        response = self._invoke(
            self._client.CreateTEDSAIStrainGageChan,
            grpc_types.CreateTEDSAIStrainGageChanRequest(
                task=task, physical_channel=physical_channel,
                name_to_assign_to_channel=name_to_assign_to_channel,
                min_val=min_val, max_val=max_val, units_raw=units,
                voltage_excit_source_raw=voltage_excit_source,
                voltage_excit_val=voltage_excit_val,
                initial_bridge_voltage=initial_bridge_voltage,
                lead_wire_resistance=lead_wire_resistance,
                custom_scale_name=custom_scale_name))

    def create_tedsai_thrmcpl_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, cjc_source, cjc_val, cjc_channel):
        response = self._invoke(
            self._client.CreateTEDSAIThrmcplChan,
            grpc_types.CreateTEDSAIThrmcplChanRequest(
                task=task, physical_channel=physical_channel,
                name_to_assign_to_channel=name_to_assign_to_channel,
                min_val=min_val, max_val=max_val, units_raw=units,
                cjc_source_raw=cjc_source, cjc_val=cjc_val,
                cjc_channel=cjc_channel))

    def create_tedsai_thrmstr_chan_iex(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, resistance_config, current_excit_source,
            current_excit_val):
        response = self._invoke(
            self._client.CreateTEDSAIThrmstrChanIex,
            grpc_types.CreateTEDSAIThrmstrChanIexRequest(
                task=task, physical_channel=physical_channel,
                name_to_assign_to_channel=name_to_assign_to_channel,
                min_val=min_val, max_val=max_val, units_raw=units,
                resistance_config_raw=resistance_config,
                current_excit_source_raw=current_excit_source,
                current_excit_val=current_excit_val))

    def create_tedsai_thrmstr_chan_vex(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, resistance_config, voltage_excit_source,
            voltage_excit_val, r_1):
        response = self._invoke(
            self._client.CreateTEDSAIThrmstrChanVex,
            grpc_types.CreateTEDSAIThrmstrChanVexRequest(
                task=task, physical_channel=physical_channel,
                name_to_assign_to_channel=name_to_assign_to_channel,
                min_val=min_val, max_val=max_val, units_raw=units,
                resistance_config_raw=resistance_config,
                voltage_excit_source_raw=voltage_excit_source,
                voltage_excit_val=voltage_excit_val, r1=r_1))

    def create_tedsai_torque_bridge_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, voltage_excit_source, voltage_excit_val,
            custom_scale_name):
        response = self._invoke(
            self._client.CreateTEDSAITorqueBridgeChan,
            grpc_types.CreateTEDSAITorqueBridgeChanRequest(
                task=task, physical_channel=physical_channel,
                name_to_assign_to_channel=name_to_assign_to_channel,
                min_val=min_val, max_val=max_val, units_raw=units,
                voltage_excit_source_raw=voltage_excit_source,
                voltage_excit_val=voltage_excit_val,
                custom_scale_name=custom_scale_name))

    def create_tedsai_voltage_chan(
            self, task, physical_channel, name_to_assign_to_channel,
            terminal_config, min_val, max_val, units, custom_scale_name):
        response = self._invoke(
            self._client.CreateTEDSAIVoltageChan,
            grpc_types.CreateTEDSAIVoltageChanRequest(
                task=task, physical_channel=physical_channel,
                name_to_assign_to_channel=name_to_assign_to_channel,
                terminal_config_raw=terminal_config, min_val=min_val,
                max_val=max_val, units_raw=units,
                custom_scale_name=custom_scale_name))

    def create_tedsai_voltage_chan_with_excit(
            self, task, physical_channel, name_to_assign_to_channel,
            terminal_config, min_val, max_val, units, voltage_excit_source,
            voltage_excit_val, custom_scale_name):
        response = self._invoke(
            self._client.CreateTEDSAIVoltageChanWithExcit,
            grpc_types.CreateTEDSAIVoltageChanWithExcitRequest(
                task=task, physical_channel=physical_channel,
                name_to_assign_to_channel=name_to_assign_to_channel,
                terminal_config_raw=terminal_config, min_val=min_val,
                max_val=max_val, units_raw=units,
                voltage_excit_source_raw=voltage_excit_source,
                voltage_excit_val=voltage_excit_val,
                custom_scale_name=custom_scale_name))

    def create_tedsairtd_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, resistance_config, current_excit_source,
            current_excit_val):
        response = self._invoke(
            self._client.CreateTEDSAIRTDChan,
            grpc_types.CreateTEDSAIRTDChanRequest(
                task=task, physical_channel=physical_channel,
                name_to_assign_to_channel=name_to_assign_to_channel,
                min_val=min_val, max_val=max_val, units_raw=units,
                resistance_config_raw=resistance_config,
                current_excit_source_raw=current_excit_source,
                current_excit_val=current_excit_val))

    def create_watchdog_timer_task_ex(
            self, device_name, session_name, timeout):
        metadata = (
            ('ni-api-key', self._grpc_options.api_key),
        )
        response = self._invoke(
            self._client.CreateWatchdogTimerTaskEx,
            grpc_types.CreateWatchdogTimerTaskExRequest(
                device_name=device_name, session_name=session_name,
                timeout=timeout,
                initialization_behavior=self._grpc_options.initialization_behavior),
            metadata=metadata)
        return response.task, response.new_session_initialized

    def delete_network_device(self, device_name):
        response = self._invoke(
            self._client.DeleteNetworkDevice,
            grpc_types.DeleteNetworkDeviceRequest(device_name=device_name))

    def delete_saved_global_chan(self, channel_name):
        response = self._invoke(
            self._client.DeleteSavedGlobalChan,
            grpc_types.DeleteSavedGlobalChanRequest(channel_name=channel_name))

    def delete_saved_scale(self, scale_name):
        response = self._invoke(
            self._client.DeleteSavedScale,
            grpc_types.DeleteSavedScaleRequest(scale_name=scale_name))

    def delete_saved_task(self, task_name):
        response = self._invoke(
            self._client.DeleteSavedTask,
            grpc_types.DeleteSavedTaskRequest(task_name=task_name))

    def device_supports_cal(self, device_name):
        response = self._invoke(
            self._client.DeviceSupportsCal,
            grpc_types.DeviceSupportsCalRequest(device_name=device_name))
        return response.cal_supported

    def disable_ref_trig(self, task):
        response = self._invoke(
            self._client.DisableRefTrig,
            grpc_types.DisableRefTrigRequest(task=task))

    def disable_start_trig(self, task):
        response = self._invoke(
            self._client.DisableStartTrig,
            grpc_types.DisableStartTrigRequest(task=task))

    def disconnect_terms(self, source_terminal, destination_terminal):
        response = self._invoke(
            self._client.DisconnectTerms,
            grpc_types.DisconnectTermsRequest(
                source_terminal=source_terminal,
                destination_terminal=destination_terminal))

    def export_signal(self, task, signal_id, output_terminal):
        response = self._invoke(
            self._client.ExportSignal,
            grpc_types.ExportSignalRequest(
                task=task, signal_id_raw=signal_id,
                output_terminal=output_terminal))

    def get_analog_power_up_states_with_output_type(
            self, channel_names, array_size):
        response = self._invoke(
            self._client.GetAnalogPowerUpStatesWithOutputType,
            grpc_types.GetAnalogPowerUpStatesWithOutputTypeRequest(
                channel_names=channel_names, array_size=array_size))
        return list(response.state_array), list(response.channel_type_array)

    def get_auto_configured_cdaq_sync_connections(self):
        response = self._invoke(
            self._client.GetAutoConfiguredCDAQSyncConnections,
            grpc_types.GetAutoConfiguredCDAQSyncConnectionsRequest())
        return response.port_list

    def get_buffer_attribute_uint32(self, task, attribute):
        response = self._invoke(
            self._client.GetBufferAttributeUInt32,
            grpc_types.GetBufferAttributeUInt32Request(task=task, attribute_raw=attribute))
        return response.value

    def get_cal_info_attribute_bool(self, device_name, attribute):
        response = self._invoke(
            self._client.GetCalInfoAttributeBool,
            grpc_types.GetCalInfoAttributeBoolRequest(
                device_name=device_name, attribute_raw=attribute))
        return response.value

    def get_cal_info_attribute_double(self, device_name, attribute):
        response = self._invoke(
            self._client.GetCalInfoAttributeDouble,
            grpc_types.GetCalInfoAttributeDoubleRequest(
                device_name=device_name, attribute_raw=attribute))
        return response.value

    def get_cal_info_attribute_string(self, device_name, attribute):
        response = self._invoke(
            self._client.GetCalInfoAttributeString,
            grpc_types.GetCalInfoAttributeStringRequest(
                device_name=device_name, attribute_raw=attribute))
        return response.value

    def get_cal_info_attribute_uint32(self, device_name, attribute):
        response = self._invoke(
            self._client.GetCalInfoAttributeUInt32,
            grpc_types.GetCalInfoAttributeUInt32Request(
                device_name=device_name, attribute_raw=attribute))
        return response.value

    def get_chan_attribute_bool(self, task, channel, attribute):
        response = self._invoke(
            self._client.GetChanAttributeBool,
            grpc_types.GetChanAttributeBoolRequest(
                task=task, channel=channel, attribute_raw=attribute))
        return response.value

    def get_chan_attribute_double(self, task, channel, attribute):
        response = self._invoke(
            self._client.GetChanAttributeDouble,
            grpc_types.GetChanAttributeDoubleRequest(
                task=task, channel=channel, attribute_raw=attribute))
        return response.value

    def get_chan_attribute_double_array(self, task, channel, attribute):
        response = self._invoke(
            self._client.GetChanAttributeDoubleArray,
            grpc_types.GetChanAttributeDoubleArrayRequest(
                task=task, channel=channel, attribute_raw=attribute))
        return list(response.value)

    def get_chan_attribute_int32(self, task, channel, attribute):
        response = self._invoke(
            self._client.GetChanAttributeInt32,
            grpc_types.GetChanAttributeInt32Request(
                task=task, channel=channel, attribute_raw=attribute))
        return response.value_raw

    def get_chan_attribute_string(self, task, channel, attribute):
        response = self._invoke(
            self._client.GetChanAttributeString,
            grpc_types.GetChanAttributeStringRequest(
                task=task, channel=channel, attribute_raw=attribute))
        return response.value

    def get_chan_attribute_uint32(self, task, channel, attribute):
        response = self._invoke(
            self._client.GetChanAttributeUInt32,
            grpc_types.GetChanAttributeUInt32Request(
                task=task, channel=channel, attribute_raw=attribute))
        return response.value

    def get_device_attribute_bool(self, device_name, attribute):
        response = self._invoke(
            self._client.GetDeviceAttributeBool,
            grpc_types.GetDeviceAttributeBoolRequest(
                device_name=device_name, attribute_raw=attribute))
        return response.value

    def get_device_attribute_double(self, device_name, attribute):
        response = self._invoke(
            self._client.GetDeviceAttributeDouble,
            grpc_types.GetDeviceAttributeDoubleRequest(
                device_name=device_name, attribute_raw=attribute))
        return response.value

    def get_device_attribute_double_array(self, device_name, attribute):
        response = self._invoke(
            self._client.GetDeviceAttributeDoubleArray,
            grpc_types.GetDeviceAttributeDoubleArrayRequest(
                device_name=device_name, attribute_raw=attribute))
        return list(response.value)

    def get_device_attribute_int32(self, device_name, attribute):
        response = self._invoke(
            self._client.GetDeviceAttributeInt32,
            grpc_types.GetDeviceAttributeInt32Request(
                device_name=device_name, attribute_raw=attribute))
        return response.value_raw

    def get_device_attribute_int32_array(self, device_name, attribute):
        response = self._invoke(
            self._client.GetDeviceAttributeInt32Array,
            grpc_types.GetDeviceAttributeInt32ArrayRequest(
                device_name=device_name, attribute_raw=attribute))
        return response.value_raw

    def get_device_attribute_string(self, device_name, attribute):
        response = self._invoke(
            self._client.GetDeviceAttributeString,
            grpc_types.GetDeviceAttributeStringRequest(
                device_name=device_name, attribute_raw=attribute))
        return response.value

    def get_device_attribute_uint32(self, device_name, attribute):
        response = self._invoke(
            self._client.GetDeviceAttributeUInt32,
            grpc_types.GetDeviceAttributeUInt32Request(
                device_name=device_name, attribute_raw=attribute))
        return response.value

    def get_device_attribute_uint32_array(self, device_name, attribute):
        response = self._invoke(
            self._client.GetDeviceAttributeUInt32Array,
            grpc_types.GetDeviceAttributeUInt32ArrayRequest(
                device_name=device_name, attribute_raw=attribute))
        return list(response.value)

    def get_digital_logic_family_power_up_state(self, device_name):
        response = self._invoke(
            self._client.GetDigitalLogicFamilyPowerUpState,
            grpc_types.GetDigitalLogicFamilyPowerUpStateRequest(device_name=device_name))
        return response.logic_family

    def get_digital_power_up_states(self, device_name, channel_name):
        response = self._invoke(
            self._client.GetDigitalPowerUpStates,
            grpc_types.GetDigitalPowerUpStatesRequest(
                device_name=device_name, channel_name=channel_name))
        return response.power_up_states

    def get_digital_pull_up_pull_down_states(self, device_name, channel_name):
        response = self._invoke(
            self._client.GetDigitalPullUpPullDownStates,
            grpc_types.GetDigitalPullUpPullDownStatesRequest(
                device_name=device_name, channel_name=channel_name))
        return response.pull_up_pull_down_states

    def get_disconnected_cdaq_sync_ports(self):
        response = self._invoke(
            self._client.GetDisconnectedCDAQSyncPorts,
            grpc_types.GetDisconnectedCDAQSyncPortsRequest())
        return response.port_list

    def get_exported_signal_attribute_bool(self, task, attribute):
        response = self._invoke(
            self._client.GetExportedSignalAttributeBool,
            grpc_types.GetExportedSignalAttributeBoolRequest(task=task, attribute_raw=attribute))
        return response.value

    def get_exported_signal_attribute_double(self, task, attribute):
        response = self._invoke(
            self._client.GetExportedSignalAttributeDouble,
            grpc_types.GetExportedSignalAttributeDoubleRequest(
                task=task, attribute_raw=attribute))
        return response.value

    def get_exported_signal_attribute_int32(self, task, attribute):
        response = self._invoke(
            self._client.GetExportedSignalAttributeInt32,
            grpc_types.GetExportedSignalAttributeInt32Request(
                task=task, attribute_raw=attribute))
        return response.value_raw

    def get_exported_signal_attribute_string(self, task, attribute):
        response = self._invoke(
            self._client.GetExportedSignalAttributeString,
            grpc_types.GetExportedSignalAttributeStringRequest(
                task=task, attribute_raw=attribute))
        return response.value

    def get_exported_signal_attribute_uint32(self, task, attribute):
        response = self._invoke(
            self._client.GetExportedSignalAttributeUInt32,
            grpc_types.GetExportedSignalAttributeUInt32Request(
                task=task, attribute_raw=attribute))
        return response.value

    def get_ext_cal_last_date_and_time(self, device_name):
        response = self._invoke(
            self._client.GetExtCalLastDateAndTime,
            grpc_types.GetExtCalLastDateAndTimeRequest(device_name=device_name))
        return response.year, response.month, response.day, response.hour, response.minute

    def get_persisted_chan_attribute_bool(self, channel, attribute):
        response = self._invoke(
            self._client.GetPersistedChanAttributeBool,
            grpc_types.GetPersistedChanAttributeBoolRequest(
                channel=channel, attribute_raw=attribute))
        return response.value

    def get_persisted_chan_attribute_string(self, channel, attribute):
        response = self._invoke(
            self._client.GetPersistedChanAttributeString,
            grpc_types.GetPersistedChanAttributeStringRequest(
                channel=channel, attribute_raw=attribute))
        return response.value

    def get_persisted_scale_attribute_bool(self, scale_name, attribute):
        response = self._invoke(
            self._client.GetPersistedScaleAttributeBool,
            grpc_types.GetPersistedScaleAttributeBoolRequest(
                scale_name=scale_name, attribute_raw=attribute))
        return response.value

    def get_persisted_scale_attribute_string(self, scale_name, attribute):
        response = self._invoke(
            self._client.GetPersistedScaleAttributeString,
            grpc_types.GetPersistedScaleAttributeStringRequest(
                scale_name=scale_name, attribute_raw=attribute))
        return response.value

    def get_persisted_task_attribute_bool(self, task_name, attribute):
        response = self._invoke(
            self._client.GetPersistedTaskAttributeBool,
            grpc_types.GetPersistedTaskAttributeBoolRequest(
                task_name=task_name, attribute_raw=attribute))
        return response.value

    def get_persisted_task_attribute_string(self, task_name, attribute):
        response = self._invoke(
            self._client.GetPersistedTaskAttributeString,
            grpc_types.GetPersistedTaskAttributeStringRequest(
                task_name=task_name, attribute_raw=attribute))
        return response.value

    def get_physical_chan_attribute_bool(self, physical_channel, attribute):
        response = self._invoke(
            self._client.GetPhysicalChanAttributeBool,
            grpc_types.GetPhysicalChanAttributeBoolRequest(
                physical_channel=physical_channel, attribute_raw=attribute))
        return response.value

    def get_physical_chan_attribute_bytes(self, physical_channel, attribute):
        response = self._invoke(
            self._client.GetPhysicalChanAttributeBytes,
            grpc_types.GetPhysicalChanAttributeBytesRequest(
                physical_channel=physical_channel, attribute_raw=attribute))
        return list(response.value)

    def get_physical_chan_attribute_double(self, physical_channel, attribute):
        response = self._invoke(
            self._client.GetPhysicalChanAttributeDouble,
            grpc_types.GetPhysicalChanAttributeDoubleRequest(
                physical_channel=physical_channel, attribute_raw=attribute))
        return response.value

    def get_physical_chan_attribute_double_array(
            self, physical_channel, attribute):
        response = self._invoke(
            self._client.GetPhysicalChanAttributeDoubleArray,
            grpc_types.GetPhysicalChanAttributeDoubleArrayRequest(
                physical_channel=physical_channel, attribute_raw=attribute))
        return list(response.value)

    def get_physical_chan_attribute_int32(self, physical_channel, attribute):
        response = self._invoke(
            self._client.GetPhysicalChanAttributeInt32,
            grpc_types.GetPhysicalChanAttributeInt32Request(
                physical_channel=physical_channel, attribute_raw=attribute))
        return response.value_raw

    def get_physical_chan_attribute_int32_array(
            self, physical_channel, attribute):
        response = self._invoke(
            self._client.GetPhysicalChanAttributeInt32Array,
            grpc_types.GetPhysicalChanAttributeInt32ArrayRequest(
                physical_channel=physical_channel, attribute_raw=attribute))
        return response.value_raw

    def get_physical_chan_attribute_string(self, physical_channel, attribute):
        response = self._invoke(
            self._client.GetPhysicalChanAttributeString,
            grpc_types.GetPhysicalChanAttributeStringRequest(
                physical_channel=physical_channel, attribute_raw=attribute))
        return response.value

    def get_physical_chan_attribute_uint32(self, physical_channel, attribute):
        response = self._invoke(
            self._client.GetPhysicalChanAttributeUInt32,
            grpc_types.GetPhysicalChanAttributeUInt32Request(
                physical_channel=physical_channel, attribute_raw=attribute))
        return response.value

    def get_physical_chan_attribute_uint32_array(
            self, physical_channel, attribute):
        response = self._invoke(
            self._client.GetPhysicalChanAttributeUInt32Array,
            grpc_types.GetPhysicalChanAttributeUInt32ArrayRequest(
                physical_channel=physical_channel, attribute_raw=attribute))
        return list(response.value)

    def get_read_attribute_bool(self, task, attribute):
        response = self._invoke(
            self._client.GetReadAttributeBool,
            grpc_types.GetReadAttributeBoolRequest(task=task, attribute_raw=attribute))
        return response.value

    def get_read_attribute_double(self, task, attribute):
        response = self._invoke(
            self._client.GetReadAttributeDouble,
            grpc_types.GetReadAttributeDoubleRequest(task=task, attribute_raw=attribute))
        return response.value

    def get_read_attribute_int32(self, task, attribute):
        response = self._invoke(
            self._client.GetReadAttributeInt32,
            grpc_types.GetReadAttributeInt32Request(task=task, attribute_raw=attribute))
        return response.value_raw

    def get_read_attribute_string(self, task, attribute, size_hint=0):
        response = self._invoke(
            self._client.GetReadAttributeString,
            grpc_types.GetReadAttributeStringRequest(task=task, attribute_raw=attribute))
        return response.value

    def get_read_attribute_uint32(self, task, attribute):
        response = self._invoke(
            self._client.GetReadAttributeUInt32,
            grpc_types.GetReadAttributeUInt32Request(task=task, attribute_raw=attribute))
        return response.value

    def get_read_attribute_uint64(self, task, attribute):
        response = self._invoke(
            self._client.GetReadAttributeUInt64,
            grpc_types.GetReadAttributeUInt64Request(task=task, attribute_raw=attribute))
        return response.value

    def get_scale_attribute_double(self, scale_name, attribute):
        response = self._invoke(
            self._client.GetScaleAttributeDouble,
            grpc_types.GetScaleAttributeDoubleRequest(
                scale_name=scale_name, attribute_raw=attribute))
        return response.value

    def get_scale_attribute_double_array(self, scale_name, attribute):
        response = self._invoke(
            self._client.GetScaleAttributeDoubleArray,
            grpc_types.GetScaleAttributeDoubleArrayRequest(
                scale_name=scale_name, attribute_raw=attribute))
        return list(response.value)

    def get_scale_attribute_int32(self, scale_name, attribute):
        response = self._invoke(
            self._client.GetScaleAttributeInt32,
            grpc_types.GetScaleAttributeInt32Request(
                scale_name=scale_name, attribute_raw=attribute))
        return response.value_raw

    def get_scale_attribute_string(self, scale_name, attribute):
        response = self._invoke(
            self._client.GetScaleAttributeString,
            grpc_types.GetScaleAttributeStringRequest(
                scale_name=scale_name, attribute_raw=attribute))
        return response.value

    def get_self_cal_last_date_and_time(self, device_name):
        response = self._invoke(
            self._client.GetSelfCalLastDateAndTime,
            grpc_types.GetSelfCalLastDateAndTimeRequest(device_name=device_name))
        return response.year, response.month, response.day, response.hour, response.minute

    def get_system_info_attribute_string(self, attribute):
        response = self._invoke(
            self._client.GetSystemInfoAttributeString,
            grpc_types.GetSystemInfoAttributeStringRequest(attribute_raw=attribute))
        return response.value

    def get_system_info_attribute_uint32(self, attribute):
        response = self._invoke(
            self._client.GetSystemInfoAttributeUInt32,
            grpc_types.GetSystemInfoAttributeUInt32Request(attribute_raw=attribute))
        return response.value

    def get_task_attribute_bool(self, task, attribute):
        response = self._invoke(
            self._client.GetTaskAttributeBool,
            grpc_types.GetTaskAttributeBoolRequest(task=task, attribute_raw=attribute))
        return response.value

    def get_task_attribute_string(self, task, attribute):
        response = self._invoke(
            self._client.GetTaskAttributeString,
            grpc_types.GetTaskAttributeStringRequest(task=task, attribute_raw=attribute))
        return response.value

    def get_task_attribute_uint32(self, task, attribute):
        response = self._invoke(
            self._client.GetTaskAttributeUInt32,
            grpc_types.GetTaskAttributeUInt32Request(task=task, attribute_raw=attribute))
        return response.value

    def get_timing_attribute_bool(self, task, attribute):
        response = self._invoke(
            self._client.GetTimingAttributeBool,
            grpc_types.GetTimingAttributeBoolRequest(task=task, attribute_raw=attribute))
        return response.value

    def get_timing_attribute_double(self, task, attribute):
        response = self._invoke(
            self._client.GetTimingAttributeDouble,
            grpc_types.GetTimingAttributeDoubleRequest(task=task, attribute_raw=attribute))
        return response.value

    def get_timing_attribute_ex_bool(self, task, device_names, attribute):
        response = self._invoke(
            self._client.GetTimingAttributeExBool,
            grpc_types.GetTimingAttributeExBoolRequest(
                task=task, device_names=device_names, attribute_raw=attribute))
        return response.value

    def get_timing_attribute_ex_double(self, task, device_names, attribute):
        response = self._invoke(
            self._client.GetTimingAttributeExDouble,
            grpc_types.GetTimingAttributeExDoubleRequest(
                task=task, device_names=device_names, attribute_raw=attribute))
        return response.value

    def get_timing_attribute_ex_int32(self, task, device_names, attribute):
        response = self._invoke(
            self._client.GetTimingAttributeExInt32,
            grpc_types.GetTimingAttributeExInt32Request(
                task=task, device_names=device_names, attribute_raw=attribute))
        return response.value_raw

    def get_timing_attribute_ex_string(self, task, device_names, attribute):
        response = self._invoke(
            self._client.GetTimingAttributeExString,
            grpc_types.GetTimingAttributeExStringRequest(
                task=task, device_names=device_names, attribute_raw=attribute))
        return response.value

    def get_timing_attribute_ex_uint32(self, task, device_names, attribute):
        response = self._invoke(
            self._client.GetTimingAttributeExUInt32,
            grpc_types.GetTimingAttributeExUInt32Request(
                task=task, device_names=device_names, attribute_raw=attribute))
        return response.value

    def get_timing_attribute_ex_uint64(self, task, device_names, attribute):
        response = self._invoke(
            self._client.GetTimingAttributeExUInt64,
            grpc_types.GetTimingAttributeExUInt64Request(
                task=task, device_names=device_names, attribute_raw=attribute))
        return response.value

    def get_timing_attribute_int32(self, task, attribute):
        response = self._invoke(
            self._client.GetTimingAttributeInt32,
            grpc_types.GetTimingAttributeInt32Request(task=task, attribute_raw=attribute))
        return response.value_raw

    def get_timing_attribute_string(self, task, attribute):
        response = self._invoke(
            self._client.GetTimingAttributeString,
            grpc_types.GetTimingAttributeStringRequest(task=task, attribute_raw=attribute))
        return response.value

    def get_timing_attribute_timestamp(self, task, attribute):
        response = self._invoke(
            self._client.GetTimingAttributeTimestamp,
            grpc_types.GetTimingAttributeTimestampRequest(task=task, attribute_raw=attribute))
        return convert_timestamp_to_time(response.value)

    def get_timing_attribute_uint32(self, task, attribute):
        response = self._invoke(
            self._client.GetTimingAttributeUInt32,
            grpc_types.GetTimingAttributeUInt32Request(task=task, attribute_raw=attribute))
        return response.value

    def get_timing_attribute_uint64(self, task, attribute):
        response = self._invoke(
            self._client.GetTimingAttributeUInt64,
            grpc_types.GetTimingAttributeUInt64Request(task=task, attribute_raw=attribute))
        return response.value

    def get_trig_attribute_bool(self, task, attribute):
        response = self._invoke(
            self._client.GetTrigAttributeBool,
            grpc_types.GetTrigAttributeBoolRequest(task=task, attribute_raw=attribute))
        return response.value

    def get_trig_attribute_double(self, task, attribute):
        response = self._invoke(
            self._client.GetTrigAttributeDouble,
            grpc_types.GetTrigAttributeDoubleRequest(task=task, attribute_raw=attribute))
        return response.value

    def get_trig_attribute_double_array(self, task, attribute):
        response = self._invoke(
            self._client.GetTrigAttributeDoubleArray,
            grpc_types.GetTrigAttributeDoubleArrayRequest(task=task, attribute_raw=attribute))
        return list(response.value)

    def get_trig_attribute_int32(self, task, attribute):
        response = self._invoke(
            self._client.GetTrigAttributeInt32,
            grpc_types.GetTrigAttributeInt32Request(task=task, attribute_raw=attribute))
        return response.value_raw

    def get_trig_attribute_int32_array(self, task, attribute):
        response = self._invoke(
            self._client.GetTrigAttributeInt32Array,
            grpc_types.GetTrigAttributeInt32ArrayRequest(task=task, attribute_raw=attribute))
        return response.value_raw

    def get_trig_attribute_string(self, task, attribute):
        response = self._invoke(
            self._client.GetTrigAttributeString,
            grpc_types.GetTrigAttributeStringRequest(task=task, attribute_raw=attribute))
        return response.value

    def get_trig_attribute_timestamp(self, task, attribute):
        response = self._invoke(
            self._client.GetTrigAttributeTimestamp,
            grpc_types.GetTrigAttributeTimestampRequest(task=task, attribute_raw=attribute))
        return convert_timestamp_to_time(response.value)

    def get_trig_attribute_uint32(self, task, attribute):
        response = self._invoke(
            self._client.GetTrigAttributeUInt32,
            grpc_types.GetTrigAttributeUInt32Request(task=task, attribute_raw=attribute))
        return response.value

    def get_watchdog_attribute_bool(self, task, lines, attribute):
        response = self._invoke(
            self._client.GetWatchdogAttributeBool,
            grpc_types.GetWatchdogAttributeBoolRequest(
                task=task, lines=lines, attribute_raw=attribute))
        return response.value

    def get_watchdog_attribute_double(self, task, lines, attribute):
        response = self._invoke(
            self._client.GetWatchdogAttributeDouble,
            grpc_types.GetWatchdogAttributeDoubleRequest(
                task=task, lines=lines, attribute_raw=attribute))
        return response.value

    def get_watchdog_attribute_int32(self, task, lines, attribute):
        response = self._invoke(
            self._client.GetWatchdogAttributeInt32,
            grpc_types.GetWatchdogAttributeInt32Request(
                task=task, lines=lines, attribute_raw=attribute))
        return response.value_raw

    def get_watchdog_attribute_string(self, task, lines, attribute):
        response = self._invoke(
            self._client.GetWatchdogAttributeString,
            grpc_types.GetWatchdogAttributeStringRequest(
                task=task, lines=lines, attribute_raw=attribute))
        return response.value

    def get_write_attribute_bool(self, task, attribute):
        response = self._invoke(
            self._client.GetWriteAttributeBool,
            grpc_types.GetWriteAttributeBoolRequest(task=task, attribute_raw=attribute))
        return response.value

    def get_write_attribute_double(self, task, attribute):
        response = self._invoke(
            self._client.GetWriteAttributeDouble,
            grpc_types.GetWriteAttributeDoubleRequest(task=task, attribute_raw=attribute))
        return response.value

    def get_write_attribute_int32(self, task, attribute):
        response = self._invoke(
            self._client.GetWriteAttributeInt32,
            grpc_types.GetWriteAttributeInt32Request(task=task, attribute_raw=attribute))
        return response.value_raw

    def get_write_attribute_string(self, task, attribute, size_hint=0):
        response = self._invoke(
            self._client.GetWriteAttributeString,
            grpc_types.GetWriteAttributeStringRequest(task=task, attribute_raw=attribute))
        return response.value

    def get_write_attribute_uint32(self, task, attribute):
        response = self._invoke(
            self._client.GetWriteAttributeUInt32,
            grpc_types.GetWriteAttributeUInt32Request(task=task, attribute_raw=attribute))
        return response.value

    def get_write_attribute_uint64(self, task, attribute):
        response = self._invoke(
            self._client.GetWriteAttributeUInt64,
            grpc_types.GetWriteAttributeUInt64Request(task=task, attribute_raw=attribute))
        return response.value

    def is_task_done(self, task):
        response = self._invoke(
            self._client.IsTaskDone,
            grpc_types.IsTaskDoneRequest(task=task))
        return response.is_task_done

    def load_task(self, session_name):
        metadata = (
            ('ni-api-key', self._grpc_options.api_key),
        )
        response = self._invoke(
            self._client.LoadTask,
            grpc_types.LoadTaskRequest(
                session_name=session_name,
                initialization_behavior=self._grpc_options.initialization_behavior),
            metadata=metadata)
        return response.task, response.new_session_initialized

    def perform_bridge_offset_nulling_cal_ex(
            self, task, channel, skip_unsupported_channels):
        response = self._invoke(
            self._client.PerformBridgeOffsetNullingCalEx,
            grpc_types.PerformBridgeOffsetNullingCalExRequest(
                task=task, channel=channel,
                skip_unsupported_channels=skip_unsupported_channels))

    def perform_bridge_shunt_cal_ex(
            self, task, channel, shunt_resistor_value,
            shunt_resistor_location, shunt_resistor_select,
            shunt_resistor_source, bridge_resistance,
            skip_unsupported_channels):
        response = self._invoke(
            self._client.PerformBridgeShuntCalEx,
            grpc_types.PerformBridgeShuntCalExRequest(
                task=task, channel=channel,
                shunt_resistor_value=shunt_resistor_value,
                shunt_resistor_location_raw=shunt_resistor_location,
                shunt_resistor_select_raw=shunt_resistor_select,
                shunt_resistor_source_raw=shunt_resistor_source,
                bridge_resistance=bridge_resistance,
                skip_unsupported_channels=skip_unsupported_channels))

    def perform_strain_shunt_cal_ex(
            self, task, channel, shunt_resistor_value,
            shunt_resistor_location, shunt_resistor_select,
            shunt_resistor_source, skip_unsupported_channels):
        response = self._invoke(
            self._client.PerformStrainShuntCalEx,
            grpc_types.PerformStrainShuntCalExRequest(
                task=task, channel=channel,
                shunt_resistor_value=shunt_resistor_value,
                shunt_resistor_location_raw=shunt_resistor_location,
                shunt_resistor_select_raw=shunt_resistor_select,
                shunt_resistor_source_raw=shunt_resistor_source,
                skip_unsupported_channels=skip_unsupported_channels))

    def perform_thrmcpl_lead_offset_nulling_cal(
            self, task, channel, skip_unsupported_channels):
        response = self._invoke(
            self._client.PerformThrmcplLeadOffsetNullingCal,
            grpc_types.PerformThrmcplLeadOffsetNullingCalRequest(
                task=task, channel=channel,
                skip_unsupported_channels=skip_unsupported_channels))

    def read_analog_f64(
            self, task, num_samps_per_chan, timeout, fill_mode, read_array):
        _validate_array_dtype(read_array, numpy.float64)
        response = self._invoke(
            self._client.ReadAnalogF64,
            grpc_types.ReadAnalogF64Request(
                task=task, num_samps_per_chan=num_samps_per_chan,
                timeout=timeout, fill_mode_raw=fill_mode,
                array_size_in_samps=read_array.size))
    
        _assign_numpy_array(read_array, response.read_array)
        self._check_for_error_from_response(response.status, samps_per_chan_read=response.samps_per_chan_read)
        return read_array, response.samps_per_chan_read

    def read_analog_scalar_f64(self, task, timeout):
        response = self._invoke(
            self._client.ReadAnalogScalarF64,
            grpc_types.ReadAnalogScalarF64Request(task=task, timeout=timeout))
        return response.value

    def read_binary_i16(
            self, task, num_samps_per_chan, timeout, fill_mode, read_array):
        _validate_array_dtype(read_array, numpy.int16)
        response = self._invoke(
            self._client.ReadBinaryI16,
            grpc_types.ReadBinaryI16Request(
                task=task, num_samps_per_chan=num_samps_per_chan,
                timeout=timeout, fill_mode_raw=fill_mode,
                array_size_in_samps=read_array.size))
    
        _assign_numpy_array(read_array, response.read_array)
        self._check_for_error_from_response(response.status, samps_per_chan_read=response.samps_per_chan_read)
        return read_array, response.samps_per_chan_read

    def read_binary_i32(
            self, task, num_samps_per_chan, timeout, fill_mode, read_array):
        _validate_array_dtype(read_array, numpy.int32)
        response = self._invoke(
            self._client.ReadBinaryI32,
            grpc_types.ReadBinaryI32Request(
                task=task, num_samps_per_chan=num_samps_per_chan,
                timeout=timeout, fill_mode_raw=fill_mode,
                array_size_in_samps=read_array.size))
    
        _assign_numpy_array(read_array, response.read_array)
        self._check_for_error_from_response(response.status, samps_per_chan_read=response.samps_per_chan_read)
        return read_array, response.samps_per_chan_read

    def read_binary_u16(
            self, task, num_samps_per_chan, timeout, fill_mode, read_array):
        _validate_array_dtype(read_array, numpy.uint16)
        response = self._invoke(
            self._client.ReadBinaryU16,
            grpc_types.ReadBinaryU16Request(
                task=task, num_samps_per_chan=num_samps_per_chan,
                timeout=timeout, fill_mode_raw=fill_mode,
                array_size_in_samps=read_array.size))
    
        _assign_numpy_array(read_array, response.read_array)
        self._check_for_error_from_response(response.status, samps_per_chan_read=response.samps_per_chan_read)
        return read_array, response.samps_per_chan_read

    def read_binary_u32(
            self, task, num_samps_per_chan, timeout, fill_mode, read_array):
        _validate_array_dtype(read_array, numpy.uint32)
        response = self._invoke(
            self._client.ReadBinaryU32,
            grpc_types.ReadBinaryU32Request(
                task=task, num_samps_per_chan=num_samps_per_chan,
                timeout=timeout, fill_mode_raw=fill_mode,
                array_size_in_samps=read_array.size))
    
        _assign_numpy_array(read_array, response.read_array)
        self._check_for_error_from_response(response.status, samps_per_chan_read=response.samps_per_chan_read)
        return read_array, response.samps_per_chan_read

    def read_counter_f64(self, task, num_samps_per_chan, timeout, read_array):
        _validate_array_dtype(read_array, numpy.float64)
        response = self._invoke(
            self._client.ReadCounterF64,
            grpc_types.ReadCounterF64Request(
                task=task, num_samps_per_chan=num_samps_per_chan,
                timeout=timeout, array_size_in_samps=read_array.size))
    
        _assign_numpy_array(read_array, response.read_array)
        self._check_for_error_from_response(response.status, samps_per_chan_read=response.samps_per_chan_read)
        return read_array, response.samps_per_chan_read

    def read_counter_f64_ex(
            self, task, num_samps_per_chan, timeout, fill_mode, read_array):
        _validate_array_dtype(read_array, numpy.float64)
        response = self._invoke(
            self._client.ReadCounterF64Ex,
            grpc_types.ReadCounterF64ExRequest(
                task=task, num_samps_per_chan=num_samps_per_chan,
                timeout=timeout, fill_mode_raw=fill_mode,
                array_size_in_samps=read_array.size))
    
        _assign_numpy_array(read_array, response.read_array)
        self._check_for_error_from_response(response.status, samps_per_chan_read=response.samps_per_chan_read)
        return read_array, response.samps_per_chan_read

    def read_counter_scalar_f64(self, task, timeout):
        response = self._invoke(
            self._client.ReadCounterScalarF64,
            grpc_types.ReadCounterScalarF64Request(task=task, timeout=timeout))
        return response.value

    def read_counter_scalar_u32(self, task, timeout):
        response = self._invoke(
            self._client.ReadCounterScalarU32,
            grpc_types.ReadCounterScalarU32Request(task=task, timeout=timeout))
        return response.value

    def read_counter_u32(self, task, num_samps_per_chan, timeout, read_array):
        _validate_array_dtype(read_array, numpy.uint32)
        response = self._invoke(
            self._client.ReadCounterU32,
            grpc_types.ReadCounterU32Request(
                task=task, num_samps_per_chan=num_samps_per_chan,
                timeout=timeout, array_size_in_samps=read_array.size))
    
        _assign_numpy_array(read_array, response.read_array)
        self._check_for_error_from_response(response.status, samps_per_chan_read=response.samps_per_chan_read)
        return read_array, response.samps_per_chan_read

    def read_counter_u32_ex(
            self, task, num_samps_per_chan, timeout, fill_mode, read_array):
        _validate_array_dtype(read_array, numpy.uint32)
        response = self._invoke(
            self._client.ReadCounterU32Ex,
            grpc_types.ReadCounterU32ExRequest(
                task=task, num_samps_per_chan=num_samps_per_chan,
                timeout=timeout, fill_mode_raw=fill_mode,
                array_size_in_samps=read_array.size))
    
        _assign_numpy_array(read_array, response.read_array)
        self._check_for_error_from_response(response.status, samps_per_chan_read=response.samps_per_chan_read)
        return read_array, response.samps_per_chan_read

    def read_ctr_freq(
            self, task, num_samps_per_chan, timeout, interleaved,
            read_array_frequency, read_array_duty_cycle):
        _validate_array_dtype(read_array_frequency, numpy.float64)
        _validate_array_dtype(read_array_duty_cycle, numpy.float64)
        response = self._invoke(
            self._client.ReadCtrFreq,
            grpc_types.ReadCtrFreqRequest(
                task=task, num_samps_per_chan=num_samps_per_chan,
                timeout=timeout, interleaved_raw=interleaved,
                array_size_in_samps=read_array_frequency.size))
    
        _assign_numpy_array(read_array_frequency, response.read_array_frequency)
        _assign_numpy_array(read_array_duty_cycle, response.read_array_duty_cycle)
        self._check_for_error_from_response(response.status, samps_per_chan_read=response.samps_per_chan_read)
        return read_array_frequency, read_array_duty_cycle, response.samps_per_chan_read

    def read_ctr_freq_scalar(self, task, timeout):
        response = self._invoke(
            self._client.ReadCtrFreqScalar,
            grpc_types.ReadCtrFreqScalarRequest(task=task, timeout=timeout))
        return response.frequency, response.duty_cycle

    def read_ctr_ticks(
            self, task, num_samps_per_chan, timeout, interleaved,
            read_array_high_ticks, read_array_low_ticks):
        _validate_array_dtype(read_array_high_ticks, numpy.uint32)
        _validate_array_dtype(read_array_low_ticks, numpy.uint32)
        response = self._invoke(
            self._client.ReadCtrTicks,
            grpc_types.ReadCtrTicksRequest(
                task=task, num_samps_per_chan=num_samps_per_chan,
                timeout=timeout, interleaved_raw=interleaved,
                array_size_in_samps=read_array_high_ticks.size))
    
        _assign_numpy_array(read_array_high_ticks, response.read_array_high_ticks)
        _assign_numpy_array(read_array_low_ticks, response.read_array_low_ticks)
        self._check_for_error_from_response(response.status, samps_per_chan_read=response.samps_per_chan_read)
        return read_array_high_ticks, read_array_low_ticks, response.samps_per_chan_read

    def read_ctr_ticks_scalar(self, task, timeout):
        response = self._invoke(
            self._client.ReadCtrTicksScalar,
            grpc_types.ReadCtrTicksScalarRequest(task=task, timeout=timeout))
        return response.high_ticks, response.low_ticks

    def read_ctr_time(
            self, task, num_samps_per_chan, timeout, interleaved,
            read_array_high_time, read_array_low_time):
        _validate_array_dtype(read_array_high_time, numpy.float64)
        _validate_array_dtype(read_array_low_time, numpy.float64)
        response = self._invoke(
            self._client.ReadCtrTime,
            grpc_types.ReadCtrTimeRequest(
                task=task, num_samps_per_chan=num_samps_per_chan,
                timeout=timeout, interleaved_raw=interleaved,
                array_size_in_samps=read_array_high_time.size))
    
        _assign_numpy_array(read_array_high_time, response.read_array_high_time)
        _assign_numpy_array(read_array_low_time, response.read_array_low_time)
        self._check_for_error_from_response(response.status, samps_per_chan_read=response.samps_per_chan_read)
        return read_array_high_time, read_array_low_time, response.samps_per_chan_read

    def read_ctr_time_scalar(self, task, timeout):
        response = self._invoke(
            self._client.ReadCtrTimeScalar,
            grpc_types.ReadCtrTimeScalarRequest(task=task, timeout=timeout))
        return response.high_time, response.low_time

    def read_digital_lines(
            self, task, num_samps_per_chan, timeout, fill_mode, read_array):
        _validate_array_dtype(read_array, bool)
        response = self._invoke(
            self._client.ReadDigitalLines,
            grpc_types.ReadDigitalLinesRequest(
                task=task, num_samps_per_chan=num_samps_per_chan,
                timeout=timeout, fill_mode_raw=fill_mode,
                array_size_in_bytes=read_array.nbytes))
    
        _assign_numpy_array(read_array, response.read_array)
        self._check_for_error_from_response(response.status, samps_per_chan_read=response.samps_per_chan_read)
        return read_array, response.samps_per_chan_read, response.num_bytes_per_samp

    def read_digital_scalar_u32(self, task, timeout):
        response = self._invoke(
            self._client.ReadDigitalScalarU32,
            grpc_types.ReadDigitalScalarU32Request(task=task, timeout=timeout))
        return response.value

    def read_digital_u16(
            self, task, num_samps_per_chan, timeout, fill_mode, read_array):
        _validate_array_dtype(read_array, numpy.uint16)
        response = self._invoke(
            self._client.ReadDigitalU16,
            grpc_types.ReadDigitalU16Request(
                task=task, num_samps_per_chan=num_samps_per_chan,
                timeout=timeout, fill_mode_raw=fill_mode,
                array_size_in_samps=read_array.size))
    
        _assign_numpy_array(read_array, response.read_array)
        self._check_for_error_from_response(response.status, samps_per_chan_read=response.samps_per_chan_read)
        return read_array, response.samps_per_chan_read

    def read_digital_u32(
            self, task, num_samps_per_chan, timeout, fill_mode, read_array):
        _validate_array_dtype(read_array, numpy.uint32)
        response = self._invoke(
            self._client.ReadDigitalU32,
            grpc_types.ReadDigitalU32Request(
                task=task, num_samps_per_chan=num_samps_per_chan,
                timeout=timeout, fill_mode_raw=fill_mode,
                array_size_in_samps=read_array.size))
    
        _assign_numpy_array(read_array, response.read_array)
        self._check_for_error_from_response(response.status, samps_per_chan_read=response.samps_per_chan_read)
        return read_array, response.samps_per_chan_read

    def read_digital_u8(
            self, task, num_samps_per_chan, timeout, fill_mode, read_array):
        _validate_array_dtype(read_array, numpy.uint8)
        response = self._invoke(
            self._client.ReadDigitalU8,
            grpc_types.ReadDigitalU8Request(
                task=task, num_samps_per_chan=num_samps_per_chan,
                timeout=timeout, fill_mode_raw=fill_mode,
                array_size_in_samps=read_array.nbytes))
    
        _assign_numpy_array(read_array, response.read_array)
        self._check_for_error_from_response(response.status, samps_per_chan_read=response.samps_per_chan_read)
        return read_array, response.samps_per_chan_read

    def read_power_binary_i16(
            self, task, num_samps_per_chan, timeout, fill_mode,
            read_array_voltage, read_array_current):
        _validate_array_dtype(read_array_voltage, numpy.int16)
        _validate_array_dtype(read_array_current, numpy.int16)
        response = self._invoke(
            self._client.ReadPowerBinaryI16,
            grpc_types.ReadPowerBinaryI16Request(
                task=task, num_samps_per_chan=num_samps_per_chan,
                timeout=timeout, fill_mode_raw=fill_mode,
                array_size_in_samps=read_array_voltage.size))
    
        _assign_numpy_array(read_array_voltage, response.read_array_voltage)
        _assign_numpy_array(read_array_current, response.read_array_current)
        self._check_for_error_from_response(response.status, samps_per_chan_read=response.samps_per_chan_read)
        return read_array_voltage, read_array_current, response.samps_per_chan_read

    def read_power_f64(
            self, task, num_samps_per_chan, timeout, fill_mode,
            read_array_voltage, read_array_current):
        _validate_array_dtype(read_array_voltage, numpy.float64)
        _validate_array_dtype(read_array_current, numpy.float64)
        response = self._invoke(
            self._client.ReadPowerF64,
            grpc_types.ReadPowerF64Request(
                task=task, num_samps_per_chan=num_samps_per_chan,
                timeout=timeout, fill_mode_raw=fill_mode,
                array_size_in_samps=read_array_voltage.size))
    
        _assign_numpy_array(read_array_voltage, response.read_array_voltage)
        _assign_numpy_array(read_array_current, response.read_array_current)
        self._check_for_error_from_response(response.status, samps_per_chan_read=response.samps_per_chan_read)
        return read_array_voltage, read_array_current, response.samps_per_chan_read

    def read_power_scalar_f64(self, task, timeout):
        response = self._invoke(
            self._client.ReadPowerScalarF64,
            grpc_types.ReadPowerScalarF64Request(task=task, timeout=timeout))
        return response.voltage, response.current

    def read_raw(self, task, num_samps_per_chan, timeout, read_array):
        _validate_array_dtype(read_array, numpy.generic)
        response = self._invoke(
            self._client.ReadRaw,
            grpc_types.ReadRawRequest(
                task=task, num_samps_per_chan=num_samps_per_chan,
                timeout=timeout, array_size_in_bytes=read_array.nbytes))
    
        _assign_numpy_array(read_array, response.read_array)
        self._check_for_error_from_response(response.status, samps_per_chan_read=response.samps_read)
        return read_array, response.samps_read, response.num_bytes_per_samp

    def register_done_event(
            self, task, options, callback_function, callback_data):
        assert options == 0
        assert callback_function is not None

        event_stream = self._invoke(
            self._client.RegisterDoneEvent,
            grpc_types.RegisterDoneEventRequest(task=task))

        self._check_for_event_registration_error(event_stream)

        def invoke_callback(response):
            try:
                callback_function(
                    task, response.status, callback_data)
            except Exception:
                _logger.exception(
                    "Ignoring unhandled exception raised by event callback function: %r",
                    callback_function,
                )

        return GrpcEventHandler(
            "done event",
            self,
            event_stream,
            invoke_callback,
        )

    def register_every_n_samples_event(
            self, task, every_n_samples_event_type, n_samples, options,
            callback_function, callback_data):
        assert options == 0
        assert callback_function is not None

        event_stream = self._invoke(
            self._client.RegisterEveryNSamplesEvent,
            grpc_types.RegisterEveryNSamplesEventRequest(
                task=task,
                every_n_samples_event_type_raw=every_n_samples_event_type,
                n_samples=n_samples))

        self._check_for_event_registration_error(event_stream)

        def invoke_callback(response):
            try:
                callback_function(
                    task, response.every_n_samples_event_type_raw,
                    response.n_samples, callback_data)
            except Exception:
                _logger.exception(
                    "Ignoring unhandled exception raised by event callback function: %r",
                    callback_function,
                )

        return GrpcEventHandler(
            "every n samples event",
            self,
            event_stream,
            invoke_callback,
        )

    def register_signal_event(
            self, task, signal_id, options, callback_function, callback_data):
        assert options == 0
        assert callback_function is not None

        event_stream = self._invoke(
            self._client.RegisterSignalEvent,
            grpc_types.RegisterSignalEventRequest(task=task, signal_id_raw=signal_id))

        self._check_for_event_registration_error(event_stream)

        def invoke_callback(response):
            try:
                callback_function(
                    task, response.signal_id, callback_data)
            except Exception:
                _logger.exception(
                    "Ignoring unhandled exception raised by event callback function: %r",
                    callback_function,
                )

        return GrpcEventHandler(
            "signal event",
            self,
            event_stream,
            invoke_callback,
        )

    def remove_cdaq_sync_connection(self, port_list):
        response = self._invoke(
            self._client.RemoveCDAQSyncConnection,
            grpc_types.RemoveCDAQSyncConnectionRequest(port_list=port_list))

    def reserve_network_device(self, device_name, override_reservation):
        response = self._invoke(
            self._client.ReserveNetworkDevice,
            grpc_types.ReserveNetworkDeviceRequest(
                device_name=device_name,
                override_reservation=override_reservation))

    def reset_buffer_attribute(self, task, attribute):
        response = self._invoke(
            self._client.ResetBufferAttribute,
            grpc_types.ResetBufferAttributeRequest(task=task, attribute_raw=attribute))

    def reset_chan_attribute(self, task, channel, attribute):
        response = self._invoke(
            self._client.ResetChanAttribute,
            grpc_types.ResetChanAttributeRequest(
                task=task, channel=channel, attribute_raw=attribute))

    def reset_device(self, device_name):
        response = self._invoke(
            self._client.ResetDevice,
            grpc_types.ResetDeviceRequest(device_name=device_name))

    def reset_exported_signal_attribute(self, task, attribute):
        response = self._invoke(
            self._client.ResetExportedSignalAttribute,
            grpc_types.ResetExportedSignalAttributeRequest(task=task, attribute_raw=attribute))

    def reset_read_attribute(self, task, attribute):
        response = self._invoke(
            self._client.ResetReadAttribute,
            grpc_types.ResetReadAttributeRequest(task=task, attribute_raw=attribute))

    def reset_timing_attribute(self, task, attribute):
        response = self._invoke(
            self._client.ResetTimingAttribute,
            grpc_types.ResetTimingAttributeRequest(task=task, attribute_raw=attribute))

    def reset_timing_attribute_ex(self, task, device_names, attribute):
        response = self._invoke(
            self._client.ResetTimingAttributeEx,
            grpc_types.ResetTimingAttributeExRequest(
                task=task, device_names=device_names, attribute_raw=attribute))

    def reset_trig_attribute(self, task, attribute):
        response = self._invoke(
            self._client.ResetTrigAttribute,
            grpc_types.ResetTrigAttributeRequest(task=task, attribute_raw=attribute))

    def reset_watchdog_attribute(self, task, lines, attribute):
        response = self._invoke(
            self._client.ResetWatchdogAttribute,
            grpc_types.ResetWatchdogAttributeRequest(
                task=task, lines=lines, attribute_raw=attribute))

    def reset_write_attribute(self, task, attribute):
        response = self._invoke(
            self._client.ResetWriteAttribute,
            grpc_types.ResetWriteAttributeRequest(task=task, attribute_raw=attribute))

    def restore_last_ext_cal_const(self, device_name):
        response = self._invoke(
            self._client.RestoreLastExtCalConst,
            grpc_types.RestoreLastExtCalConstRequest(device_name=device_name))

    def save_global_chan(self, task, channel_name, save_as, author, options):
        response = self._invoke(
            self._client.SaveGlobalChan,
            grpc_types.SaveGlobalChanRequest(
                task=task, channel_name=channel_name, save_as=save_as,
                author=author, options_raw=options))

    def save_scale(self, scale_name, save_as, author, options):
        response = self._invoke(
            self._client.SaveScale,
            grpc_types.SaveScaleRequest(
                scale_name=scale_name, save_as=save_as, author=author,
                options_raw=options))

    def save_task(self, task, save_as, author, options):
        response = self._invoke(
            self._client.SaveTask,
            grpc_types.SaveTaskRequest(
                task=task, save_as=save_as, author=author,
                options_raw=options))

    def self_cal(self, device_name):
        response = self._invoke(
            self._client.SelfCal,
            grpc_types.SelfCalRequest(device_name=device_name))

    def self_test_device(self, device_name):
        response = self._invoke(
            self._client.SelfTestDevice,
            grpc_types.SelfTestDeviceRequest(device_name=device_name))

    def set_analog_power_up_states(
            self, device_name, channel_names, state, channel_type):
        power_up_states = []
        for index in range(len(channel_names)):
            power_up_states.append(grpc_types.AnalogPowerUpChannelsAndState(channel_names=channel_names[index], state=state[index], channel_type=channel_type[index]))
        response = self._invoke(
            self._client.SetAnalogPowerUpStates,
            grpc_types.SetAnalogPowerUpStatesRequest(
                device_name=device_name, power_up_states=power_up_states))

    def set_analog_power_up_states_with_output_type(
            self, channel_names, state_array, channel_type_array):
        response = self._invoke(
            self._client.SetAnalogPowerUpStatesWithOutputType,
            grpc_types.SetAnalogPowerUpStatesWithOutputTypeRequest(
                channel_names=channel_names, state_array=state_array,
                channel_type_array=channel_type_array))

    def set_buffer_attribute_uint32(self, task, attribute, value):
        response = self._invoke(
            self._client.SetBufferAttributeUInt32,
            grpc_types.SetBufferAttributeUInt32Request(
                task=task, attribute_raw=attribute, value=value))

    def set_cal_info_attribute_bool(self, device_name, attribute, value):
        response = self._invoke(
            self._client.SetCalInfoAttributeBool,
            grpc_types.SetCalInfoAttributeBoolRequest(
                device_name=device_name, attribute_raw=attribute, value=value))

    def set_cal_info_attribute_double(self, device_name, attribute, value):
        response = self._invoke(
            self._client.SetCalInfoAttributeDouble,
            grpc_types.SetCalInfoAttributeDoubleRequest(
                device_name=device_name, attribute_raw=attribute, value=value))

    def set_cal_info_attribute_string(self, device_name, attribute, value):
        response = self._invoke(
            self._client.SetCalInfoAttributeString,
            grpc_types.SetCalInfoAttributeStringRequest(
                device_name=device_name, attribute_raw=attribute, value=value))

    def set_cal_info_attribute_uint32(self, device_name, attribute, value):
        response = self._invoke(
            self._client.SetCalInfoAttributeUInt32,
            grpc_types.SetCalInfoAttributeUInt32Request(
                device_name=device_name, attribute_raw=attribute, value=value))

    def set_chan_attribute_bool(self, task, channel, attribute, value):
        response = self._invoke(
            self._client.SetChanAttributeBool,
            grpc_types.SetChanAttributeBoolRequest(
                task=task, channel=channel, attribute_raw=attribute,
                value=value))

    def set_chan_attribute_double(self, task, channel, attribute, value):
        response = self._invoke(
            self._client.SetChanAttributeDouble,
            grpc_types.SetChanAttributeDoubleRequest(
                task=task, channel=channel, attribute_raw=attribute,
                value=value))

    def set_chan_attribute_double_array(self, task, channel, attribute, value):
        response = self._invoke(
            self._client.SetChanAttributeDoubleArray,
            grpc_types.SetChanAttributeDoubleArrayRequest(
                task=task, channel=channel, attribute_raw=attribute,
                value=value))

    def set_chan_attribute_int32(self, task, channel, attribute, value):
        response = self._invoke(
            self._client.SetChanAttributeInt32,
            grpc_types.SetChanAttributeInt32Request(
                task=task, channel=channel, attribute_raw=attribute,
                value_raw=value))

    def set_chan_attribute_string(self, task, channel, attribute, value):
        response = self._invoke(
            self._client.SetChanAttributeString,
            grpc_types.SetChanAttributeStringRequest(
                task=task, channel=channel, attribute_raw=attribute,
                value=value))

    def set_chan_attribute_uint32(self, task, channel, attribute, value):
        response = self._invoke(
            self._client.SetChanAttributeUInt32,
            grpc_types.SetChanAttributeUInt32Request(
                task=task, channel=channel, attribute_raw=attribute,
                value=value))

    def set_digital_logic_family_power_up_state(
            self, device_name, logic_family):
        response = self._invoke(
            self._client.SetDigitalLogicFamilyPowerUpState,
            grpc_types.SetDigitalLogicFamilyPowerUpStateRequest(
                device_name=device_name, logic_family_raw=logic_family))

    def set_digital_power_up_states(self, device_name, channel_names, state):
        power_up_states = []
        for index in range(len(channel_names)):
            power_up_states.append(grpc_types.DigitalPowerUpChannelsAndState(channel_names=channel_names[index], state=state[index]))
        response = self._invoke(
            self._client.SetDigitalPowerUpStates,
            grpc_types.SetDigitalPowerUpStatesRequest(
                device_name=device_name, power_up_states=power_up_states))

    def set_digital_pull_up_pull_down_states(
            self, device_name, channel_names, state):
        pull_up_pull_down_states = []
        for index in range(len(channel_names)):
            pull_up_pull_down_states.append(grpc_types.DigitalPullUpPullDownChannelsAndState(channel_names=channel_names[index], state=state[index]))
        response = self._invoke(
            self._client.SetDigitalPullUpPullDownStates,
            grpc_types.SetDigitalPullUpPullDownStatesRequest(
                device_name=device_name,
                pull_up_pull_down_states=pull_up_pull_down_states))

    def set_exported_signal_attribute_bool(self, task, attribute, value):
        response = self._invoke(
            self._client.SetExportedSignalAttributeBool,
            grpc_types.SetExportedSignalAttributeBoolRequest(
                task=task, attribute_raw=attribute, value=value))

    def set_exported_signal_attribute_double(self, task, attribute, value):
        response = self._invoke(
            self._client.SetExportedSignalAttributeDouble,
            grpc_types.SetExportedSignalAttributeDoubleRequest(
                task=task, attribute_raw=attribute, value=value))

    def set_exported_signal_attribute_int32(self, task, attribute, value):
        response = self._invoke(
            self._client.SetExportedSignalAttributeInt32,
            grpc_types.SetExportedSignalAttributeInt32Request(
                task=task, attribute_raw=attribute, value_raw=value))

    def set_exported_signal_attribute_string(self, task, attribute, value):
        response = self._invoke(
            self._client.SetExportedSignalAttributeString,
            grpc_types.SetExportedSignalAttributeStringRequest(
                task=task, attribute_raw=attribute, value=value))

    def set_exported_signal_attribute_uint32(self, task, attribute, value):
        response = self._invoke(
            self._client.SetExportedSignalAttributeUInt32,
            grpc_types.SetExportedSignalAttributeUInt32Request(
                task=task, attribute_raw=attribute, value=value))

    def set_read_attribute_bool(self, task, attribute, value):
        response = self._invoke(
            self._client.SetReadAttributeBool,
            grpc_types.SetReadAttributeBoolRequest(
                task=task, attribute_raw=attribute, value=value))

    def set_read_attribute_double(self, task, attribute, value):
        response = self._invoke(
            self._client.SetReadAttributeDouble,
            grpc_types.SetReadAttributeDoubleRequest(
                task=task, attribute_raw=attribute, value=value))

    def set_read_attribute_int32(self, task, attribute, value):
        response = self._invoke(
            self._client.SetReadAttributeInt32,
            grpc_types.SetReadAttributeInt32Request(
                task=task, attribute_raw=attribute, value_raw=value))

    def set_read_attribute_string(self, task, attribute, value):
        response = self._invoke(
            self._client.SetReadAttributeString,
            grpc_types.SetReadAttributeStringRequest(
                task=task, attribute_raw=attribute, value=value))

    def set_read_attribute_uint32(self, task, attribute, value):
        response = self._invoke(
            self._client.SetReadAttributeUInt32,
            grpc_types.SetReadAttributeUInt32Request(
                task=task, attribute_raw=attribute, value=value))

    def set_read_attribute_uint64(self, task, attribute, value):
        response = self._invoke(
            self._client.SetReadAttributeUInt64,
            grpc_types.SetReadAttributeUInt64Request(
                task=task, attribute_raw=attribute, value=value))

    def set_scale_attribute_double(self, scale_name, attribute, value):
        response = self._invoke(
            self._client.SetScaleAttributeDouble,
            grpc_types.SetScaleAttributeDoubleRequest(
                scale_name=scale_name, attribute_raw=attribute, value=value))

    def set_scale_attribute_double_array(self, scale_name, attribute, value):
        response = self._invoke(
            self._client.SetScaleAttributeDoubleArray,
            grpc_types.SetScaleAttributeDoubleArrayRequest(
                scale_name=scale_name, attribute_raw=attribute, value=value))

    def set_scale_attribute_int32(self, scale_name, attribute, value):
        response = self._invoke(
            self._client.SetScaleAttributeInt32,
            grpc_types.SetScaleAttributeInt32Request(
                scale_name=scale_name, attribute_raw=attribute,
                value_raw=value))

    def set_scale_attribute_string(self, scale_name, attribute, value):
        response = self._invoke(
            self._client.SetScaleAttributeString,
            grpc_types.SetScaleAttributeStringRequest(
                scale_name=scale_name, attribute_raw=attribute, value=value))

    def set_timing_attribute_bool(self, task, attribute, value):
        response = self._invoke(
            self._client.SetTimingAttributeBool,
            grpc_types.SetTimingAttributeBoolRequest(
                task=task, attribute_raw=attribute, value=value))

    def set_timing_attribute_double(self, task, attribute, value):
        response = self._invoke(
            self._client.SetTimingAttributeDouble,
            grpc_types.SetTimingAttributeDoubleRequest(
                task=task, attribute_raw=attribute, value=value))

    def set_timing_attribute_ex_bool(
            self, task, device_names, attribute, value):
        response = self._invoke(
            self._client.SetTimingAttributeExBool,
            grpc_types.SetTimingAttributeExBoolRequest(
                task=task, device_names=device_names, attribute_raw=attribute,
                value=value))

    def set_timing_attribute_ex_double(
            self, task, device_names, attribute, value):
        response = self._invoke(
            self._client.SetTimingAttributeExDouble,
            grpc_types.SetTimingAttributeExDoubleRequest(
                task=task, device_names=device_names, attribute_raw=attribute,
                value=value))

    def set_timing_attribute_ex_int32(
            self, task, device_names, attribute, value):
        response = self._invoke(
            self._client.SetTimingAttributeExInt32,
            grpc_types.SetTimingAttributeExInt32Request(
                task=task, device_names=device_names, attribute_raw=attribute,
                value_raw=value))

    def set_timing_attribute_ex_string(
            self, task, device_names, attribute, value):
        response = self._invoke(
            self._client.SetTimingAttributeExString,
            grpc_types.SetTimingAttributeExStringRequest(
                task=task, device_names=device_names, attribute_raw=attribute,
                value=value))

    def set_timing_attribute_ex_uint32(
            self, task, device_names, attribute, value):
        response = self._invoke(
            self._client.SetTimingAttributeExUInt32,
            grpc_types.SetTimingAttributeExUInt32Request(
                task=task, device_names=device_names, attribute_raw=attribute,
                value=value))

    def set_timing_attribute_ex_uint64(
            self, task, device_names, attribute, value):
        response = self._invoke(
            self._client.SetTimingAttributeExUInt64,
            grpc_types.SetTimingAttributeExUInt64Request(
                task=task, device_names=device_names, attribute_raw=attribute,
                value=value))

    def set_timing_attribute_int32(self, task, attribute, value):
        response = self._invoke(
            self._client.SetTimingAttributeInt32,
            grpc_types.SetTimingAttributeInt32Request(
                task=task, attribute_raw=attribute, value_raw=value))

    def set_timing_attribute_string(self, task, attribute, value):
        response = self._invoke(
            self._client.SetTimingAttributeString,
            grpc_types.SetTimingAttributeStringRequest(
                task=task, attribute_raw=attribute, value=value))

    def set_timing_attribute_uint32(self, task, attribute, value):
        response = self._invoke(
            self._client.SetTimingAttributeUInt32,
            grpc_types.SetTimingAttributeUInt32Request(
                task=task, attribute_raw=attribute, value=value))

    def set_timing_attribute_uint64(self, task, attribute, value):
        response = self._invoke(
            self._client.SetTimingAttributeUInt64,
            grpc_types.SetTimingAttributeUInt64Request(
                task=task, attribute_raw=attribute, value=value))

    def set_trig_attribute_bool(self, task, attribute, value):
        response = self._invoke(
            self._client.SetTrigAttributeBool,
            grpc_types.SetTrigAttributeBoolRequest(
                task=task, attribute_raw=attribute, value=value))

    def set_trig_attribute_double(self, task, attribute, value):
        response = self._invoke(
            self._client.SetTrigAttributeDouble,
            grpc_types.SetTrigAttributeDoubleRequest(
                task=task, attribute_raw=attribute, value=value))

    def set_trig_attribute_double_array(self, task, attribute, value):
        response = self._invoke(
            self._client.SetTrigAttributeDoubleArray,
            grpc_types.SetTrigAttributeDoubleArrayRequest(
                task=task, attribute_raw=attribute, value=value))

    def set_trig_attribute_int32(self, task, attribute, value):
        response = self._invoke(
            self._client.SetTrigAttributeInt32,
            grpc_types.SetTrigAttributeInt32Request(
                task=task, attribute_raw=attribute, value_raw=value))

    def set_trig_attribute_int32_array(self, task, attribute, value):
        response = self._invoke(
            self._client.SetTrigAttributeInt32Array,
            grpc_types.SetTrigAttributeInt32ArrayRequest(
                task=task, attribute_raw=attribute, value=value))

    def set_trig_attribute_string(self, task, attribute, value):
        response = self._invoke(
            self._client.SetTrigAttributeString,
            grpc_types.SetTrigAttributeStringRequest(
                task=task, attribute_raw=attribute, value=value))

    def set_trig_attribute_timestamp(self, task, attribute, value):
        response = self._invoke(
            self._client.SetTrigAttributeTimestamp,
            grpc_types.SetTrigAttributeTimestampRequest(
                task=task, attribute_raw=attribute,
                value=convert_time_to_timestamp(value)))

    def set_trig_attribute_uint32(self, task, attribute, value):
        response = self._invoke(
            self._client.SetTrigAttributeUInt32,
            grpc_types.SetTrigAttributeUInt32Request(
                task=task, attribute_raw=attribute, value=value))

    def set_watchdog_attribute_bool(self, task, lines, attribute, value):
        response = self._invoke(
            self._client.SetWatchdogAttributeBool,
            grpc_types.SetWatchdogAttributeBoolRequest(
                task=task, lines=lines, attribute_raw=attribute, value=value))

    def set_watchdog_attribute_double(self, task, lines, attribute, value):
        response = self._invoke(
            self._client.SetWatchdogAttributeDouble,
            grpc_types.SetWatchdogAttributeDoubleRequest(
                task=task, lines=lines, attribute_raw=attribute, value=value))

    def set_watchdog_attribute_int32(self, task, lines, attribute, value):
        response = self._invoke(
            self._client.SetWatchdogAttributeInt32,
            grpc_types.SetWatchdogAttributeInt32Request(
                task=task, lines=lines, attribute_raw=attribute,
                value_raw=value))

    def set_watchdog_attribute_string(self, task, lines, attribute, value):
        response = self._invoke(
            self._client.SetWatchdogAttributeString,
            grpc_types.SetWatchdogAttributeStringRequest(
                task=task, lines=lines, attribute_raw=attribute, value=value))

    def set_write_attribute_bool(self, task, attribute, value):
        response = self._invoke(
            self._client.SetWriteAttributeBool,
            grpc_types.SetWriteAttributeBoolRequest(
                task=task, attribute_raw=attribute, value=value))

    def set_write_attribute_double(self, task, attribute, value):
        response = self._invoke(
            self._client.SetWriteAttributeDouble,
            grpc_types.SetWriteAttributeDoubleRequest(
                task=task, attribute_raw=attribute, value=value))

    def set_write_attribute_int32(self, task, attribute, value):
        response = self._invoke(
            self._client.SetWriteAttributeInt32,
            grpc_types.SetWriteAttributeInt32Request(
                task=task, attribute_raw=attribute, value_raw=value))

    def set_write_attribute_string(self, task, attribute, value):
        response = self._invoke(
            self._client.SetWriteAttributeString,
            grpc_types.SetWriteAttributeStringRequest(
                task=task, attribute_raw=attribute, value=value))

    def set_write_attribute_uint32(self, task, attribute, value):
        response = self._invoke(
            self._client.SetWriteAttributeUInt32,
            grpc_types.SetWriteAttributeUInt32Request(
                task=task, attribute_raw=attribute, value=value))

    def set_write_attribute_uint64(self, task, attribute, value):
        response = self._invoke(
            self._client.SetWriteAttributeUInt64,
            grpc_types.SetWriteAttributeUInt64Request(
                task=task, attribute_raw=attribute, value=value))

    def start_new_file(self, task, file_path):
        response = self._invoke(
            self._client.StartNewFile,
            grpc_types.StartNewFileRequest(task=task, file_path=file_path))

    def start_task(self, task):
        response = self._invoke(
            self._client.StartTask,
            grpc_types.StartTaskRequest(task=task))

    def stop_task(self, task):
        response = self._invoke(
            self._client.StopTask,
            grpc_types.StopTaskRequest(task=task))

    def task_control(self, task, action):
        response = self._invoke(
            self._client.TaskControl,
            grpc_types.TaskControlRequest(task=task, action_raw=action))

    def tristate_output_term(self, output_terminal):
        response = self._invoke(
            self._client.TristateOutputTerm,
            grpc_types.TristateOutputTermRequest(output_terminal=output_terminal))

    def unregister_done_event(self, task):
        response = self._invoke(
            self._client.UnregisterDoneEvent,
            grpc_types.UnregisterDoneEventRequest(task=task))

    def unregister_every_n_samples_event(
            self, task, every_n_samples_event_type):
        response = self._invoke(
            self._client.UnregisterEveryNSamplesEvent,
            grpc_types.UnregisterEveryNSamplesEventRequest(
                task=task,
                every_n_samples_event_type_raw=every_n_samples_event_type))

    def unregister_signal_event(self, task, signal_id):
        response = self._invoke(
            self._client.UnregisterSignalEvent,
            grpc_types.UnregisterSignalEventRequest(task=task, signal_id_raw=signal_id))

    def unreserve_network_device(self, device_name):
        response = self._invoke(
            self._client.UnreserveNetworkDevice,
            grpc_types.UnreserveNetworkDeviceRequest(device_name=device_name))

    def wait_for_valid_timestamp(self, task, timestamp_event, timeout):
        response = self._invoke(
            self._client.WaitForValidTimestamp,
            grpc_types.WaitForValidTimestampRequest(
                task=task, timestamp_event_raw=timestamp_event,
                timeout=timeout))
        return convert_timestamp_to_time(response.timestamp)

    def wait_until_task_done(self, task, time_to_wait):
        response = self._invoke(
            self._client.WaitUntilTaskDone,
            grpc_types.WaitUntilTaskDoneRequest(task=task, time_to_wait=time_to_wait))

    def write_analog_f64(
            self, task, num_samps_per_chan, auto_start, timeout, data_layout,
            write_array):
        _validate_array_dtype(write_array, numpy.float64)
        response = self._invoke(
            self._client.WriteAnalogF64,
            grpc_types.WriteAnalogF64Request(
                task=task, num_samps_per_chan=num_samps_per_chan,
                auto_start=auto_start, timeout=timeout,
                data_layout_raw=data_layout, write_array=write_array.flat))
        return response.samps_per_chan_written

    def write_analog_scalar_f64(self, task, auto_start, timeout, value):
        response = self._invoke(
            self._client.WriteAnalogScalarF64,
            grpc_types.WriteAnalogScalarF64Request(
                task=task, auto_start=auto_start, timeout=timeout,
                value=value))

    def write_binary_i16(
            self, task, num_samps_per_chan, auto_start, timeout, data_layout,
            write_array):
        _validate_array_dtype(write_array, numpy.int16)
        response = self._invoke(
            self._client.WriteBinaryI16,
            grpc_types.WriteBinaryI16Request(
                task=task, num_samps_per_chan=num_samps_per_chan,
                auto_start=auto_start, timeout=timeout,
                data_layout_raw=data_layout, write_array=write_array.flat))
        return response.samps_per_chan_written

    def write_binary_i32(
            self, task, num_samps_per_chan, auto_start, timeout, data_layout,
            write_array):
        _validate_array_dtype(write_array, numpy.int32)
        response = self._invoke(
            self._client.WriteBinaryI32,
            grpc_types.WriteBinaryI32Request(
                task=task, num_samps_per_chan=num_samps_per_chan,
                auto_start=auto_start, timeout=timeout,
                data_layout_raw=data_layout, write_array=write_array.flat))
        return response.samps_per_chan_written

    def write_binary_u16(
            self, task, num_samps_per_chan, auto_start, timeout, data_layout,
            write_array):
        _validate_array_dtype(write_array, numpy.uint16)
        response = self._invoke(
            self._client.WriteBinaryU16,
            grpc_types.WriteBinaryU16Request(
                task=task, num_samps_per_chan=num_samps_per_chan,
                auto_start=auto_start, timeout=timeout,
                data_layout_raw=data_layout, write_array=write_array.flat))
        return response.samps_per_chan_written

    def write_binary_u32(
            self, task, num_samps_per_chan, auto_start, timeout, data_layout,
            write_array):
        _validate_array_dtype(write_array, numpy.uint32)
        response = self._invoke(
            self._client.WriteBinaryU32,
            grpc_types.WriteBinaryU32Request(
                task=task, num_samps_per_chan=num_samps_per_chan,
                auto_start=auto_start, timeout=timeout,
                data_layout_raw=data_layout, write_array=write_array.flat))
        return response.samps_per_chan_written

    def write_ctr_freq(
            self, task, num_samps_per_chan, auto_start, timeout, data_layout,
            frequency, duty_cycle):
        _validate_array_dtype(frequency, numpy.float64)
        _validate_array_dtype(duty_cycle, numpy.float64)
        response = self._invoke(
            self._client.WriteCtrFreq,
            grpc_types.WriteCtrFreqRequest(
                task=task, num_samps_per_chan=num_samps_per_chan,
                auto_start=auto_start, timeout=timeout,
                data_layout_raw=data_layout, frequency=frequency.flat,
                duty_cycle=duty_cycle.flat))
        return response.num_samps_per_chan_written

    def write_ctr_freq_scalar(
            self, task, auto_start, timeout, frequency, duty_cycle):
        response = self._invoke(
            self._client.WriteCtrFreqScalar,
            grpc_types.WriteCtrFreqScalarRequest(
                task=task, auto_start=auto_start, timeout=timeout,
                frequency=frequency, duty_cycle=duty_cycle))

    def write_ctr_ticks(
            self, task, num_samps_per_chan, auto_start, timeout, data_layout,
            high_ticks, low_ticks):
        _validate_array_dtype(high_ticks, numpy.uint32)
        _validate_array_dtype(low_ticks, numpy.uint32)
        response = self._invoke(
            self._client.WriteCtrTicks,
            grpc_types.WriteCtrTicksRequest(
                task=task, num_samps_per_chan=num_samps_per_chan,
                auto_start=auto_start, timeout=timeout,
                data_layout_raw=data_layout, high_ticks=high_ticks.flat,
                low_ticks=low_ticks.flat))
        return response.num_samps_per_chan_written

    def write_ctr_ticks_scalar(
            self, task, auto_start, timeout, high_ticks, low_ticks):
        response = self._invoke(
            self._client.WriteCtrTicksScalar,
            grpc_types.WriteCtrTicksScalarRequest(
                task=task, auto_start=auto_start, timeout=timeout,
                high_ticks=high_ticks, low_ticks=low_ticks))

    def write_ctr_time(
            self, task, num_samps_per_chan, auto_start, timeout, data_layout,
            high_time, low_time):
        _validate_array_dtype(high_time, numpy.float64)
        _validate_array_dtype(low_time, numpy.float64)
        response = self._invoke(
            self._client.WriteCtrTime,
            grpc_types.WriteCtrTimeRequest(
                task=task, num_samps_per_chan=num_samps_per_chan,
                auto_start=auto_start, timeout=timeout,
                data_layout_raw=data_layout, high_time=high_time.flat,
                low_time=low_time.flat))
        return response.num_samps_per_chan_written

    def write_ctr_time_scalar(
            self, task, auto_start, timeout, high_time, low_time):
        response = self._invoke(
            self._client.WriteCtrTimeScalar,
            grpc_types.WriteCtrTimeScalarRequest(
                task=task, auto_start=auto_start, timeout=timeout,
                high_time=high_time, low_time=low_time))

    def write_digital_lines(
            self, task, num_samps_per_chan, auto_start, timeout, data_layout,
            write_array):
        _validate_array_dtype(write_array, bool)
        response = self._invoke(
            self._client.WriteDigitalLines,
            grpc_types.WriteDigitalLinesRequest(
                task=task, num_samps_per_chan=num_samps_per_chan,
                auto_start=auto_start, timeout=timeout,
                data_layout_raw=data_layout,
                write_array=write_array.tobytes()))
        return response.samps_per_chan_written

    def write_digital_scalar_u32(self, task, auto_start, timeout, value):
        response = self._invoke(
            self._client.WriteDigitalScalarU32,
            grpc_types.WriteDigitalScalarU32Request(
                task=task, auto_start=auto_start, timeout=timeout,
                value=value))

    def write_digital_u16(
            self, task, num_samps_per_chan, auto_start, timeout, data_layout,
            write_array):
        _validate_array_dtype(write_array, numpy.uint16)
        response = self._invoke(
            self._client.WriteDigitalU16,
            grpc_types.WriteDigitalU16Request(
                task=task, num_samps_per_chan=num_samps_per_chan,
                auto_start=auto_start, timeout=timeout,
                data_layout_raw=data_layout, write_array=write_array.flat))
        return response.samps_per_chan_written

    def write_digital_u32(
            self, task, num_samps_per_chan, auto_start, timeout, data_layout,
            write_array):
        _validate_array_dtype(write_array, numpy.uint32)
        response = self._invoke(
            self._client.WriteDigitalU32,
            grpc_types.WriteDigitalU32Request(
                task=task, num_samps_per_chan=num_samps_per_chan,
                auto_start=auto_start, timeout=timeout,
                data_layout_raw=data_layout, write_array=write_array.flat))
        return response.samps_per_chan_written

    def write_digital_u8(
            self, task, num_samps_per_chan, auto_start, timeout, data_layout,
            write_array):
        _validate_array_dtype(write_array, numpy.uint8)
        response = self._invoke(
            self._client.WriteDigitalU8,
            grpc_types.WriteDigitalU8Request(
                task=task, num_samps_per_chan=num_samps_per_chan,
                auto_start=auto_start, timeout=timeout,
                data_layout_raw=data_layout,
                write_array=write_array.tobytes()))
        return response.samps_per_chan_written

    def write_id_pin_memory(self, device_name, id_pin_name, data, format_code):
        response = self._invoke(
            self._client.WriteIDPinMemory,
            grpc_types.WriteIDPinMemoryRequest(
                device_name=device_name, id_pin_name=id_pin_name,
                data=data.tobytes(), format_code=format_code))

    def write_raw(self, task, num_samps, auto_start, timeout, write_array):
        _validate_array_dtype(write_array, numpy.generic)
        response = self._invoke(
            self._client.WriteRaw,
            grpc_types.WriteRawRequest(
                task=task, num_samps=num_samps, auto_start=auto_start,
                timeout=timeout, write_array=write_array.tobytes()))
        return response.samps_per_chan_written

    def write_to_teds_from_array(
            self, physical_channel, bit_stream, basic_teds_options):
        response = self._invoke(
            self._client.WriteToTEDSFromArray,
            grpc_types.WriteToTEDSFromArrayRequest(
                physical_channel=physical_channel,
                bit_stream=bit_stream.tobytes(),
                basic_teds_options_raw=basic_teds_options))

    def write_to_teds_from_file(
            self, physical_channel, file_path, basic_teds_options):
        response = self._invoke(
            self._client.WriteToTEDSFromFile,
            grpc_types.WriteToTEDSFromFileRequest(
                physical_channel=physical_channel, file_path=file_path,
                basic_teds_options_raw=basic_teds_options))

    def hash_task_handle(self, task_handle):
        return hash(task_handle.name)

    def get_error_string(self, error_code):
        try:
            # Do not use self._invoke() because it may call back into self.get_error_string().
            response = self._client.GetErrorString(
                grpc_types.GetErrorStringRequest(error_code=error_code))
            if not response.error_string:
                return _UNABLE_TO_LOCATE_ERROR_RESOURCES_ERROR_MESSAGE
            return response.error_string
        except grpc.RpcError:
            _logger.exception('Failed to get error string for error code %d.', error_code)
            return 'Failed to retrieve error description.'

    def read_id_pin_memory(self, device_name, id_pin_name):
        response = self._invoke(
            self._client.ReadIDPinMemory,
            grpc_types.ReadIDPinMemoryRequest(device_name=device_name, id_pin_name=id_pin_name, array_size=0))
        if response.status <= 0:
            self._check_for_error_from_response(response.status)
        response = self._invoke(
            self._client.ReadIDPinMemory,
            grpc_types.ReadIDPinMemoryRequest(device_name=device_name, id_pin_name=id_pin_name, array_size=response.status))
        self._check_for_error_from_response(response.status)
        return list(response.data), response.data_length_read, response.format_code

    def set_runtime_environment(
            self, environment, environment_version, reserved_1, reserved_2):
        raise NotImplementedError

    def internal_get_last_created_chan(self):
        raise NotImplementedError

    def read_analog_waveform(
        self,
        task_handle: object,
        number_of_samples_per_channel: int,
        timeout: float,
        waveform: AnalogWaveform[numpy.float64],
        waveform_attribute_mode: WaveformAttributeMode
    ) -> int:
        return self.read_analog_waveforms(
            task_handle,
            number_of_samples_per_channel,
            timeout,
            [waveform],
            waveform_attribute_mode
        )

    def read_analog_waveforms(
        self,
        task_handle: object,
        number_of_samples_per_channel: int,
        timeout: float,
        waveforms: Sequence[AnalogWaveform[numpy.float64]],
        waveform_attribute_mode: WaveformAttributeMode
    ) -> int:
        assert isinstance(task_handle, Session)
        response = self._invoke(
            self._client.ReadAnalogWaveforms,
            grpc_types.ReadAnalogWaveformsRequest(
                task=task_handle,
                num_samps_per_chan=number_of_samples_per_channel,
                timeout=timeout,
                waveform_attribute_mode_raw=waveform_attribute_mode.value
            ))

        if len(response.waveforms) != len(waveforms):
            raise ValueError(f"Expected {len(waveforms)} waveforms but received {len(response.waveforms)} from server")

        for i, grpc_waveform in enumerate(response.waveforms):
            temp_waveform = float64_analog_waveform_from_protobuf(grpc_waveform)
            waveforms[i].load_data(temp_waveform.scaled_data)

            waveforms[i].scale_mode = temp_waveform.scale_mode
            waveforms[i].timing = temp_waveform.timing
            waveforms[i].extended_properties.clear()
            waveforms[i].extended_properties.update(temp_waveform.extended_properties)

        self._check_for_error_from_response(response.status, samps_per_chan_read=response.samps_per_chan_read)
        return response.samps_per_chan_read

    def read_digital_waveform(
        self,
        task_handle: object,
        number_of_samples_per_channel: int,
        timeout: float,
        waveform: DigitalWaveform[Any],
        waveform_attribute_mode: WaveformAttributeMode
    ) -> int:
        return self.read_digital_waveforms(
            task_handle,
            1,  # channel_count
            number_of_samples_per_channel,
            waveform.signal_count,  # number_of_signals_per_sample
            timeout,
            [waveform],
            waveform_attribute_mode
        )

    def read_digital_waveforms(
        self,
        task_handle: object,
        channel_count: int,
        number_of_samples_per_channel: int,
        number_of_signals_per_sample: int,
        timeout: float,
        waveforms: Sequence[DigitalWaveform[Any]],
        waveform_attribute_mode: WaveformAttributeMode,
    ) -> int:
        assert isinstance(task_handle, Session)
        response = self._invoke(
            self._client.ReadDigitalWaveforms,
            grpc_types.ReadDigitalWaveformsRequest(
                task=task_handle,
                num_samps_per_chan=number_of_samples_per_channel,
                timeout=timeout,
                waveform_attribute_mode_raw=waveform_attribute_mode.value
            ))

        if len(response.waveforms) != len(waveforms):
            raise ValueError(f"Expected {len(waveforms)} waveforms but received {len(response.waveforms)} from server")

        for i, grpc_waveform in enumerate(response.waveforms):
            temp_waveform = digital_waveform_from_protobuf(grpc_waveform)
            data = temp_waveform.data
            if data.dtype != waveforms[i].dtype:
                data = data.view(waveforms[i].dtype)
            waveforms[i].load_data(data)

            waveforms[i].timing = temp_waveform.timing
            waveforms[i].extended_properties.clear()
            waveforms[i].extended_properties.update(temp_waveform.extended_properties)

        self._check_for_error_from_response(response.status, samps_per_chan_read=response.samps_per_chan_read)
        return response.samps_per_chan_read

    def read_new_digital_waveforms(
        self,
        task_handle: object,
        channel_count: int,
        number_of_samples_per_channel: int,
        number_of_signals_per_sample: int,
        timeout: float,
        waveform_attribute_mode: WaveformAttributeMode,
    ) -> Sequence[DigitalWaveform[numpy.uint8]]:
        assert isinstance(task_handle, Session)
        response = self._invoke(
            self._client.ReadDigitalWaveforms,
            grpc_types.ReadDigitalWaveformsRequest(
                task=task_handle,
                num_samps_per_chan=number_of_samples_per_channel,
                timeout=timeout,
                waveform_attribute_mode_raw=waveform_attribute_mode.value
            ))

        waveforms = [digital_waveform_from_protobuf(grpc_waveform) for grpc_waveform in response.waveforms]

        self._check_for_error_from_response(response.status, samps_per_chan_read=response.samps_per_chan_read)
        return waveforms

    def write_analog_waveform(
        self,
        task_handle: object,
        waveform: AnalogWaveform[typing.Any],
        auto_start: bool,
        timeout: float
    ) -> int:
        return self.write_analog_waveforms(task_handle, [waveform], auto_start, timeout)

    def write_analog_waveforms(
        self,
        task_handle: object,
        waveforms: Sequence[AnalogWaveform[typing.Any]],
        auto_start: bool,
        timeout: float
    ) -> int:
        assert isinstance(task_handle, Session)
        num_samps_per_chan = get_num_samps_per_chan(waveforms)

        grpc_waveforms = [float64_analog_waveform_to_protobuf(waveform) for waveform in waveforms]

        response = self._invoke(
            self._client.WriteAnalogWaveforms,
            grpc_types.WriteAnalogWaveformsRequest(
                task=task_handle,
                auto_start=auto_start,
                timeout=timeout,
                waveforms=grpc_waveforms
            ))

        self._check_for_error_from_response(response.status, samps_per_chan_written=response.samps_per_chan_written)
        return response.samps_per_chan_written

    def write_digital_waveform(
        self,
        task_handle: object,
        waveform: DigitalWaveform[Any],
        auto_start: bool,
        timeout: float,
    ) -> int:
        return self.write_digital_waveforms(task_handle, [waveform], auto_start, timeout)

    def write_digital_waveforms(
        self,
        task_handle: object,
        waveforms: Sequence[DigitalWaveform[Any]],
        auto_start: bool,
        timeout: float,
    ) -> int:
        assert isinstance(task_handle, Session)
        num_samps_per_chan = get_num_samps_per_chan(waveforms)

        grpc_waveforms = [digital_waveform_to_protobuf(waveform) for waveform in waveforms]

        response = self._invoke(
            self._client.WriteDigitalWaveforms,
            grpc_types.WriteDigitalWaveformsRequest(
                task=task_handle,
                auto_start=auto_start,
                timeout=timeout,
                waveforms=grpc_waveforms
            ))

        self._check_for_error_from_response(response.status, samps_per_chan_written=response.samps_per_chan_written)
        return response.samps_per_chan_written

def _assign_numpy_array(numpy_array, grpc_array):
    """
    Assigns grpc array to numpy array maintaining the original shape.

    Checks for the instance of grpc_array with bytes, if validated to True,
    the numpy array is assigned to a 1D array of the grpc array.
    """
    grpc_array_size = len(grpc_array)
    if isinstance(grpc_array, bytes):
        assert numpy_array.nbytes >= grpc_array_size
        numpy_array.flat[:grpc_array_size] = numpy.frombuffer(grpc_array, dtype=numpy_array.dtype)
    else:
        assert numpy_array.size >= grpc_array_size
        numpy_array.flat[:grpc_array_size] = grpc_array

def _validate_array_dtype(numpy_array, expected_numpy_array_dtype):
    """Raises TypeError if array type doesn't match with expected numpy.dtype"""
    if expected_numpy_array_dtype != numpy.generic and numpy_array.dtype != expected_numpy_array_dtype:
        raise TypeError(f"array must have data type {expected_numpy_array_dtype}")

def _is_cancelled(ex: Exception) -> bool:
    """Returns True if the given exception is a cancelled RPC exception."""
    return (
        (isinstance(ex, grpc.RpcError) and ex.code() == grpc.StatusCode.CANCELLED)
        or (isinstance(ex, errors.RpcError) and ex.rpc_code == grpc.StatusCode.CANCELLED)
    )

_ERROR_MESSAGES = {
    DAQmxErrors.SAMPLES_NOT_YET_AVAILABLE: 'Some or all of the samples requested have not yet been acquired.\n\nTo wait for the samples to become available use a longer read timeout or read later in your program. To make the samples available sooner, increase the sample rate. If your task uses a start trigger, make sure that your start trigger is configured correctly. It is also possible that you configured the task for external timing, and no clock was supplied. If this is the case, supply an external clock.'
}
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=generated/nidaqmx/_grpc_time.py sha256=788c6bb95fb17659d16be1a0ddf53eca71b8167247a1498aafb89d224feb46de bytes=2083 -->
## FILE: generated/nidaqmx/_grpc_time.py

- repository: `ni/nidaqmx-python`
- source_path: `generated/nidaqmx/_grpc_time.py`
- sha256: `788c6bb95fb17659d16be1a0ddf53eca71b8167247a1498aafb89d224feb46de`
- bytes: 2083

````python
from __future__ import annotations

from datetime import datetime as std_datetime, timezone, tzinfo as dt_tzinfo

from google.protobuf.timestamp_pb2 import Timestamp as GrpcTimestamp
from hightime import datetime as ht_datetime, timedelta as ht_timedelta

from nidaqmx._time import _convert_to_desired_timezone

# 66 years, 17 leap days = 24107 days = 2082844800 seconds
_BIAS_FROM_1970_EPOCH = 2082844800

_NS_PER_S = 10**9
_NS_PER_US = 10**3

_YS_PER_US = 10**18
_YS_PER_NS = 10**15
_YS_PER_FS = 10**9

_EPOCH_1970 = ht_datetime(1970, 1, 1, tzinfo=timezone.utc)


def convert_time_to_timestamp(  # noqa: D103 - Missing docstring in public function (auto-generated noqa)
    dt: std_datetime | ht_datetime, ts: GrpcTimestamp | None = None
) -> GrpcTimestamp:
    seconds_since_1970 = 0

    if ts is None:
        ts = GrpcTimestamp()

    if isinstance(dt, ht_datetime):
        seconds_since_1970 = int((dt - _EPOCH_1970).precision_total_seconds())
        total_yoctoseconds = dt.yoctosecond
        total_yoctoseconds += dt.femtosecond * _YS_PER_FS
        total_yoctoseconds += dt.microsecond * _YS_PER_US
        nanos, remainder_yoctoseconds = divmod(total_yoctoseconds, _YS_PER_NS)
        # round up, if necessary
        if remainder_yoctoseconds >= _YS_PER_NS / 2:
            nanos += 1
    else:
        seconds_since_1970 = int((dt - _EPOCH_1970).total_seconds())
        nanos = dt.microsecond * _NS_PER_US

    ts.FromNanoseconds(seconds_since_1970 * _NS_PER_S + nanos)
    return ts


def convert_timestamp_to_time(  # noqa: D103 - Missing docstring in public function (auto-generated noqa)
    ts: GrpcTimestamp, tzinfo: dt_tzinfo | None = None
) -> ht_datetime:
    total_nanos = ts.ToNanoseconds()
    seconds, nanos = divmod(total_nanos, _NS_PER_S)
    # Convert the nanoseconds to yoctoseconds.
    total_yoctoseconds = int(round(_YS_PER_NS * nanos))
    dt = _EPOCH_1970 + ht_timedelta(seconds=seconds) + ht_timedelta(yoctoseconds=total_yoctoseconds)
    return _convert_to_desired_timezone(dt, tzinfo)
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=generated/nidaqmx/_install_daqmx.py sha256=f35314f917e393e4c6edacc86454a72c005293fed3aa9d9dc9fbbe698ae1e529 bytes=18858 -->
## FILE: generated/nidaqmx/_install_daqmx.py

- repository: `ni/nidaqmx-python`
- source_path: `generated/nidaqmx/_install_daqmx.py`
- sha256: `f35314f917e393e4c6edacc86454a72c005293fed3aa9d9dc9fbbe698ae1e529`
- bytes: 18858

````python
from __future__ import annotations

import contextlib
import importlib.resources as pkg_resources
import json
import logging
import os
import re
import subprocess  # nosec: B404
import sys
import tempfile
import zipfile
from collections.abc import Generator
from urllib.parse import urlparse

import click
import requests

if sys.platform.startswith("win"):
    import winreg
elif sys.platform.startswith("linux"):
    import distro

    from nidaqmx._linux_installation_commands import (
        LINUX_COMMANDS,
        get_linux_installation_commands,
    )

_logger = logging.getLogger(__name__)

METADATA_FILE = "_installer_metadata.json"
_NETWORK_TIMEOUT_IN_SECONDS = 60


def _parse_version(version: str) -> tuple[int, ...]:
    """Split the version string into a tuple of integers.

    >>> _parse_version("23.8.0")
    (23, 8, 0)
    >>> _parse_version("24.0.0")
    (24, 0, 0)
    >>> _parse_version("invalid_version")
    Traceback (most recent call last):
    ...
    click.exceptions.ClickException: Invalid version format found
    """
    try:
        return tuple(int(part) for part in version.split("."))
    except ValueError as e:
        _logger.info("Failed to parse version.", exc_info=True)
        raise click.ClickException(f"Invalid version number '{version}'.") from e


def _get_daqmx_installed_version() -> str | None:
    """Check for existing installation of NI-DAQmx."""
    if sys.platform.startswith("win"):
        try:
            _logger.debug("Reading the registry entries to get installed DAQmx version")
            with winreg.OpenKeyEx(
                winreg.HKEY_LOCAL_MACHINE,
                r"SOFTWARE\National Instruments\NI-DAQmx\CurrentVersion",
                0,
                winreg.KEY_READ | winreg.KEY_WOW64_32KEY,
            ) as daqmx_reg_key:
                product_name = winreg.QueryValueEx(daqmx_reg_key, "ProductName")[0]
                product_version = winreg.QueryValueEx(daqmx_reg_key, "Version")[0]

            if product_name == "NI-DAQmx":
                _logger.info(
                    "Found registry entries for Product Name: %s and version %s",
                    product_name,
                    product_version,
                )
                return product_version
            return None
        except FileNotFoundError:
            _logger.info("No existing NI-DAQmx installation found.")
            return None
        except PermissionError as e:
            _logger.info("Failed to read the registry key.", exc_info=True)
            raise click.ClickException(
                f"Permission denied while getting the installed NI-DAQmx version.\nDetails: {e}"
            ) from e
        except OSError as e:
            _logger.info("Failed to read the registry key.", exc_info=True)
            raise click.ClickException(
                f"An OS error occurred while getting the installed NI-DAQmx version.\nDetails: {e}"
            ) from e
    elif sys.platform.startswith("linux"):
        try:
            distribution = distro.id()
            _logger.debug("Checking for installed NI-DAQmx version")
            commands_info = LINUX_COMMANDS[distribution]
            query_command = commands_info.get_daqmx_version
            # Run the package query command defined by _linux_installation_commands.py.
            query_output = subprocess.run(
                query_command, stdout=subprocess.PIPE, text=True
            ).stdout  # nosec: B603

            if distribution == "ubuntu":
                version_match = re.search(r"ii\s+ni-daqmx\s+(\d+\.\d+\.\d+)", query_output)
            elif distribution == "opensuse" or distribution == "rhel":
                version_match = re.search(r"ni-daqmx-(\d+\.\d+\.\d+)", query_output)
            else:
                raise click.ClickException(f"Unsupported distribution '{distribution}'")
            if version_match is None:
                return None
            else:
                installed_version = version_match.group(1)
                _logger.info("Found installed NI-DAQmx version: %s", installed_version)
                return installed_version

        except subprocess.CalledProcessError as e:
            _logger.info("Failed to get installed NI-DAQmx version.", exc_info=True)
            raise click.ClickException(
                f"An error occurred while getting the installed NI-DAQmx version.\nCommand returned non-zero exit status '{e.returncode}'."
            ) from e
    else:
        raise NotImplementedError("This function is only supported on Windows and Linux.")


# Creating a temp file that we then close and yield - this is used to allow subprocesses to access
@contextlib.contextmanager
def _multi_access_temp_file(*, suffix: str = ".exe", delete: bool = True) -> Generator[str]:
    """Context manager for creating a temporary file."""
    try:
        temp_file = tempfile.NamedTemporaryFile(suffix=suffix, delete=False, mode="w")
        temp_file.close()
        _logger.debug("Created temp file: %s", temp_file.name)
    except Exception as e:
        _logger.info("Failed to create temporary file.", exc_info=True)
        raise click.ClickException(
            f"Failed to create temporary file '{temp_file.name}'.\nDetails: {e}"
        ) from e

    try:
        yield temp_file.name
    finally:
        if delete:
            try:
                _logger.debug("Deleting temp file: %s", temp_file.name)
                os.unlink(temp_file.name)
            except ValueError as e:
                _logger.info("Failed to delete temporary file.", exc_info=True)
                raise click.ClickException(
                    f"Failed to delete temporary file '{temp_file.name}'.\nDetails: {e}"
                ) from e


def _load_data(
    json_data: str, platform: str
) -> tuple[str | None, str | None, str | None, list[str] | None]:
    """Load data from JSON string and extract Windows metadata.

    >>> json_data = '{"Windows": [{"Location": "path/to/windows/driver", "Version": "24.0", "Release": "2024Q1", "supportedOS": ["Windows 11"]}], "Linux": []}'
    >>> _load_data(json_data, "Windows")
    ('path/to/windows/driver', '24.0', '2024Q1', ['Windows 11'])

    >>> json_data = '{"Windows": [], "Linux": [{"Location": "path/to/linux/driver", "Version": "24.0", "Release": "2024Q1", "supportedOS": ["ubuntu 20.04 ", "rhel 9"]}]}'
    >>> _load_data(json_data, "Linux")
    ('path/to/linux/driver', '24.0', '2024Q1', ['ubuntu 20.04', 'rhel 9'])

    >>> json_data = '{"Windows": [{"Location": "path/to/windows/driver", "Version": "24.0", "Release": "2024Q1", "supportedOS": ["Windows 11"]}], "Linux": []}'
    >>> _load_data(json_data, "Linux")
    Traceback (most recent call last):
    click.exceptions.ClickException: Unable to fetch driver details

    >>> json_data = 'invalid json'
    >>> _load_data(json_data, "Windows")
    Traceback (most recent call last):
    click.exceptions.ClickException: Failed to parse the driver metadata.
    Details: Expecting value: line 1 column 1 (char 0)

    >>> json_data = '{"Windows": [{"Location": "path/to/windows/driver", "Version": "24.0", "Release": "2024Q1", "supportedOS": ["Windows 11"]}], "Linux": []}'
    >>> _load_data(json_data, "macOS")
    Traceback (most recent call last):
    click.exceptions.ClickException: Unsupported os 'macOS'

    """  # noqa: W505 - doc line too long (159 > 100 characters) (auto-generated noqa)
    try:
        if platform == "Windows":
            metadata = json.loads(json_data).get("Windows", [])
        elif platform == "Linux":
            metadata = json.loads(json_data).get("Linux", [])
        else:
            raise click.ClickException(f"Unsupported os '{platform}'")
    except json.JSONDecodeError as e:
        _logger.info("Failed to parse the json data.", exc_info=True)
        raise click.ClickException(f"Failed to parse the driver metadata.\nDetails: {e}") from e

    for metadata_entry in metadata:
        location: str | None = metadata_entry.get("Location")
        version: str | None = metadata_entry.get("Version")
        release: str | None = metadata_entry.get("Release")
        supported_os: list[str] | None = metadata_entry.get("supportedOS")
        _logger.debug("From metadata file found location %s and version %s.", location, version)
        if location and version:
            return location, version, release, supported_os
    raise click.ClickException(f"Unable to fetch driver details")


def _get_driver_details(
    platform: str,
) -> tuple[str | None, str | None, str | None, list[str] | None]:
    """Parse the JSON data and retrieve the download link and version information."""
    try:
        with pkg_resources.open_text(__package__, METADATA_FILE) as json_file:
            _logger.debug("Opening the metadata file %s.", METADATA_FILE)
            location, version, release, supported_os = _load_data(json_file.read(), platform)
        return location, version, release, supported_os

    except click.ClickException:
        raise
    except Exception as e:
        _logger.info("Failed to get driver metadata.", exc_info=True)
        raise click.ClickException(
            f"An error occurred while getting the driver metadata.\nDetails: {e}"
        ) from e


def _install_daqmx_driver_windows_core(download_url: str) -> None:
    """Download and launch NI-DAQmx Driver installation in an interactive mode."""
    _validate_download_url(download_url)
    try:
        with _multi_access_temp_file() as temp_file:
            _logger.info("Downloading Driver to %s", temp_file)
            response = requests.get(download_url, timeout=_NETWORK_TIMEOUT_IN_SECONDS)
            response.raise_for_status()
            with open(temp_file, "wb") as f:
                f.write(response.content)
            _logger.info("Installing NI-DAQmx")
            # Run the installer that we just downloaded from https://download.ni.com.
            subprocess.run([temp_file], shell=True, check=True)  # nosec: B602
    except subprocess.CalledProcessError as e:
        _logger.info("Failed to install NI-DAQmx driver.", exc_info=True)
        raise click.ClickException(
            f"An error occurred while installing the NI-DAQmx driver. Command returned non-zero exit status '{e.returncode}'."
        ) from e
    except requests.RequestException as e:
        _logger.info("Failed to download NI-DAQmx driver.", exc_info=True)
        raise click.ClickException(f"Failed to download the NI-DAQmx driver.\nDetails: {e}") from e
    except Exception as e:
        _logger.info("Failed to install NI-DAQmx driver.", exc_info=True)
        raise click.ClickException(f"Failed to install the NI-DAQmx driver.\nDetails: {e}") from e


def _install_daqmx_driver_linux_core(download_url: str, release: str) -> None:
    """Download NI Linux Device Drivers and install NI-DAQmx on Linux OS."""
    if sys.platform.startswith("linux"):
        _validate_download_url(download_url)
        try:
            with _multi_access_temp_file(suffix=".zip") as temp_file:
                _logger.info("Downloading Driver to %s", temp_file)
                response = requests.get(download_url, timeout=_NETWORK_TIMEOUT_IN_SECONDS)
                response.raise_for_status()
                with open(temp_file, "wb") as f:
                    f.write(response.content)

                with tempfile.TemporaryDirectory() as temp_folder:
                    directory_to_extract_to = temp_folder

                    _logger.info("Unzipping the downloaded file to %s", directory_to_extract_to)

                    with zipfile.ZipFile(temp_file, "r") as zip_ref:
                        zip_ref.extractall(directory_to_extract_to)

                    _logger.info("Installing NI-DAQmx")
                    for command in get_linux_installation_commands(
                        directory_to_extract_to, distro.id(), distro.version(), release
                    ):
                        print("\nRunning command:", " ".join(command))
                        # Run the commands defined in
                        # _linux_installation_commands.py to install the package
                        # that we just downloaded from https://download.ni.com.
                        subprocess.run(command, check=True)  # nosec: B603

            # Check if the installation was successful
            if not _get_daqmx_installed_version():
                raise click.ClickException(
                    "Failed to install NI-DAQmx driver. All installation commands ran successfully but the driver is not installed."
                )
            else:
                print("NI-DAQmx driver installed successfully. Please reboot the system.")

        except subprocess.CalledProcessError as e:
            _logger.info("Failed to install NI-DAQmx driver.", exc_info=True)
            raise click.ClickException(
                f"An error occurred while installing the NI-DAQmx driver. Command returned non-zero exit status '{e.returncode}'."
            ) from e
        except requests.RequestException as e:
            _logger.info("Failed to download NI-DAQmx driver.", exc_info=True)
            raise click.ClickException(
                f"Failed to download the NI-DAQmx driver.\nDetails: {e}"
            ) from e
        except Exception as e:
            _logger.info("Failed to install NI-DAQmx driver.", exc_info=True)
            raise click.ClickException(
                f"Failed to install the NI-DAQmx driver.\nDetails: {e}"
            ) from e
    else:
        raise NotImplementedError("This function is only supported on Linux.")


def _validate_download_url(download_url: str) -> None:
    """Validate that the download URL uses https and points to a trusted site."""
    parsed_url = urlparse(download_url)
    if parsed_url.scheme != "https" or parsed_url.netloc != "download.ni.com":
        raise click.ClickException(f"Unsupported download URL: {download_url}")


def _ask_user_confirmation(user_message: str) -> bool:
    """Prompt for user confirmation."""
    while True:
        response = input(user_message + " (yes/no): ").strip().lower()
        if response in ["yes", "y"]:
            return True
        elif response in ["no", "n"]:
            return False
        else:
            print("Please enter 'yes' or 'no'.")


def _upgrade_daqmx_user_confirmation(
    installed_version: str,
    latest_version: str,
    release: str,
) -> bool:
    """Confirm with the user and return the user response."""
    _logger.debug("Entering _upgrade_daqmx_user_confirmation")
    installed_parts = _parse_version(installed_version)
    latest_parts = _parse_version(latest_version)
    if installed_parts >= latest_parts:
        print(
            f"Installed NI-DAQmx version ({installed_version}) is up to date. (Expected {latest_version} ({release}) or newer.)"
        )
        return False
    is_upgrade = _ask_user_confirmation(
        f"Installed NI-DAQmx version is {installed_version}. Latest version available is {latest_version} ({release}). Do you want to upgrade?"
    )
    return is_upgrade


def _fresh_install_daqmx_user_confirmation(
    latest_version: str,
    release: str,
) -> bool:
    """Confirm with the user and return the user response."""
    _logger.debug("Entering _fresh_install_daqmx_user_confirmation")
    return _ask_user_confirmation(
        f"Latest NI-DAQmx version available is {latest_version} ({release}). Do you want to install?"
    )


def _is_distribution_supported() -> None:
    """Raises an exception if the linux distribution and its version are not supported."""
    if sys.platform.startswith("linux"):
        dist_name = distro.id()
        dist_version = distro.version()

        # For rhel, we only need the major version
        if dist_name == "rhel":
            dist_version = dist_version.split(".")[0]
        dist_name_and_version = dist_name + " " + dist_version

        download_url, latest_version, release, supported_os = _get_driver_details("Linux")
        if supported_os is None:
            raise ValueError("supported_os cannot be None")

        # Check if the platform is one of the supported ones
        if dist_name_and_version in supported_os:
            _logger.info(f"The platform is supported: {dist_name_and_version}")
        else:
            raise click.ClickException(f"The platform {dist_name_and_version} is not supported.")
    else:
        raise NotImplementedError("This function is only supported on Linux.")


def _install_daqmx_driver():
    """Install the NI-DAQmx driver."""
    if sys.platform.startswith("win"):
        _logger.info("Windows platform detected")
        platform = "Windows"
    elif sys.platform.startswith("linux"):
        _logger.info("Linux platform detected")
        platform = "Linux"

        try:
            _is_distribution_supported()
        except Exception as e:
            raise click.ClickException(f"Distribution not supported.\nDetails: {e}") from e

    else:
        raise click.ClickException(
            f"The 'installdriver' command is supported only on Windows and Linux."
        )

    installed_version = _get_daqmx_installed_version()
    download_url, latest_version, release, _ = _get_driver_details(platform)

    if not download_url:
        raise click.ClickException(f"Failed to fetch the download url.")
    if not release or not latest_version:
        raise click.ClickException(f"Failed to fetch the release version string.")
    else:
        if installed_version:
            user_response = _upgrade_daqmx_user_confirmation(
                installed_version, latest_version, release
            )
        else:
            user_response = _fresh_install_daqmx_user_confirmation(latest_version, release)

        if user_response:
            if platform == "Linux":
                _install_daqmx_driver_linux_core(download_url, release)
            else:
                _install_daqmx_driver_windows_core(download_url)


def installdriver() -> None:
    """Download and launch NI-DAQmx Driver installation in an interactive mode."""
    try:
        _install_daqmx_driver()
    except click.ClickException:
        raise
    except Exception as e:
        _logger.info("Failed to install driver.", exc_info=True)
        raise click.ClickException(
            f"An error occurred during the installation of the NI-DAQmx driver.\nDetails: {e}"
        ) from e
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=generated/nidaqmx/_installer_metadata.json sha256=1c15f26832c8bf3716fc0665faf4442a530334ab41c710956de6236645c2dc4c bytes=1181 -->
## FILE: generated/nidaqmx/_installer_metadata.json

- repository: `ni/nidaqmx-python`
- source_path: `generated/nidaqmx/_installer_metadata.json`
- sha256: `1c15f26832c8bf3716fc0665faf4442a530334ab41c710956de6236645c2dc4c`
- bytes: 1181

````json
{
    "Windows": [
        {
            "Version": "26.3.0",
            "Release": "2026Q2",
            "Location": "https://download.ni.com/support/nipkg/products/ni-d/ni-daqmx/26.3/online/ni-daqmx_26.3_online.exe",
            "supportedOS": [
                "Windows 11",
                "Windows Server 2025",
                "Windows Server 2022 64-bit",
                "Windows 10 IoT Enterprise 2021"
            ]
        }
    ],
    "Linux": [
        {
            "Version": "26.3.0",
            "Release": "2026Q2",
            "_comment": "Location url must be of the format 'https://download.ni.com/support/softlib/MasterRepository/LinuxDrivers<Release>/NILinux<Release>DeviceDrivers.zip'. Any change to the format will require a change in the code.",
            "Location": "https://download.ni.com/support/softlib/MasterRepository/LinuxDrivers2026Q2/NILinux2026Q2DeviceDrivers.zip",
            "supportedOS": [
                "ubuntu 22.04",
                "ubuntu 24.04",
                "rhel 9",
                "rhel 10",
                "opensuse 15.6",
                "opensuse 16.0"
            ]
        }
    ]
}
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=generated/nidaqmx/_lib.py sha256=cfa76149d33eaf294fc5568c262b0049761ceda4337c879529742696719dd40c bytes=8182 -->
## FILE: generated/nidaqmx/_lib.py

- repository: `ni/nidaqmx-python`
- source_path: `generated/nidaqmx/_lib.py`
- sha256: `cfa76149d33eaf294fc5568c262b0049761ceda4337c879529742696719dd40c`
- bytes: 8182

````python
from __future__ import annotations

import ctypes
import locale
import sys
import threading
from ctypes.util import find_library
from typing import TYPE_CHECKING, cast

from decouple import config
from numpy.ctypeslib import ndpointer

from nidaqmx.errors import (
    DaqFunctionNotSupportedError,
    DaqNotFoundError,
    DaqNotSupportedError,
)

if TYPE_CHECKING:
    from typing_extensions import TypeAlias


_DAQ_NOT_FOUND_MESSAGE = (
    "Could not find an installation of NI-DAQmx. Please ensure that NI-DAQmx "
    "is installed on this machine or contact National Instruments for support."
)

_DAQ_NOT_SUPPORTED_MESSAGE = (
    "NI-DAQmx Python is not supported on this platform: {0}. Please "
    "direct any questions or feedback to National Instruments."
)

_FUNCTION_NOT_SUPPORTED_MESSAGE = (
    'The NI-DAQmx function "{0}" is not supported in this version '
    "of NI-DAQmx. Visit ni.com/downloads to upgrade."
)


class c_bool32(  # noqa: N801 - class name 'c_bool32' should use CapWords convention (auto-generated noqa)
    ctypes.c_uint
):
    """Specifies a custom ctypes data type to represent 32-bit booleans."""

    # typeshed specifies that _SimpleCData[_T].value is an instance variable with type _T, so
    # accessing it with the descriptor protocol via its class results in "error: Access to generic
    # instance variables via class is ambiguous".

    def _getter(self):
        return bool(ctypes.c_uint.value.__get__(self))  # type: ignore

    def _setter(self, val):
        ctypes.c_uint.value.__set__(self, int(val))  # type: ignore

    value: bool = cast(bool, property(_getter, _setter))

    del _getter, _setter


class CtypesByteString:
    """Custom argtype that automatically converts unicode strings to encoding used by the C API."""

    @classmethod
    def from_param(  # noqa: D102 - Missing docstring in public method (auto-generated noqa)
        cls, param
    ):
        if isinstance(param, str):
            param = param.encode(lib_importer.encoding)
        return ctypes.c_char_p(param)


ctypes_byte_str: TypeAlias = CtypesByteString


def wrapped_ndpointer(*args, **kwargs):
    """Wraps numpy.ctypeslib.ndpointer in order to allow passing None.

    Taken from http://stackoverflow.com/questions/32120178
    """
    base = ndpointer(*args, **kwargs)

    def from_param(cls, obj):
        if obj is None:
            return obj
        return base.from_param(obj)

    return type(base.__name__, (base,), {"from_param": classmethod(from_param)})


class DaqFunctionImporter:
    """Wraps the function getter function of a ctypes library.

    Allows the NI-DAQmx Python API to fail elegantly if a function is not
    supported in the current version of the API.
    """

    def __init__(self, library):
        """Initialize a new DaqFunctionImporter."""
        self._library = library
        self._lib_lock = threading.Lock()

    def __getattr__(  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        self, function
    ):
        try:
            c_func = getattr(self._library, function)
            if not hasattr(c_func, "arg_lock"):
                with self._lib_lock:
                    if not hasattr(c_func, "arg_lock"):
                        c_func.arg_lock = threading.Lock()
            return c_func
        except AttributeError:
            raise DaqFunctionNotSupportedError(_FUNCTION_NOT_SUPPORTED_MESSAGE.format(function))


CalHandle: TypeAlias = ctypes.c_uint
"""Calibration handle.

NIDAQmx.h defines CalHandle as a typedef for uInt32.
"""

TaskHandle: TypeAlias = ctypes.c_void_p
"""Task handle.

NIDAQmx.h defines TaskHandle as a typedef for void*.

From NI-DAQmx versions 7.0 to 8.8, TaskHandle was defined as uInt32. In NI-DAQmx 8.9, it was
changed to void* in order to support 64-bit platforms. This change did not break binary
compatibility because uInt32 and void* are the same size for 32-bit applications.
"""


def get_encoding_from_locale() -> str:
    """Gets the current locale encoding handling cases where it is unset."""
    _, encoding = locale.getlocale()
    return encoding or "ascii"


class DaqLibImporter:
    """Encapsulates NI-DAQmx library importing and handle type parsing logic."""

    def __init__(self):
        """Initialize a new DaqLibImporter."""
        self._windll = None
        self._cdll = None
        self._cal_handle = None
        self._task_handle = None
        self._encoding = None

    @property
    def windll(self):  # noqa: D102 - Missing docstring in public method (auto-generated noqa)
        if self._windll is None:
            self._import_lib()
        return self._windll

    @property
    def cdll(self):  # noqa: D102 - Missing docstring in public method (auto-generated noqa)
        if self._cdll is None:
            self._import_lib()
        return self._cdll

    @property
    def task_handle(  # noqa: D102 - Missing docstring in public method (auto-generated noqa)
        self,
    ) -> type:
        return TaskHandle

    @property
    def cal_handle(  # noqa: D102 - Missing docstring in public method (auto-generated noqa)
        self,
    ) -> type:
        return CalHandle

    @property
    def encoding(self):  # noqa: D102 - Missing docstring in public method (auto-generated noqa)
        if self._encoding is None:
            self._import_lib()
        return self._encoding

    def _import_lib(self):
        """Determines the location of and loads the NI-DAQmx CAI DLL."""
        self._windll = None
        self._cdll = None
        self._encoding = None

        windll = None
        cdll = None
        encoding = None

        if sys.platform.startswith("win"):

            def _load_lib(library_name: str):
                windll = ctypes.windll.LoadLibrary(library_name)
                cdll = ctypes.cdll.LoadLibrary(library_name)
                return windll, cdll

            # Feature Toggle to load nicaiu.dll or nicai_utf8.dll
            # The Feature Toggle can be set in the .env file
            nidaqmx_c_library = config("NIDAQMX_C_LIBRARY", default=None)

            if nidaqmx_c_library is not None:
                try:
                    if nidaqmx_c_library == "nicaiu":
                        windll, cdll = _load_lib("nicaiu")
                        encoding = get_encoding_from_locale()
                    elif nidaqmx_c_library == "nicai_utf8":
                        windll, cdll = _load_lib("nicai_utf8")
                        encoding = "utf-8"
                    else:
                        raise ValueError(
                            f"Unsupported NIDAQMX_C_LIBRARY value: {nidaqmx_c_library}"
                        )
                except OSError as e:
                    raise DaqNotFoundError(_DAQ_NOT_FOUND_MESSAGE) from e
            else:
                try:
                    windll, cdll = _load_lib("nicai_utf8")
                    encoding = "utf-8"
                except OSError:
                    # Fallback to nicaiu.dll if nicai_utf8.dll cannot be loaded
                    try:
                        windll, cdll = _load_lib("nicaiu")
                        encoding = get_encoding_from_locale()
                    except OSError as e:
                        raise DaqNotFoundError(_DAQ_NOT_FOUND_MESSAGE) from e
        elif sys.platform.startswith("linux"):
            library_path = find_library("nidaqmx")
            if library_path is not None:
                cdll = ctypes.cdll.LoadLibrary(library_path)
                windll = cdll
                encoding = get_encoding_from_locale()
            else:
                raise DaqNotFoundError(_DAQ_NOT_FOUND_MESSAGE)
        else:
            raise DaqNotSupportedError(_DAQ_NOT_SUPPORTED_MESSAGE.format(sys.platform))

        self._windll = DaqFunctionImporter(windll)
        self._cdll = DaqFunctionImporter(cdll)
        self._encoding = encoding


lib_importer = DaqLibImporter()
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=generated/nidaqmx/_lib_time.py sha256=10d6a0f4dc4f571415e9308226ab124c05cdc1abd2d415b53de39d3149524fba bytes=3282 -->
## FILE: generated/nidaqmx/_lib_time.py

- repository: `ni/nidaqmx-python`
- source_path: `generated/nidaqmx/_lib_time.py`
- sha256: `10d6a0f4dc4f571415e9308226ab124c05cdc1abd2d415b53de39d3149524fba`
- bytes: 3282

````python
from __future__ import annotations

import ctypes
import functools
from datetime import datetime as std_datetime, timezone, tzinfo as dt_tzinfo

from hightime import datetime as ht_datetime, timedelta as ht_timedelta

from nidaqmx._time import _convert_to_desired_timezone


@functools.total_ordering
class AbsoluteTime(  # noqa: D101 - Missing docstring in public class (auto-generated noqa)
    ctypes.Structure
):
    # Please visit ni.com/info and enter the Info Code NI_BTF for detailed information.
    # The summary is:
    #    * lsb - positive fractions (2^-64) of a second
    #    * msb - number of whole seconds since 12am, Friday, January 1, 1904, UTC

    _pack_ = 4
    _fields_ = [("lsb", ctypes.c_uint64), ("msb", ctypes.c_int64)]

    # 66 years, 17 leap days = 24107 days = 2082844800 seconds
    _BIAS_FROM_1970_EPOCH = 2082844800
    _NUM_SUBSECONDS = 2**64
    _US_PER_S = 10**6
    _YS_PER_S = 10**24
    _YS_PER_US = 10**18
    _YS_PER_FS = 10**9

    MAX_FS = 10**9
    MAX_YS = 10**9

    _EPOCH_1904 = ht_datetime(1904, 1, 1, tzinfo=timezone.utc)

    @classmethod
    def from_datetime(  # noqa: D102 - Missing docstring in public method (auto-generated noqa)
        cls, dt: std_datetime | ht_datetime
    ) -> AbsoluteTime:
        seconds_since_1904 = 0

        # Convert the subseconds.
        if isinstance(dt, ht_datetime):
            seconds_since_1904 = int((dt - AbsoluteTime._EPOCH_1904).precision_total_seconds())
            total_yoctoseconds = dt.yoctosecond
            total_yoctoseconds += dt.femtosecond * AbsoluteTime._YS_PER_FS
            total_yoctoseconds += dt.microsecond * AbsoluteTime._YS_PER_US
            lsb = int(
                round(AbsoluteTime._NUM_SUBSECONDS * total_yoctoseconds / AbsoluteTime._YS_PER_S)
            )
        else:
            seconds_since_1904 = int((dt - AbsoluteTime._EPOCH_1904).total_seconds())
            lsb = int(round(AbsoluteTime._NUM_SUBSECONDS * dt.microsecond / AbsoluteTime._US_PER_S))

        return AbsoluteTime(lsb=lsb, msb=seconds_since_1904)

    def to_datetime(  # noqa: D102 - Missing docstring in public method (auto-generated noqa)
        self, tzinfo: dt_tzinfo | None = None
    ) -> ht_datetime:
        total_yoctoseconds = int(
            round(AbsoluteTime._YS_PER_S * self.lsb / AbsoluteTime._NUM_SUBSECONDS)
        )
        dt = (
            AbsoluteTime._EPOCH_1904
            + ht_timedelta(seconds=self.msb)
            + ht_timedelta(yoctoseconds=total_yoctoseconds)
        )
        return _convert_to_desired_timezone(dt, tzinfo)

    def __str__(  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        self,
    ) -> str:
        return f"AbsoluteTime(lsb=0x{self.lsb:x}, msb=0x{self.msb:x})"

    def __eq__(  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        self, other
    ) -> bool:
        return self.msb == other.msb and self.lsb == other.lsb

    def __lt__(  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        self, other
    ) -> bool:
        if self.msb == other.msb:
            return self.lsb < other.lsb
        else:
            return self.msb < other.msb
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=generated/nidaqmx/_library_interpreter.py sha256=a496639fab31258e78316f4a73b641fc061c0bc4230cae54a65a51f3fd046b3f bytes=312126 -->
## FILE: generated/nidaqmx/_library_interpreter.py

- repository: `ni/nidaqmx-python`
- source_path: `generated/nidaqmx/_library_interpreter.py`
- sha256: `a496639fab31258e78316f4a73b641fc061c0bc4230cae54a65a51f3fd046b3f`
- bytes: 312126

````python
# Do not edit this file; it was automatically generated.

from __future__ import annotations
import ctypes
import logging
import numpy
import platform
import warnings
from enum import Enum
from datetime import timezone
from hightime import datetime as ht_datetime
from hightime import timedelta as ht_timedelta
from typing import Any, TYPE_CHECKING

from collections.abc import Callable, Sequence

from nidaqmx._base_interpreter import BaseEventHandler, BaseInterpreter
from nidaqmx._lib import lib_importer, ctypes_byte_str, c_bool32, wrapped_ndpointer, TaskHandle
from nidaqmx.constants import FillMode, WaveformAttributeMode
from nidaqmx.error_codes import DAQmxErrors, DAQmxWarnings
from nidaqmx.errors import DaqError, DaqFunctionNotSupportedError, DaqReadError, DaqWarning, DaqWriteError
from nidaqmx.types import DriverVersion
from nidaqmx._lib_time import AbsoluteTime
from nidaqmx._waveform_utils import get_num_samps_per_chan
from nitypes.waveform.typing import ExtendedPropertyValue
from nitypes.waveform import AnalogWaveform, DigitalWaveform, SampleIntervalMode, Timing, ExtendedPropertyDictionary

if TYPE_CHECKING:
    from typing_extensions import TypeAlias

_logger = logging.getLogger(__name__)
_was_runtime_environment_set = None

_INT64_WFM_SEC_PER_TICK = 100e-9
_T0_EPOCH = ht_datetime(1, 1, 1, tzinfo=timezone.utc)

# typedef int32 (CVICALLBACK *DAQmxSetWfmAttrCallbackPtr)(uInt32 channelIndex, const char attributeName[], int32 attributeType, const void* value, uInt32 valueSizeInBytes, void *callbackData);  # noqa: W505 - doc line too long
CSetWfmAttrCallbackPtr = ctypes.CFUNCTYPE(
    ctypes.c_int32,  # return value (error code)
    ctypes.c_uint32,  # channel_index
    ctypes.c_char_p,  # attribute_name
    ctypes.c_int32,  # attribute_type
    ctypes.c_void_p,  # value
    ctypes.c_uint32,  # value_size_in_bytes
    ctypes.c_void_p,  # callback_data
)

class WfmAttrType(Enum):
    BOOL32 = 1
    FLOAT64 = 2
    INT32 = 3
    STRING = 4

SetWfmAttrCallback: TypeAlias = Callable[[int, str, WfmAttrType, ExtendedPropertyValue, object], int]

class LibraryEventHandler(BaseEventHandler):
    """Manage the lifetime of a ctypes callback method pointer.

    If DAQmx invokes a callback method pointer that has been garbage collected, the Python
    interpreter will crash.
    """
    __slots__ = ["_callback_method_ptr"]

    def __init__(self, callback_method_ptr: object) -> None:
        self._callback_method_ptr = callback_method_ptr

    def close(self) -> None:
        self._callback_method_ptr = None


class LibraryInterpreter(BaseInterpreter):
    """
    Library C<->Python interpreter.
    This class is responsible for interpreting the Library's C API.

    """
    # Do not add per-task state to the interpreter class.
    __slots__ = ('_driver_version',)

    def __init__(self):
        global _was_runtime_environment_set
        if _was_runtime_environment_set is None:
            try:
                runtime_env = platform.python_implementation()
                version = platform.python_version()
                self.set_runtime_environment(
                    runtime_env,
                    version,
                    '',
                    ''
                )
            except DaqFunctionNotSupportedError:
                pass
            finally:
                _was_runtime_environment_set = True

        major_version = self.get_system_info_attribute_uint32(0x1272)
        minor_version = self.get_system_info_attribute_uint32(0x1923)
        update_version = self.get_system_info_attribute_uint32(0x2f22)
        self._driver_version = DriverVersion(major_version, minor_version, update_version)

    @property
    def driver_version(self):
        return self._driver_version


    def add_cdaq_sync_connection(self, port_list):
        c_func = lib_importer.windll.DAQmxAddCDAQSyncConnection
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes_byte_str]

        error_code = c_func(
            port_list)
        self.check_for_error(error_code)

    def add_global_chans_to_task(self, task, channel_names):
        c_func = lib_importer.windll.DAQmxAddGlobalChansToTask
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = c_func(
            task, channel_names)
        self.check_for_error(error_code)

    def add_network_device(
            self, ip_address, device_name, attempt_reservation, timeout):
        c_func = lib_importer.windll.DAQmxAddNetworkDevice
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes_byte_str, ctypes_byte_str, c_bool32,
                        ctypes.c_double, ctypes.c_char_p, ctypes.c_uint]

        temp_size = 0
        while True:
            device_name_out = ctypes.create_string_buffer(temp_size)
            size_or_code = c_func(
                ip_address, device_name, attempt_reservation, timeout,
                device_name_out, temp_size)
            if is_string_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break
        self.check_for_error(size_or_code)
        return device_name_out.value.decode(lib_importer.encoding)

    def are_configured_cdaq_sync_ports_disconnected(
            self, chassis_devices_ports, timeout):
        disconnected_ports_exist = c_bool32()

        c_func = lib_importer.windll.DAQmxAreConfiguredCDAQSyncPortsDisconnected
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes_byte_str, ctypes.c_double,
                        ctypes.POINTER(c_bool32)]

        error_code = c_func(
            chassis_devices_ports, timeout,
            ctypes.byref(disconnected_ports_exist))
        self.check_for_error(error_code)
        return disconnected_ports_exist.value

    def auto_configure_cdaq_sync_connections(
            self, chassis_devices_ports, timeout):
        c_func = lib_importer.windll.DAQmxAutoConfigureCDAQSyncConnections
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes_byte_str, ctypes.c_double]

        error_code = c_func(
            chassis_devices_ports, timeout)
        self.check_for_error(error_code)

    def calculate_reverse_poly_coeff(
            self, forward_coeffs, min_val_x, max_val_x, num_points_to_compute,
            reverse_poly_order):
        size = len(forward_coeffs) if reverse_poly_order < 0 else reverse_poly_order + 1
        reverse_coeffs = numpy.zeros(size, dtype=numpy.float64)

        c_func = lib_importer.windll.DAQmxCalculateReversePolyCoeff
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        wrapped_ndpointer(dtype=numpy.float64, flags=('C')),
                        ctypes.c_uint, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes.c_int,
                        wrapped_ndpointer(dtype=numpy.float64,
                        flags=('C','W'))]

        error_code = c_func(
            forward_coeffs, len(forward_coeffs), min_val_x, max_val_x,
            num_points_to_compute, reverse_poly_order, reverse_coeffs)
        self.check_for_error(error_code)
        return reverse_coeffs.tolist()

    def cfg_anlg_edge_ref_trig(
            self, task, trigger_source, pretrigger_samples, trigger_slope,
            trigger_level):
        c_func = lib_importer.windll.DAQmxCfgAnlgEdgeRefTrig
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int, ctypes.c_double, ctypes.c_uint]

        error_code = c_func(
            task, trigger_source, trigger_slope, trigger_level,
            pretrigger_samples)
        self.check_for_error(error_code)

    def cfg_anlg_edge_start_trig(
            self, task, trigger_source, trigger_slope, trigger_level):
        c_func = lib_importer.windll.DAQmxCfgAnlgEdgeStartTrig
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int, ctypes.c_double]

        error_code = c_func(
            task, trigger_source, trigger_slope, trigger_level)
        self.check_for_error(error_code)

    def cfg_anlg_multi_edge_ref_trig(
            self, task, trigger_sources, pretrigger_samples,
            trigger_slope_array, trigger_level_array):
        c_func = lib_importer.windll.DAQmxCfgAnlgMultiEdgeRefTrig
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        wrapped_ndpointer(dtype=numpy.int32, flags=('C')),
                        wrapped_ndpointer(dtype=numpy.float64, flags=('C')),
                        ctypes.c_uint32, ctypes.c_uint]

        error_code = c_func(
            task, trigger_sources, trigger_slope_array, trigger_level_array,
            pretrigger_samples, len(trigger_level_array))
        self.check_for_error(error_code)

    def cfg_anlg_multi_edge_start_trig(
            self, task, trigger_sources, trigger_slope_array,
            trigger_level_array):
        c_func = lib_importer.windll.DAQmxCfgAnlgMultiEdgeStartTrig
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        wrapped_ndpointer(dtype=numpy.int32, flags=('C')),
                        wrapped_ndpointer(dtype=numpy.float64, flags=('C')),
                        ctypes.c_uint]

        error_code = c_func(
            task, trigger_sources, trigger_slope_array, trigger_level_array,
            len(trigger_level_array))
        self.check_for_error(error_code)

    def cfg_anlg_window_ref_trig(
            self, task, trigger_source, window_top, window_bottom,
            pretrigger_samples, trigger_when):
        c_func = lib_importer.windll.DAQmxCfgAnlgWindowRefTrig
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int, ctypes.c_double, ctypes.c_double,
                        ctypes.c_uint]

        error_code = c_func(
            task, trigger_source, trigger_when, window_top, window_bottom,
            pretrigger_samples)
        self.check_for_error(error_code)

    def cfg_anlg_window_start_trig(
            self, task, window_top, window_bottom, trigger_source,
            trigger_when):
        c_func = lib_importer.windll.DAQmxCfgAnlgWindowStartTrig
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int, ctypes.c_double, ctypes.c_double]

        error_code = c_func(
            task, trigger_source, trigger_when, window_top, window_bottom)
        self.check_for_error(error_code)

    def cfg_burst_handshaking_timing_export_clock(
            self, task, sample_clk_rate, sample_clk_outp_term, sample_mode,
            samps_per_chan, sample_clk_pulse_polarity, pause_when,
            ready_event_active_level):
        c_func = lib_importer.windll.DAQmxCfgBurstHandshakingTimingExportClock
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int,
                        ctypes.c_ulonglong, ctypes.c_double, ctypes_byte_str,
                        ctypes.c_int, ctypes.c_int, ctypes.c_int]

        error_code = c_func(
            task, sample_mode, samps_per_chan, sample_clk_rate,
            sample_clk_outp_term, sample_clk_pulse_polarity, pause_when,
            ready_event_active_level)
        self.check_for_error(error_code)

    def cfg_burst_handshaking_timing_import_clock(
            self, task, sample_clk_rate, sample_clk_src, sample_mode,
            samps_per_chan, sample_clk_active_edge, pause_when,
            ready_event_active_level):
        c_func = lib_importer.windll.DAQmxCfgBurstHandshakingTimingImportClock
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int,
                        ctypes.c_ulonglong, ctypes.c_double, ctypes_byte_str,
                        ctypes.c_int, ctypes.c_int, ctypes.c_int]

        error_code = c_func(
            task, sample_mode, samps_per_chan, sample_clk_rate,
            sample_clk_src, sample_clk_active_edge, pause_when,
            ready_event_active_level)
        self.check_for_error(error_code)

    def cfg_change_detection_timing(
            self, task, rising_edge_chan, falling_edge_chan, sample_mode,
            samps_per_chan):
        c_func = lib_importer.windll.DAQmxCfgChangeDetectionTiming
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_int, ctypes.c_ulonglong]

        error_code = c_func(
            task, rising_edge_chan, falling_edge_chan, sample_mode,
            samps_per_chan)
        self.check_for_error(error_code)

    def cfg_dig_edge_ref_trig(
            self, task, trigger_source, pretrigger_samples, trigger_edge):
        c_func = lib_importer.windll.DAQmxCfgDigEdgeRefTrig
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int, ctypes.c_uint]

        error_code = c_func(
            task, trigger_source, trigger_edge, pretrigger_samples)
        self.check_for_error(error_code)

    def cfg_dig_edge_start_trig(self, task, trigger_source, trigger_edge):
        c_func = lib_importer.windll.DAQmxCfgDigEdgeStartTrig
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = c_func(
            task, trigger_source, trigger_edge)
        self.check_for_error(error_code)

    def cfg_dig_pattern_ref_trig(
            self, task, trigger_source, trigger_pattern, pretrigger_samples,
            trigger_when):
        c_func = lib_importer.windll.DAQmxCfgDigPatternRefTrig
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_int, ctypes.c_uint]

        error_code = c_func(
            task, trigger_source, trigger_pattern, trigger_when,
            pretrigger_samples)
        self.check_for_error(error_code)

    def cfg_dig_pattern_start_trig(
            self, task, trigger_source, trigger_pattern, trigger_when):
        c_func = lib_importer.windll.DAQmxCfgDigPatternStartTrig
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_int]

        error_code = c_func(
            task, trigger_source, trigger_pattern, trigger_when)
        self.check_for_error(error_code)

    def cfg_handshaking_timing(self, task, sample_mode, samps_per_chan):
        c_func = lib_importer.windll.DAQmxCfgHandshakingTiming
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int,
                        ctypes.c_ulonglong]

        error_code = c_func(
            task, sample_mode, samps_per_chan)
        self.check_for_error(error_code)

    def cfg_implicit_timing(self, task, sample_mode, samps_per_chan):
        c_func = lib_importer.windll.DAQmxCfgImplicitTiming
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int,
                        ctypes.c_ulonglong]

        error_code = c_func(
            task, sample_mode, samps_per_chan)
        self.check_for_error(error_code)

    def cfg_pipelined_samp_clk_timing(
            self, task, rate, source, active_edge, sample_mode,
            samps_per_chan):
        c_func = lib_importer.windll.DAQmxCfgPipelinedSampClkTiming
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double, ctypes.c_int, ctypes.c_int,
                        ctypes.c_ulonglong]

        error_code = c_func(
            task, source, rate, active_edge, sample_mode, samps_per_chan)
        self.check_for_error(error_code)

    def cfg_samp_clk_timing(
            self, task, rate, source, active_edge, sample_mode,
            samps_per_chan):
        c_func = lib_importer.windll.DAQmxCfgSampClkTiming
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double, ctypes.c_int, ctypes.c_int,
                        ctypes.c_ulonglong]

        error_code = c_func(
            task, source, rate, active_edge, sample_mode, samps_per_chan)
        self.check_for_error(error_code)

    def cfg_time_start_trig(self, task, when, timescale):
        c_func = lib_importer.windll.DAQmxCfgTimeStartTrig
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, AbsoluteTime, ctypes.c_int]

        error_code = c_func(
            task, AbsoluteTime.from_datetime(when), timescale)
        self.check_for_error(error_code)

    def cfg_watchdog_ao_expir_states(
            self, task, channel_names, expir_state_array, output_type_array):
        c_func = lib_importer.windll.DAQmxCfgWatchdogAOExpirStates
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        wrapped_ndpointer(dtype=numpy.float64, flags=('C')),
                        wrapped_ndpointer(dtype=numpy.int32, flags=('C')),
                        ctypes.c_uint]

        error_code = c_func(
            task, channel_names, expir_state_array, output_type_array,
            len(output_type_array))
        self.check_for_error(error_code)

    def cfg_watchdog_co_expir_states(
            self, task, channel_names, expir_state_array):
        c_func = lib_importer.windll.DAQmxCfgWatchdogCOExpirStates
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        wrapped_ndpointer(dtype=numpy.int32, flags=('C')),
                        ctypes.c_uint]

        error_code = c_func(
            task, channel_names, expir_state_array, len(expir_state_array))
        self.check_for_error(error_code)

    def cfg_watchdog_do_expir_states(
            self, task, channel_names, expir_state_array):
        c_func = lib_importer.windll.DAQmxCfgWatchdogDOExpirStates
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        wrapped_ndpointer(dtype=numpy.int32, flags=('C')),
                        ctypes.c_uint]

        error_code = c_func(
            task, channel_names, expir_state_array, len(expir_state_array))
        self.check_for_error(error_code)

    def clear_task(self, task):
        c_func = lib_importer.windll.DAQmxClearTask
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle]

        error_code = c_func(
            task)
        self.check_for_error(error_code)

    def clear_teds(self, physical_channel):
        c_func = lib_importer.windll.DAQmxClearTEDS
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes_byte_str]

        error_code = c_func(
            physical_channel)
        self.check_for_error(error_code)

    def configure_logging(
            self, task, file_path, logging_mode, group_name, operation):
        c_func = lib_importer.windll.DAQmxConfigureLogging
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int, ctypes_byte_str, ctypes.c_int]

        error_code = c_func(
            task, file_path, logging_mode, group_name, operation)
        self.check_for_error(error_code)

    def configure_teds(self, physical_channel, file_path):
        c_func = lib_importer.windll.DAQmxConfigureTEDS
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes_byte_str, ctypes_byte_str]

        error_code = c_func(
            physical_channel, file_path)
        self.check_for_error(error_code)

    def connect_terms(
            self, source_terminal, destination_terminal, signal_modifiers):
        c_func = lib_importer.windll.DAQmxConnectTerms
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes_byte_str, ctypes_byte_str, ctypes.c_int]

        error_code = c_func(
            source_terminal, destination_terminal, signal_modifiers)
        self.check_for_error(error_code)

    def control_watchdog_task(self, task, action):
        c_func = lib_importer.windll.DAQmxControlWatchdogTask
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int]

        error_code = c_func(
            task, action)
        self.check_for_error(error_code)

    def create_ai_accel4_wire_dc_voltage_chan(
            self, task, physical_channel, name_to_assign_to_channel,
            terminal_config, min_val, max_val, units, sensitivity,
            sensitivity_units, voltage_excit_source, voltage_excit_val,
            use_excit_for_scaling, custom_scale_name):
        c_func = lib_importer.windll.DAQmxCreateAIAccel4WireDCVoltageChan
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_int, ctypes.c_double,
                        ctypes.c_double, ctypes.c_int, ctypes.c_double,
                        ctypes.c_int, ctypes.c_int, ctypes.c_double, c_bool32,
                        ctypes_byte_str]

        error_code = c_func(
            task, physical_channel, name_to_assign_to_channel,
            terminal_config, min_val, max_val, units, sensitivity,
            sensitivity_units, voltage_excit_source, voltage_excit_val,
            use_excit_for_scaling, custom_scale_name)
        self.check_for_error(error_code)

    def create_ai_accel_chan(
            self, task, physical_channel, name_to_assign_to_channel,
            terminal_config, min_val, max_val, units, sensitivity,
            sensitivity_units, current_excit_source, current_excit_val,
            custom_scale_name):
        c_func = lib_importer.windll.DAQmxCreateAIAccelChan
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_int, ctypes.c_double,
                        ctypes.c_double, ctypes.c_int, ctypes.c_double,
                        ctypes.c_int, ctypes.c_int, ctypes.c_double,
                        ctypes_byte_str]

        error_code = c_func(
            task, physical_channel, name_to_assign_to_channel,
            terminal_config, min_val, max_val, units, sensitivity,
            sensitivity_units, current_excit_source, current_excit_val,
            custom_scale_name)
        self.check_for_error(error_code)

    def create_ai_accel_charge_chan(
            self, task, physical_channel, name_to_assign_to_channel,
            terminal_config, min_val, max_val, units, sensitivity,
            sensitivity_units, custom_scale_name):
        c_func = lib_importer.windll.DAQmxCreateAIAccelChargeChan
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_int, ctypes.c_double,
                        ctypes.c_double, ctypes.c_int, ctypes.c_double,
                        ctypes.c_int, ctypes_byte_str]

        error_code = c_func(
            task, physical_channel, name_to_assign_to_channel,
            terminal_config, min_val, max_val, units, sensitivity,
            sensitivity_units, custom_scale_name)
        self.check_for_error(error_code)

    def create_ai_bridge_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, bridge_config, voltage_excit_source,
            voltage_excit_val, nominal_bridge_resistance, custom_scale_name):
        c_func = lib_importer.windll.DAQmxCreateAIBridgeChan
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes.c_int, ctypes.c_int,
                        ctypes.c_double, ctypes.c_double, ctypes_byte_str]

        error_code = c_func(
            task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, bridge_config, voltage_excit_source,
            voltage_excit_val, nominal_bridge_resistance, custom_scale_name)
        self.check_for_error(error_code)

    def create_ai_calculated_power_chan(
            self, task, voltage_physical_channel, current_physical_channel,
            name_to_assign_to_channel, terminal_config, voltage_min_val,
            voltage_max_val, current_min_val, current_max_val, units,
            shunt_resistor_loc, ext_shunt_resistor_val, custom_scale_name):
        c_func = lib_importer.windll.DAQmxCreateAICalculatedPowerChan
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes_byte_str, ctypes.c_int,
                        ctypes.c_double, ctypes.c_double, ctypes.c_double,
                        ctypes.c_double, ctypes.c_int, ctypes.c_int,
                        ctypes.c_double, ctypes_byte_str]

        error_code = c_func(
            task, voltage_physical_channel, current_physical_channel,
            name_to_assign_to_channel, terminal_config, voltage_min_val,
            voltage_max_val, current_min_val, current_max_val, units,
            shunt_resistor_loc, ext_shunt_resistor_val, custom_scale_name)
        self.check_for_error(error_code)

    def create_ai_charge_chan(
            self, task, physical_channel, name_to_assign_to_channel,
            terminal_config, min_val, max_val, units, custom_scale_name):
        c_func = lib_importer.windll.DAQmxCreateAIChargeChan
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_int, ctypes.c_double,
                        ctypes.c_double, ctypes.c_int, ctypes_byte_str]

        error_code = c_func(
            task, physical_channel, name_to_assign_to_channel,
            terminal_config, min_val, max_val, units, custom_scale_name)
        self.check_for_error(error_code)

    def create_ai_current_chan(
            self, task, physical_channel, name_to_assign_to_channel,
            terminal_config, min_val, max_val, units, shunt_resistor_loc,
            ext_shunt_resistor_val, custom_scale_name):
        c_func = lib_importer.windll.DAQmxCreateAICurrentChan
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_int, ctypes.c_double,
                        ctypes.c_double, ctypes.c_int, ctypes.c_int,
                        ctypes.c_double, ctypes_byte_str]

        error_code = c_func(
            task, physical_channel, name_to_assign_to_channel,
            terminal_config, min_val, max_val, units, shunt_resistor_loc,
            ext_shunt_resistor_val, custom_scale_name)
        self.check_for_error(error_code)

    def create_ai_current_rms_chan(
            self, task, physical_channel, name_to_assign_to_channel,
            terminal_config, min_val, max_val, units, shunt_resistor_loc,
            ext_shunt_resistor_val, custom_scale_name):
        c_func = lib_importer.windll.DAQmxCreateAICurrentRMSChan
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_int, ctypes.c_double,
                        ctypes.c_double, ctypes.c_int, ctypes.c_int,
                        ctypes.c_double, ctypes_byte_str]

        error_code = c_func(
            task, physical_channel, name_to_assign_to_channel,
            terminal_config, min_val, max_val, units, shunt_resistor_loc,
            ext_shunt_resistor_val, custom_scale_name)
        self.check_for_error(error_code)

    def create_ai_force_bridge_polynomial_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, bridge_config, voltage_excit_source,
            voltage_excit_val, nominal_bridge_resistance, forward_coeffs,
            reverse_coeffs, electrical_units, physical_units,
            custom_scale_name):
        c_func = lib_importer.windll.DAQmxCreateAIForceBridgePolynomialChan
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes.c_int, ctypes.c_int,
                        ctypes.c_double, ctypes.c_double,
                        wrapped_ndpointer(dtype=numpy.float64, flags=('C')),
                        ctypes.c_uint, wrapped_ndpointer(dtype=numpy.float64,
                        flags=('C')), ctypes.c_uint, ctypes.c_int,
                        ctypes.c_int, ctypes_byte_str]

        error_code = c_func(
            task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, bridge_config, voltage_excit_source,
            voltage_excit_val, nominal_bridge_resistance, forward_coeffs,
            len(forward_coeffs), reverse_coeffs, len(reverse_coeffs),
            electrical_units, physical_units, custom_scale_name)
        self.check_for_error(error_code)

    def create_ai_force_bridge_table_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, bridge_config, voltage_excit_source,
            voltage_excit_val, nominal_bridge_resistance, electrical_vals,
            electrical_units, physical_vals, physical_units,
            custom_scale_name):
        c_func = lib_importer.windll.DAQmxCreateAIForceBridgeTableChan
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes.c_int, ctypes.c_int,
                        ctypes.c_double, ctypes.c_double,
                        wrapped_ndpointer(dtype=numpy.float64, flags=('C')),
                        ctypes.c_uint, ctypes.c_int,
                        wrapped_ndpointer(dtype=numpy.float64, flags=('C')),
                        ctypes.c_uint, ctypes.c_int, ctypes_byte_str]

        error_code = c_func(
            task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, bridge_config, voltage_excit_source,
            voltage_excit_val, nominal_bridge_resistance, electrical_vals,
            len(electrical_vals), electrical_units, physical_vals,
            len(physical_vals), physical_units, custom_scale_name)
        self.check_for_error(error_code)

    def create_ai_force_bridge_two_point_lin_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, bridge_config, voltage_excit_source,
            voltage_excit_val, nominal_bridge_resistance,
            first_electrical_val, second_electrical_val, electrical_units,
            first_physical_val, second_physical_val, physical_units,
            custom_scale_name):
        c_func = lib_importer.windll.DAQmxCreateAIForceBridgeTwoPointLinChan
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes.c_int, ctypes.c_int,
                        ctypes.c_double, ctypes.c_double, ctypes.c_double,
                        ctypes.c_double, ctypes.c_int, ctypes.c_double,
                        ctypes.c_double, ctypes.c_int, ctypes_byte_str]

        error_code = c_func(
            task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, bridge_config, voltage_excit_source,
            voltage_excit_val, nominal_bridge_resistance,
            first_electrical_val, second_electrical_val, electrical_units,
            first_physical_val, second_physical_val, physical_units,
            custom_scale_name)
        self.check_for_error(error_code)

    def create_ai_force_iepe_chan(
            self, task, physical_channel, name_to_assign_to_channel,
            terminal_config, min_val, max_val, units, sensitivity,
            sensitivity_units, current_excit_source, current_excit_val,
            custom_scale_name):
        c_func = lib_importer.windll.DAQmxCreateAIForceIEPEChan
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_int, ctypes.c_double,
                        ctypes.c_double, ctypes.c_int, ctypes.c_double,
                        ctypes.c_int, ctypes.c_int, ctypes.c_double,
                        ctypes_byte_str]

        error_code = c_func(
            task, physical_channel, name_to_assign_to_channel,
            terminal_config, min_val, max_val, units, sensitivity,
            sensitivity_units, current_excit_source, current_excit_val,
            custom_scale_name)
        self.check_for_error(error_code)

    def create_ai_freq_voltage_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, threshold_level, hysteresis, custom_scale_name):
        c_func = lib_importer.windll.DAQmxCreateAIFreqVoltageChan
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes.c_double, ctypes.c_double,
                        ctypes_byte_str]

        error_code = c_func(
            task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, threshold_level, hysteresis, custom_scale_name)
        self.check_for_error(error_code)

    def create_ai_microphone_chan(
            self, task, physical_channel, name_to_assign_to_channel,
            terminal_config, units, mic_sensitivity, max_snd_press_level,
            current_excit_source, current_excit_val, custom_scale_name):
        c_func = lib_importer.windll.DAQmxCreateAIMicrophoneChan
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_int, ctypes.c_int,
                        ctypes.c_double, ctypes.c_double, ctypes.c_int,
                        ctypes.c_double, ctypes_byte_str]

        error_code = c_func(
            task, physical_channel, name_to_assign_to_channel,
            terminal_config, units, mic_sensitivity, max_snd_press_level,
            current_excit_source, current_excit_val, custom_scale_name)
        self.check_for_error(error_code)

    def create_ai_pos_eddy_curr_prox_probe_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, sensitivity, sensitivity_units,
            custom_scale_name):
        c_func = lib_importer.windll.DAQmxCreateAIPosEddyCurrProxProbeChan
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes.c_double, ctypes.c_int,
                        ctypes_byte_str]

        error_code = c_func(
            task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, sensitivity, sensitivity_units, custom_scale_name)
        self.check_for_error(error_code)

    def create_ai_pos_lvdt_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, sensitivity, sensitivity_units,
            voltage_excit_source, voltage_excit_val, voltage_excit_freq,
            ac_excit_wire_mode, custom_scale_name):
        c_func = lib_importer.windll.DAQmxCreateAIPosLVDTChan
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes.c_double, ctypes.c_int,
                        ctypes.c_int, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes_byte_str]

        error_code = c_func(
            task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, sensitivity, sensitivity_units,
            voltage_excit_source, voltage_excit_val, voltage_excit_freq,
            ac_excit_wire_mode, custom_scale_name)
        self.check_for_error(error_code)

    def create_ai_pos_rvdt_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, sensitivity, sensitivity_units,
            voltage_excit_source, voltage_excit_val, voltage_excit_freq,
            ac_excit_wire_mode, custom_scale_name):
        c_func = lib_importer.windll.DAQmxCreateAIPosRVDTChan
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes.c_double, ctypes.c_int,
                        ctypes.c_int, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes_byte_str]

        error_code = c_func(
            task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, sensitivity, sensitivity_units,
            voltage_excit_source, voltage_excit_val, voltage_excit_freq,
            ac_excit_wire_mode, custom_scale_name)
        self.check_for_error(error_code)

    def create_ai_power_chan(
            self, task, physical_channel, voltage_setpoint, current_setpoint,
            output_enable, name_to_assign_to_channel):
        c_func = lib_importer.windll.DAQmxCreateAIPowerChan
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        c_bool32]

        error_code = c_func(
            task, physical_channel, name_to_assign_to_channel,
            voltage_setpoint, current_setpoint, output_enable)
        self.check_for_error(error_code)

    def create_ai_pressure_bridge_polynomial_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, bridge_config, voltage_excit_source,
            voltage_excit_val, nominal_bridge_resistance, forward_coeffs,
            reverse_coeffs, electrical_units, physical_units,
            custom_scale_name):
        c_func = lib_importer.windll.DAQmxCreateAIPressureBridgePolynomialChan
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes.c_int, ctypes.c_int,
                        ctypes.c_double, ctypes.c_double,
                        wrapped_ndpointer(dtype=numpy.float64, flags=('C')),
                        ctypes.c_uint, wrapped_ndpointer(dtype=numpy.float64,
                        flags=('C')), ctypes.c_uint, ctypes.c_int,
                        ctypes.c_int, ctypes_byte_str]

        error_code = c_func(
            task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, bridge_config, voltage_excit_source,
            voltage_excit_val, nominal_bridge_resistance, forward_coeffs,
            len(forward_coeffs), reverse_coeffs, len(reverse_coeffs),
            electrical_units, physical_units, custom_scale_name)
        self.check_for_error(error_code)

    def create_ai_pressure_bridge_table_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, bridge_config, voltage_excit_source,
            voltage_excit_val, nominal_bridge_resistance, electrical_vals,
            electrical_units, physical_vals, physical_units,
            custom_scale_name):
        c_func = lib_importer.windll.DAQmxCreateAIPressureBridgeTableChan
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes.c_int, ctypes.c_int,
                        ctypes.c_double, ctypes.c_double,
                        wrapped_ndpointer(dtype=numpy.float64, flags=('C')),
                        ctypes.c_uint, ctypes.c_int,
                        wrapped_ndpointer(dtype=numpy.float64, flags=('C')),
                        ctypes.c_uint, ctypes.c_int, ctypes_byte_str]

        error_code = c_func(
            task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, bridge_config, voltage_excit_source,
            voltage_excit_val, nominal_bridge_resistance, electrical_vals,
            len(electrical_vals), electrical_units, physical_vals,
            len(physical_vals), physical_units, custom_scale_name)
        self.check_for_error(error_code)

    def create_ai_pressure_bridge_two_point_lin_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, bridge_config, voltage_excit_source,
            voltage_excit_val, nominal_bridge_resistance,
            first_electrical_val, second_electrical_val, electrical_units,
            first_physical_val, second_physical_val, physical_units,
            custom_scale_name):
        c_func = lib_importer.windll.DAQmxCreateAIPressureBridgeTwoPointLinChan
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes.c_int, ctypes.c_int,
                        ctypes.c_double, ctypes.c_double, ctypes.c_double,
                        ctypes.c_double, ctypes.c_int, ctypes.c_double,
                        ctypes.c_double, ctypes.c_int, ctypes_byte_str]

        error_code = c_func(
            task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, bridge_config, voltage_excit_source,
            voltage_excit_val, nominal_bridge_resistance,
            first_electrical_val, second_electrical_val, electrical_units,
            first_physical_val, second_physical_val, physical_units,
            custom_scale_name)
        self.check_for_error(error_code)

    def create_ai_resistance_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, resistance_config, current_excit_source,
            current_excit_val, custom_scale_name):
        c_func = lib_importer.windll.DAQmxCreateAIResistanceChan
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes.c_int, ctypes.c_int,
                        ctypes.c_double, ctypes_byte_str]

        error_code = c_func(
            task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, resistance_config, current_excit_source,
            current_excit_val, custom_scale_name)
        self.check_for_error(error_code)

    def create_ai_rosette_strain_gage_chan(
            self, task, physical_channel, rosette_type, gage_orientation,
            rosette_meas_types, name_to_assign_to_channel, min_val, max_val,
            strain_config, voltage_excit_source, voltage_excit_val,
            gage_factor, nominal_gage_resistance, poisson_ratio,
            lead_wire_resistance):
        c_func = lib_importer.windll.DAQmxCreateAIRosetteStrainGageChan
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes.c_double,
                        wrapped_ndpointer(dtype=numpy.int32, flags=('C')),
                        ctypes.c_uint, ctypes.c_int, ctypes.c_int,
                        ctypes.c_double, ctypes.c_double, ctypes.c_double,
                        ctypes.c_double, ctypes.c_double]

        error_code = c_func(
            task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, rosette_type, gage_orientation, rosette_meas_types,
            len(rosette_meas_types), strain_config, voltage_excit_source,
            voltage_excit_val, gage_factor, nominal_gage_resistance,
            poisson_ratio, lead_wire_resistance)
        self.check_for_error(error_code)

    def create_ai_strain_gage_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, strain_config, voltage_excit_source,
            voltage_excit_val, gage_factor, initial_bridge_voltage,
            nominal_gage_resistance, poisson_ratio, lead_wire_resistance,
            custom_scale_name):
        c_func = lib_importer.windll.DAQmxCreateAIStrainGageChan
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes.c_int, ctypes.c_int,
                        ctypes.c_double, ctypes.c_double, ctypes.c_double,
                        ctypes.c_double, ctypes.c_double, ctypes.c_double,
                        ctypes_byte_str]

        error_code = c_func(
            task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, strain_config, voltage_excit_source,
            voltage_excit_val, gage_factor, initial_bridge_voltage,
            nominal_gage_resistance, poisson_ratio, lead_wire_resistance,
            custom_scale_name)
        self.check_for_error(error_code)

    def create_ai_temp_built_in_sensor_chan(
            self, task, physical_channel, name_to_assign_to_channel, units):
        c_func = lib_importer.windll.DAQmxCreateAITempBuiltInSensorChan
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_int]

        error_code = c_func(
            task, physical_channel, name_to_assign_to_channel, units)
        self.check_for_error(error_code)

    def create_ai_thrmcpl_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, thermocouple_type, cjc_source, cjc_val,
            cjc_channel):
        c_func = lib_importer.windll.DAQmxCreateAIThrmcplChan
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes.c_int, ctypes.c_int,
                        ctypes.c_double, ctypes_byte_str]

        error_code = c_func(
            task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, thermocouple_type, cjc_source, cjc_val,
            cjc_channel)
        self.check_for_error(error_code)

    def create_ai_thrmstr_chan_iex(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, resistance_config, current_excit_source,
            current_excit_val, a, b, c):
        c_func = lib_importer.windll.DAQmxCreateAIThrmstrChanIex
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes.c_int, ctypes.c_int,
                        ctypes.c_double, ctypes.c_double, ctypes.c_double,
                        ctypes.c_double]

        error_code = c_func(
            task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, resistance_config, current_excit_source,
            current_excit_val, a, b, c)
        self.check_for_error(error_code)

    def create_ai_thrmstr_chan_vex(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, resistance_config, voltage_excit_source,
            voltage_excit_val, a, b, c, r_1):
        c_func = lib_importer.windll.DAQmxCreateAIThrmstrChanVex
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes.c_int, ctypes.c_int,
                        ctypes.c_double, ctypes.c_double, ctypes.c_double,
                        ctypes.c_double, ctypes.c_double]

        error_code = c_func(
            task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, resistance_config, voltage_excit_source,
            voltage_excit_val, a, b, c, r_1)
        self.check_for_error(error_code)

    def create_ai_torque_bridge_polynomial_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, bridge_config, voltage_excit_source,
            voltage_excit_val, nominal_bridge_resistance, forward_coeffs,
            reverse_coeffs, electrical_units, physical_units,
            custom_scale_name):
        c_func = lib_importer.windll.DAQmxCreateAITorqueBridgePolynomialChan
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes.c_int, ctypes.c_int,
                        ctypes.c_double, ctypes.c_double,
                        wrapped_ndpointer(dtype=numpy.float64, flags=('C')),
                        ctypes.c_uint, wrapped_ndpointer(dtype=numpy.float64,
                        flags=('C')), ctypes.c_uint, ctypes.c_int,
                        ctypes.c_int, ctypes_byte_str]

        error_code = c_func(
            task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, bridge_config, voltage_excit_source,
            voltage_excit_val, nominal_bridge_resistance, forward_coeffs,
            len(forward_coeffs), reverse_coeffs, len(reverse_coeffs),
            electrical_units, physical_units, custom_scale_name)
        self.check_for_error(error_code)

    def create_ai_torque_bridge_table_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, bridge_config, voltage_excit_source,
            voltage_excit_val, nominal_bridge_resistance, electrical_vals,
            electrical_units, physical_vals, physical_units,
            custom_scale_name):
        c_func = lib_importer.windll.DAQmxCreateAITorqueBridgeTableChan
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes.c_int, ctypes.c_int,
                        ctypes.c_double, ctypes.c_double,
                        wrapped_ndpointer(dtype=numpy.float64, flags=('C')),
                        ctypes.c_uint, ctypes.c_int,
                        wrapped_ndpointer(dtype=numpy.float64, flags=('C')),
                        ctypes.c_uint, ctypes.c_int, ctypes_byte_str]

        error_code = c_func(
            task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, bridge_config, voltage_excit_source,
            voltage_excit_val, nominal_bridge_resistance, electrical_vals,
            len(electrical_vals), electrical_units, physical_vals,
            len(physical_vals), physical_units, custom_scale_name)
        self.check_for_error(error_code)

    def create_ai_torque_bridge_two_point_lin_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, bridge_config, voltage_excit_source,
            voltage_excit_val, nominal_bridge_resistance,
            first_electrical_val, second_electrical_val, electrical_units,
            first_physical_val, second_physical_val, physical_units,
            custom_scale_name):
        c_func = lib_importer.windll.DAQmxCreateAITorqueBridgeTwoPointLinChan
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes.c_int, ctypes.c_int,
                        ctypes.c_double, ctypes.c_double, ctypes.c_double,
                        ctypes.c_double, ctypes.c_int, ctypes.c_double,
                        ctypes.c_double, ctypes.c_int, ctypes_byte_str]

        error_code = c_func(
            task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, bridge_config, voltage_excit_source,
            voltage_excit_val, nominal_bridge_resistance,
            first_electrical_val, second_electrical_val, electrical_units,
            first_physical_val, second_physical_val, physical_units,
            custom_scale_name)
        self.check_for_error(error_code)

    def create_ai_velocity_iepe_chan(
            self, task, physical_channel, name_to_assign_to_channel,
            terminal_config, min_val, max_val, units, sensitivity,
            sensitivity_units, current_excit_source, current_excit_val,
            custom_scale_name):
        c_func = lib_importer.windll.DAQmxCreateAIVelocityIEPEChan
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_int, ctypes.c_double,
                        ctypes.c_double, ctypes.c_int, ctypes.c_double,
                        ctypes.c_int, ctypes.c_int, ctypes.c_double,
                        ctypes_byte_str]

        error_code = c_func(
            task, physical_channel, name_to_assign_to_channel,
            terminal_config, min_val, max_val, units, sensitivity,
            sensitivity_units, current_excit_source, current_excit_val,
            custom_scale_name)
        self.check_for_error(error_code)

    def create_ai_voltage_chan(
            self, task, physical_channel, name_to_assign_to_channel,
            terminal_config, min_val, max_val, units, custom_scale_name):
        c_func = lib_importer.windll.DAQmxCreateAIVoltageChan
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_int, ctypes.c_double,
                        ctypes.c_double, ctypes.c_int, ctypes_byte_str]

        error_code = c_func(
            task, physical_channel, name_to_assign_to_channel,
            terminal_config, min_val, max_val, units, custom_scale_name)
        self.check_for_error(error_code)

    def create_ai_voltage_chan_with_excit(
            self, task, physical_channel, name_to_assign_to_channel,
            terminal_config, min_val, max_val, units, bridge_config,
            voltage_excit_source, voltage_excit_val, use_excit_for_scaling,
            custom_scale_name):
        c_func = lib_importer.windll.DAQmxCreateAIVoltageChanWithExcit
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_int, ctypes.c_double,
                        ctypes.c_double, ctypes.c_int, ctypes.c_int,
                        ctypes.c_int, ctypes.c_double, c_bool32,
                        ctypes_byte_str]

        error_code = c_func(
            task, physical_channel, name_to_assign_to_channel,
            terminal_config, min_val, max_val, units, bridge_config,
            voltage_excit_source, voltage_excit_val, use_excit_for_scaling,
            custom_scale_name)
        self.check_for_error(error_code)

    def create_ai_voltage_rms_chan(
            self, task, physical_channel, name_to_assign_to_channel,
            terminal_config, min_val, max_val, units, custom_scale_name):
        c_func = lib_importer.windll.DAQmxCreateAIVoltageRMSChan
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_int, ctypes.c_double,
                        ctypes.c_double, ctypes.c_int, ctypes_byte_str]

        error_code = c_func(
            task, physical_channel, name_to_assign_to_channel,
            terminal_config, min_val, max_val, units, custom_scale_name)
        self.check_for_error(error_code)

    def create_airtd_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, rtd_type, resistance_config, current_excit_source,
            current_excit_val, r_0):
        c_func = lib_importer.windll.DAQmxCreateAIRTDChan
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes.c_int, ctypes.c_int,
                        ctypes.c_int, ctypes.c_double, ctypes.c_double]

        error_code = c_func(
            task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, rtd_type, resistance_config, current_excit_source,
            current_excit_val, r_0)
        self.check_for_error(error_code)

    def create_ao_current_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, custom_scale_name):
        c_func = lib_importer.windll.DAQmxCreateAOCurrentChan
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes_byte_str]

        error_code = c_func(
            task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, custom_scale_name)
        self.check_for_error(error_code)

    def create_ao_func_gen_chan(
            self, task, physical_channel, name_to_assign_to_channel, type,
            freq, amplitude, offset):
        c_func = lib_importer.windll.DAQmxCreateAOFuncGenChan
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_int, ctypes.c_double,
                        ctypes.c_double, ctypes.c_double]

        error_code = c_func(
            task, physical_channel, name_to_assign_to_channel, type, freq,
            amplitude, offset)
        self.check_for_error(error_code)

    def create_ao_voltage_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, custom_scale_name):
        c_func = lib_importer.windll.DAQmxCreateAOVoltageChan
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes_byte_str]

        error_code = c_func(
            task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, custom_scale_name)
        self.check_for_error(error_code)

    def create_ci_ang_encoder_chan(
            self, task, counter, name_to_assign_to_channel, decoding_type,
            zidx_enable, zidx_val, zidx_phase, units, pulses_per_rev,
            initial_angle, custom_scale_name):
        c_func = lib_importer.windll.DAQmxCreateCIAngEncoderChan
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_int, c_bool32,
                        ctypes.c_double, ctypes.c_int, ctypes.c_int,
                        ctypes.c_uint, ctypes.c_double, ctypes_byte_str]

        error_code = c_func(
            task, counter, name_to_assign_to_channel, decoding_type,
            zidx_enable, zidx_val, zidx_phase, units, pulses_per_rev,
            initial_angle, custom_scale_name)
        self.check_for_error(error_code)

    def create_ci_ang_velocity_chan(
            self, task, counter, name_to_assign_to_channel, min_val, max_val,
            decoding_type, units, pulses_per_rev, custom_scale_name):
        c_func = lib_importer.windll.DAQmxCreateCIAngVelocityChan
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes.c_int, ctypes.c_uint,
                        ctypes_byte_str]

        error_code = c_func(
            task, counter, name_to_assign_to_channel, min_val, max_val,
            decoding_type, units, pulses_per_rev, custom_scale_name)
        self.check_for_error(error_code)

    def create_ci_count_edges_chan(
            self, task, counter, name_to_assign_to_channel, edge,
            initial_count, count_direction):
        c_func = lib_importer.windll.DAQmxCreateCICountEdgesChan
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_int, ctypes.c_uint,
                        ctypes.c_int]

        error_code = c_func(
            task, counter, name_to_assign_to_channel, edge, initial_count,
            count_direction)
        self.check_for_error(error_code)

    def create_ci_duty_cycle_chan(
            self, task, counter, name_to_assign_to_channel, min_freq,
            max_freq, edge, custom_scale_name):
        c_func = lib_importer.windll.DAQmxCreateCIDutyCycleChan
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes_byte_str]

        error_code = c_func(
            task, counter, name_to_assign_to_channel, min_freq, max_freq,
            edge, custom_scale_name)
        self.check_for_error(error_code)

    def create_ci_freq_chan(
            self, task, counter, name_to_assign_to_channel, min_val, max_val,
            units, edge, meas_method, meas_time, divisor, custom_scale_name):
        c_func = lib_importer.windll.DAQmxCreateCIFreqChan
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes.c_int, ctypes.c_int,
                        ctypes.c_double, ctypes.c_uint, ctypes_byte_str]

        error_code = c_func(
            task, counter, name_to_assign_to_channel, min_val, max_val, units,
            edge, meas_method, meas_time, divisor, custom_scale_name)
        self.check_for_error(error_code)

    def create_ci_lin_encoder_chan(
            self, task, counter, name_to_assign_to_channel, decoding_type,
            zidx_enable, zidx_val, zidx_phase, units, dist_per_pulse,
            initial_pos, custom_scale_name):
        c_func = lib_importer.windll.DAQmxCreateCILinEncoderChan
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_int, c_bool32,
                        ctypes.c_double, ctypes.c_int, ctypes.c_int,
                        ctypes.c_double, ctypes.c_double, ctypes_byte_str]

        error_code = c_func(
            task, counter, name_to_assign_to_channel, decoding_type,
            zidx_enable, zidx_val, zidx_phase, units, dist_per_pulse,
            initial_pos, custom_scale_name)
        self.check_for_error(error_code)

    def create_ci_lin_velocity_chan(
            self, task, counter, name_to_assign_to_channel, min_val, max_val,
            decoding_type, units, dist_per_pulse, custom_scale_name):
        c_func = lib_importer.windll.DAQmxCreateCILinVelocityChan
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes.c_int, ctypes.c_double,
                        ctypes_byte_str]

        error_code = c_func(
            task, counter, name_to_assign_to_channel, min_val, max_val,
            decoding_type, units, dist_per_pulse, custom_scale_name)
        self.check_for_error(error_code)

    def create_ci_period_chan(
            self, task, counter, name_to_assign_to_channel, min_val, max_val,
            units, edge, meas_method, meas_time, divisor, custom_scale_name):
        c_func = lib_importer.windll.DAQmxCreateCIPeriodChan
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes.c_int, ctypes.c_int,
                        ctypes.c_double, ctypes.c_uint, ctypes_byte_str]

        error_code = c_func(
            task, counter, name_to_assign_to_channel, min_val, max_val, units,
            edge, meas_method, meas_time, divisor, custom_scale_name)
        self.check_for_error(error_code)

    def create_ci_pulse_chan_freq(
            self, task, counter, name_to_assign_to_channel, min_val, max_val,
            units):
        c_func = lib_importer.windll.DAQmxCreateCIPulseChanFreq
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int]

        error_code = c_func(
            task, counter, name_to_assign_to_channel, min_val, max_val, units)
        self.check_for_error(error_code)

    def create_ci_pulse_chan_ticks(
            self, task, counter, name_to_assign_to_channel, source_terminal,
            min_val, max_val):
        c_func = lib_importer.windll.DAQmxCreateCIPulseChanTicks
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes_byte_str, ctypes.c_double,
                        ctypes.c_double]

        error_code = c_func(
            task, counter, name_to_assign_to_channel, source_terminal,
            min_val, max_val)
        self.check_for_error(error_code)

    def create_ci_pulse_chan_time(
            self, task, counter, name_to_assign_to_channel, min_val, max_val,
            units):
        c_func = lib_importer.windll.DAQmxCreateCIPulseChanTime
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int]

        error_code = c_func(
            task, counter, name_to_assign_to_channel, min_val, max_val, units)
        self.check_for_error(error_code)

    def create_ci_pulse_width_chan(
            self, task, counter, name_to_assign_to_channel, min_val, max_val,
            units, starting_edge, custom_scale_name):
        c_func = lib_importer.windll.DAQmxCreateCIPulseWidthChan
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes.c_int, ctypes_byte_str]

        error_code = c_func(
            task, counter, name_to_assign_to_channel, min_val, max_val, units,
            starting_edge, custom_scale_name)
        self.check_for_error(error_code)

    def create_ci_semi_period_chan(
            self, task, counter, name_to_assign_to_channel, min_val, max_val,
            units, custom_scale_name):
        c_func = lib_importer.windll.DAQmxCreateCISemiPeriodChan
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes_byte_str]

        error_code = c_func(
            task, counter, name_to_assign_to_channel, min_val, max_val, units,
            custom_scale_name)
        self.check_for_error(error_code)

    def create_ci_two_edge_sep_chan(
            self, task, counter, name_to_assign_to_channel, min_val, max_val,
            units, first_edge, second_edge, custom_scale_name):
        c_func = lib_importer.windll.DAQmxCreateCITwoEdgeSepChan
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes.c_int, ctypes.c_int,
                        ctypes_byte_str]

        error_code = c_func(
            task, counter, name_to_assign_to_channel, min_val, max_val, units,
            first_edge, second_edge, custom_scale_name)
        self.check_for_error(error_code)

    def create_cigps_timestamp_chan(
            self, task, counter, name_to_assign_to_channel, units,
            sync_method, custom_scale_name):
        c_func = lib_importer.windll.DAQmxCreateCIGPSTimestampChan
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_int, ctypes.c_int,
                        ctypes_byte_str]

        error_code = c_func(
            task, counter, name_to_assign_to_channel, units, sync_method,
            custom_scale_name)
        self.check_for_error(error_code)

    def create_co_pulse_chan_freq(
            self, task, counter, name_to_assign_to_channel, units, idle_state,
            initial_delay, freq, duty_cycle):
        c_func = lib_importer.windll.DAQmxCreateCOPulseChanFreq
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_int, ctypes.c_int,
                        ctypes.c_double, ctypes.c_double, ctypes.c_double]

        error_code = c_func(
            task, counter, name_to_assign_to_channel, units, idle_state,
            initial_delay, freq, duty_cycle)
        self.check_for_error(error_code)

    def create_co_pulse_chan_ticks(
            self, task, counter, source_terminal, name_to_assign_to_channel,
            idle_state, initial_delay, low_ticks, high_ticks):
        c_func = lib_importer.windll.DAQmxCreateCOPulseChanTicks
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes_byte_str, ctypes.c_int,
                        ctypes.c_int, ctypes.c_int, ctypes.c_int]

        error_code = c_func(
            task, counter, name_to_assign_to_channel, source_terminal,
            idle_state, initial_delay, low_ticks, high_ticks)
        self.check_for_error(error_code)

    def create_co_pulse_chan_time(
            self, task, counter, name_to_assign_to_channel, units, idle_state,
            initial_delay, low_time, high_time):
        c_func = lib_importer.windll.DAQmxCreateCOPulseChanTime
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_int, ctypes.c_int,
                        ctypes.c_double, ctypes.c_double, ctypes.c_double]

        error_code = c_func(
            task, counter, name_to_assign_to_channel, units, idle_state,
            initial_delay, low_time, high_time)
        self.check_for_error(error_code)

    def create_di_chan(
            self, task, lines, name_to_assign_to_lines, line_grouping):
        c_func = lib_importer.windll.DAQmxCreateDIChan
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_int]

        error_code = c_func(
            task, lines, name_to_assign_to_lines, line_grouping)
        self.check_for_error(error_code)

    def create_do_chan(
            self, task, lines, name_to_assign_to_lines, line_grouping):
        c_func = lib_importer.windll.DAQmxCreateDOChan
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_int]

        error_code = c_func(
            task, lines, name_to_assign_to_lines, line_grouping)
        self.check_for_error(error_code)

    def create_lin_scale(
            self, name, slope, y_intercept, pre_scaled_units, scaled_units):
        c_func = lib_importer.windll.DAQmxCreateLinScale
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes_byte_str]

        error_code = c_func(
            name, slope, y_intercept, pre_scaled_units, scaled_units)
        self.check_for_error(error_code)

    def create_map_scale(
            self, name, prescaled_min, prescaled_max, scaled_min, scaled_max,
            pre_scaled_units, scaled_units):
        c_func = lib_importer.windll.DAQmxCreateMapScale
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_double, ctypes.c_double, ctypes.c_int,
                        ctypes_byte_str]

        error_code = c_func(
            name, prescaled_min, prescaled_max, scaled_min, scaled_max,
            pre_scaled_units, scaled_units)
        self.check_for_error(error_code)

    def create_polynomial_scale(
            self, name, forward_coeffs, reverse_coeffs, pre_scaled_units,
            scaled_units):
        c_func = lib_importer.windll.DAQmxCreatePolynomialScale
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes_byte_str,
                        wrapped_ndpointer(dtype=numpy.float64, flags=('C')),
                        ctypes.c_uint, wrapped_ndpointer(dtype=numpy.float64,
                        flags=('C')), ctypes.c_uint, ctypes.c_int,
                        ctypes_byte_str]

        error_code = c_func(
            name, forward_coeffs, len(forward_coeffs), reverse_coeffs,
            len(reverse_coeffs), pre_scaled_units, scaled_units)
        self.check_for_error(error_code)

    def create_table_scale(
            self, name, prescaled_vals, scaled_vals, pre_scaled_units,
            scaled_units):
        c_func = lib_importer.windll.DAQmxCreateTableScale
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes_byte_str,
                        wrapped_ndpointer(dtype=numpy.float64, flags=('C')),
                        ctypes.c_uint, wrapped_ndpointer(dtype=numpy.float64,
                        flags=('C')), ctypes.c_uint, ctypes.c_int,
                        ctypes_byte_str]

        error_code = c_func(
            name, prescaled_vals, len(prescaled_vals), scaled_vals,
            len(scaled_vals), pre_scaled_units, scaled_units)
        self.check_for_error(error_code)

    def create_task(self, session_name):
        new_session_initialized = True
        task = lib_importer.task_handle(0)

        c_func = lib_importer.windll.DAQmxCreateTask
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes_byte_str,
                        ctypes.POINTER(lib_importer.task_handle)]

        error_code = c_func(
            session_name, ctypes.byref(task))
        self.check_for_error(error_code)
        return task, new_session_initialized

    def create_tedsai_accel_chan(
            self, task, physical_channel, name_to_assign_to_channel,
            terminal_config, min_val, max_val, units, current_excit_source,
            current_excit_val, custom_scale_name):
        c_func = lib_importer.windll.DAQmxCreateTEDSAIAccelChan
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_int, ctypes.c_double,
                        ctypes.c_double, ctypes.c_int, ctypes.c_int,
                        ctypes.c_double, ctypes_byte_str]

        error_code = c_func(
            task, physical_channel, name_to_assign_to_channel,
            terminal_config, min_val, max_val, units, current_excit_source,
            current_excit_val, custom_scale_name)
        self.check_for_error(error_code)

    def create_tedsai_bridge_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, voltage_excit_source, voltage_excit_val,
            custom_scale_name):
        c_func = lib_importer.windll.DAQmxCreateTEDSAIBridgeChan
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes.c_int, ctypes.c_double,
                        ctypes_byte_str]

        error_code = c_func(
            task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, voltage_excit_source, voltage_excit_val,
            custom_scale_name)
        self.check_for_error(error_code)

    def create_tedsai_current_chan(
            self, task, physical_channel, name_to_assign_to_channel,
            terminal_config, min_val, max_val, units, shunt_resistor_loc,
            ext_shunt_resistor_val, custom_scale_name):
        c_func = lib_importer.windll.DAQmxCreateTEDSAICurrentChan
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_int, ctypes.c_double,
                        ctypes.c_double, ctypes.c_int, ctypes.c_int,
                        ctypes.c_double, ctypes_byte_str]

        error_code = c_func(
            task, physical_channel, name_to_assign_to_channel,
            terminal_config, min_val, max_val, units, shunt_resistor_loc,
            ext_shunt_resistor_val, custom_scale_name)
        self.check_for_error(error_code)

    def create_tedsai_force_bridge_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, voltage_excit_source, voltage_excit_val,
            custom_scale_name):
        c_func = lib_importer.windll.DAQmxCreateTEDSAIForceBridgeChan
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes.c_int, ctypes.c_double,
                        ctypes_byte_str]

        error_code = c_func(
            task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, voltage_excit_source, voltage_excit_val,
            custom_scale_name)
        self.check_for_error(error_code)

    def create_tedsai_force_iepe_chan(
            self, task, physical_channel, name_to_assign_to_channel,
            terminal_config, min_val, max_val, units, current_excit_source,
            current_excit_val, custom_scale_name):
        c_func = lib_importer.windll.DAQmxCreateTEDSAIForceIEPEChan
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_int, ctypes.c_double,
                        ctypes.c_double, ctypes.c_int, ctypes.c_int,
                        ctypes.c_double, ctypes_byte_str]

        error_code = c_func(
            task, physical_channel, name_to_assign_to_channel,
            terminal_config, min_val, max_val, units, current_excit_source,
            current_excit_val, custom_scale_name)
        self.check_for_error(error_code)

    def create_tedsai_microphone_chan(
            self, task, physical_channel, name_to_assign_to_channel,
            terminal_config, units, max_snd_press_level, current_excit_source,
            current_excit_val, custom_scale_name):
        c_func = lib_importer.windll.DAQmxCreateTEDSAIMicrophoneChan
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_int, ctypes.c_int,
                        ctypes.c_double, ctypes.c_int, ctypes.c_double,
                        ctypes_byte_str]

        error_code = c_func(
            task, physical_channel, name_to_assign_to_channel,
            terminal_config, units, max_snd_press_level, current_excit_source,
            current_excit_val, custom_scale_name)
        self.check_for_error(error_code)

    def create_tedsai_pos_lvdt_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, voltage_excit_source, voltage_excit_val,
            voltage_excit_freq, ac_excit_wire_mode, custom_scale_name):
        c_func = lib_importer.windll.DAQmxCreateTEDSAIPosLVDTChan
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes.c_int, ctypes.c_double,
                        ctypes.c_double, ctypes.c_int, ctypes_byte_str]

        error_code = c_func(
            task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, voltage_excit_source, voltage_excit_val,
            voltage_excit_freq, ac_excit_wire_mode, custom_scale_name)
        self.check_for_error(error_code)

    def create_tedsai_pos_rvdt_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, voltage_excit_source, voltage_excit_val,
            voltage_excit_freq, ac_excit_wire_mode, custom_scale_name):
        c_func = lib_importer.windll.DAQmxCreateTEDSAIPosRVDTChan
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes.c_int, ctypes.c_double,
                        ctypes.c_double, ctypes.c_int, ctypes_byte_str]

        error_code = c_func(
            task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, voltage_excit_source, voltage_excit_val,
            voltage_excit_freq, ac_excit_wire_mode, custom_scale_name)
        self.check_for_error(error_code)

    def create_tedsai_pressure_bridge_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, voltage_excit_source, voltage_excit_val,
            custom_scale_name):
        c_func = lib_importer.windll.DAQmxCreateTEDSAIPressureBridgeChan
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes.c_int, ctypes.c_double,
                        ctypes_byte_str]

        error_code = c_func(
            task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, voltage_excit_source, voltage_excit_val,
            custom_scale_name)
        self.check_for_error(error_code)

    def create_tedsai_resistance_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, resistance_config, current_excit_source,
            current_excit_val, custom_scale_name):
        c_func = lib_importer.windll.DAQmxCreateTEDSAIResistanceChan
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes.c_int, ctypes.c_int,
                        ctypes.c_double, ctypes_byte_str]

        error_code = c_func(
            task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, resistance_config, current_excit_source,
            current_excit_val, custom_scale_name)
        self.check_for_error(error_code)

    def create_tedsai_strain_gage_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, voltage_excit_source, voltage_excit_val,
            initial_bridge_voltage, lead_wire_resistance, custom_scale_name):
        c_func = lib_importer.windll.DAQmxCreateTEDSAIStrainGageChan
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes.c_int, ctypes.c_double,
                        ctypes.c_double, ctypes.c_double, ctypes_byte_str]

        error_code = c_func(
            task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, voltage_excit_source, voltage_excit_val,
            initial_bridge_voltage, lead_wire_resistance, custom_scale_name)
        self.check_for_error(error_code)

    def create_tedsai_thrmcpl_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, cjc_source, cjc_val, cjc_channel):
        c_func = lib_importer.windll.DAQmxCreateTEDSAIThrmcplChan
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes.c_int, ctypes.c_double,
                        ctypes_byte_str]

        error_code = c_func(
            task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, cjc_source, cjc_val, cjc_channel)
        self.check_for_error(error_code)

    def create_tedsai_thrmstr_chan_iex(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, resistance_config, current_excit_source,
            current_excit_val):
        c_func = lib_importer.windll.DAQmxCreateTEDSAIThrmstrChanIex
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes.c_int, ctypes.c_int,
                        ctypes.c_double]

        error_code = c_func(
            task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, resistance_config, current_excit_source,
            current_excit_val)
        self.check_for_error(error_code)

    def create_tedsai_thrmstr_chan_vex(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, resistance_config, voltage_excit_source,
            voltage_excit_val, r_1):
        c_func = lib_importer.windll.DAQmxCreateTEDSAIThrmstrChanVex
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes.c_int, ctypes.c_int,
                        ctypes.c_double, ctypes.c_double]

        error_code = c_func(
            task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, resistance_config, voltage_excit_source,
            voltage_excit_val, r_1)
        self.check_for_error(error_code)

    def create_tedsai_torque_bridge_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, voltage_excit_source, voltage_excit_val,
            custom_scale_name):
        c_func = lib_importer.windll.DAQmxCreateTEDSAITorqueBridgeChan
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes.c_int, ctypes.c_double,
                        ctypes_byte_str]

        error_code = c_func(
            task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, voltage_excit_source, voltage_excit_val,
            custom_scale_name)
        self.check_for_error(error_code)

    def create_tedsai_voltage_chan(
            self, task, physical_channel, name_to_assign_to_channel,
            terminal_config, min_val, max_val, units, custom_scale_name):
        c_func = lib_importer.windll.DAQmxCreateTEDSAIVoltageChan
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_int, ctypes.c_double,
                        ctypes.c_double, ctypes.c_int, ctypes_byte_str]

        error_code = c_func(
            task, physical_channel, name_to_assign_to_channel,
            terminal_config, min_val, max_val, units, custom_scale_name)
        self.check_for_error(error_code)

    def create_tedsai_voltage_chan_with_excit(
            self, task, physical_channel, name_to_assign_to_channel,
            terminal_config, min_val, max_val, units, voltage_excit_source,
            voltage_excit_val, custom_scale_name):
        c_func = lib_importer.windll.DAQmxCreateTEDSAIVoltageChanWithExcit
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_int, ctypes.c_double,
                        ctypes.c_double, ctypes.c_int, ctypes.c_int,
                        ctypes.c_double, ctypes_byte_str]

        error_code = c_func(
            task, physical_channel, name_to_assign_to_channel,
            terminal_config, min_val, max_val, units, voltage_excit_source,
            voltage_excit_val, custom_scale_name)
        self.check_for_error(error_code)

    def create_tedsairtd_chan(
            self, task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, resistance_config, current_excit_source,
            current_excit_val):
        c_func = lib_importer.windll.DAQmxCreateTEDSAIRTDChan
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_double, ctypes.c_double,
                        ctypes.c_int, ctypes.c_int, ctypes.c_int,
                        ctypes.c_double]

        error_code = c_func(
            task, physical_channel, name_to_assign_to_channel, min_val,
            max_val, units, resistance_config, current_excit_source,
            current_excit_val)
        self.check_for_error(error_code)

    def create_watchdog_timer_task_ex(
            self, device_name, session_name, timeout):
        new_session_initialized = True
        task = lib_importer.task_handle(0)

        c_func = lib_importer.windll.DAQmxCreateWatchdogTimerTaskEx
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes_byte_str, ctypes_byte_str,
                        ctypes.POINTER(lib_importer.task_handle),
                        ctypes.c_double]

        error_code = c_func(
            device_name, session_name, ctypes.byref(task), timeout)
        self.check_for_error(error_code)
        return task, new_session_initialized

    def delete_network_device(self, device_name):
        c_func = lib_importer.windll.DAQmxDeleteNetworkDevice
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes_byte_str]

        error_code = c_func(
            device_name)
        self.check_for_error(error_code)

    def delete_saved_global_chan(self, channel_name):
        c_func = lib_importer.windll.DAQmxDeleteSavedGlobalChan
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes_byte_str]

        error_code = c_func(
            channel_name)
        self.check_for_error(error_code)

    def delete_saved_scale(self, scale_name):
        c_func = lib_importer.windll.DAQmxDeleteSavedScale
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes_byte_str]

        error_code = c_func(
            scale_name)
        self.check_for_error(error_code)

    def delete_saved_task(self, task_name):
        c_func = lib_importer.windll.DAQmxDeleteSavedTask
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes_byte_str]

        error_code = c_func(
            task_name)
        self.check_for_error(error_code)

    def device_supports_cal(self, device_name):
        cal_supported = c_bool32()

        c_func = lib_importer.windll.DAQmxDeviceSupportsCal
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes_byte_str, ctypes.POINTER(c_bool32)]

        error_code = c_func(
            device_name, ctypes.byref(cal_supported))
        self.check_for_error(error_code)
        return cal_supported.value

    def disable_ref_trig(self, task):
        c_func = lib_importer.windll.DAQmxDisableRefTrig
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle]

        error_code = c_func(
            task)
        self.check_for_error(error_code)

    def disable_start_trig(self, task):
        c_func = lib_importer.windll.DAQmxDisableStartTrig
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle]

        error_code = c_func(
            task)
        self.check_for_error(error_code)

    def disconnect_terms(self, source_terminal, destination_terminal):
        c_func = lib_importer.windll.DAQmxDisconnectTerms
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes_byte_str, ctypes_byte_str]

        error_code = c_func(
            source_terminal, destination_terminal)
        self.check_for_error(error_code)

    def export_signal(self, task, signal_id, output_terminal):
        c_func = lib_importer.windll.DAQmxExportSignal
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int,
                        ctypes_byte_str]

        error_code = c_func(
            task, signal_id, output_terminal)
        self.check_for_error(error_code)

    def get_analog_power_up_states_with_output_type(
            self, channel_names, array_size):
        state_array = numpy.zeros(array_size, dtype=numpy.float64)
        channel_type_array = numpy.zeros(array_size, dtype=numpy.int32)
        array_size = ctypes.c_uint32(array_size)

        c_func = lib_importer.cdll.DAQmxGetAnalogPowerUpStatesWithOutputType
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes_byte_str,
                        wrapped_ndpointer(dtype=numpy.float64,
                        flags=('C','W')), wrapped_ndpointer(dtype=numpy.int32,
                        flags=('C','W')), ctypes.POINTER(ctypes.c_uint)]

        error_code = c_func(
            channel_names, state_array, channel_type_array,
            ctypes.byref(array_size))
        self.check_for_error(error_code)
        return state_array.tolist(), channel_type_array.tolist()

    def get_auto_configured_cdaq_sync_connections(self):
        c_func = lib_importer.windll.DAQmxGetAutoConfiguredCDAQSyncConnections
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes.c_char_p, ctypes.c_uint]

        temp_size = 0
        while True:
            port_list = ctypes.create_string_buffer(temp_size)
            size_or_code = c_func(
                port_list, temp_size)
            if is_string_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break
        self.check_for_error(size_or_code)
        return port_list.value.decode(lib_importer.encoding)

    def get_buffer_attribute_uint32(self, task, attribute):
        value = ctypes.c_uint32()

        c_func = lib_importer.cdll.DAQmxGetBufferAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int32]

        error_code = c_func(
            task, attribute, ctypes.byref(value))
        self.check_for_error(error_code)
        return value.value

    def get_cal_info_attribute_bool(self, device_name, attribute):
        value = c_bool32()

        c_func = lib_importer.cdll.DAQmxGetCalInfoAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes_byte_str, ctypes.c_int32]

        error_code = c_func(
            device_name, attribute, ctypes.byref(value))
        self.check_for_error(error_code)
        return value.value

    def get_cal_info_attribute_double(self, device_name, attribute):
        value = ctypes.c_double()

        c_func = lib_importer.cdll.DAQmxGetCalInfoAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes_byte_str, ctypes.c_int32]

        error_code = c_func(
            device_name, attribute, ctypes.byref(value))
        self.check_for_error(error_code)
        return value.value

    def get_cal_info_attribute_string(self, device_name, attribute):
        c_func = lib_importer.cdll.DAQmxGetCalInfoAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes_byte_str, ctypes.c_int32]

        temp_size = 0
        while True:
            value = ctypes.create_string_buffer(temp_size)
            size_or_code = c_func(
                device_name, attribute, value, temp_size)
            if is_string_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break
        self.check_for_error(size_or_code)
        return value.value.decode(lib_importer.encoding)

    def get_cal_info_attribute_uint32(self, device_name, attribute):
        value = ctypes.c_uint32()

        c_func = lib_importer.cdll.DAQmxGetCalInfoAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes_byte_str, ctypes.c_int32]

        error_code = c_func(
            device_name, attribute, ctypes.byref(value))
        self.check_for_error(error_code)
        return value.value

    def get_chan_attribute_bool(self, task, channel, attribute):
        value = c_bool32()

        c_func = lib_importer.cdll.DAQmxGetChanAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int32]

        error_code = c_func(
            task, channel, attribute, ctypes.byref(value))
        self.check_for_error(error_code)
        return value.value

    def get_chan_attribute_double(self, task, channel, attribute):
        value = ctypes.c_double()

        c_func = lib_importer.cdll.DAQmxGetChanAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int32]

        error_code = c_func(
            task, channel, attribute, ctypes.byref(value))
        self.check_for_error(error_code)
        return value.value

    def get_chan_attribute_double_array(self, task, channel, attribute):
        c_func = lib_importer.cdll.DAQmxGetChanAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int32]

        temp_size = 0
        while True:
            value = numpy.zeros(temp_size, dtype=numpy.float64)
            size_or_code = c_func(
                task, channel, attribute,
                value.ctypes.data_as(ctypes.c_void_p), temp_size)
            if is_array_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break
        self.check_for_error(size_or_code)
        return value.tolist()

    def get_chan_attribute_int32(self, task, channel, attribute):
        value = ctypes.c_int32()

        c_func = lib_importer.cdll.DAQmxGetChanAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int32]

        error_code = c_func(
            task, channel, attribute, ctypes.byref(value))
        self.check_for_error(error_code)
        return value.value

    def get_chan_attribute_string(self, task, channel, attribute):
        c_func = lib_importer.cdll.DAQmxGetChanAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int32]

        temp_size = 0
        while True:
            value = ctypes.create_string_buffer(temp_size)
            size_or_code = c_func(
                task, channel, attribute, value, temp_size)
            if is_string_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break
        self.check_for_error(size_or_code)
        return value.value.decode(lib_importer.encoding)

    def get_chan_attribute_uint32(self, task, channel, attribute):
        value = ctypes.c_uint32()

        c_func = lib_importer.cdll.DAQmxGetChanAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int32]

        error_code = c_func(
            task, channel, attribute, ctypes.byref(value))
        self.check_for_error(error_code)
        return value.value

    def get_device_attribute_bool(self, device_name, attribute):
        value = c_bool32()

        c_func = lib_importer.cdll.DAQmxGetDeviceAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes_byte_str, ctypes.c_int32]

        error_code = c_func(
            device_name, attribute, ctypes.byref(value))
        self.check_for_error(error_code)
        return value.value

    def get_device_attribute_double(self, device_name, attribute):
        value = ctypes.c_double()

        c_func = lib_importer.cdll.DAQmxGetDeviceAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes_byte_str, ctypes.c_int32]

        error_code = c_func(
            device_name, attribute, ctypes.byref(value))
        self.check_for_error(error_code)
        return value.value

    def get_device_attribute_double_array(self, device_name, attribute):
        c_func = lib_importer.cdll.DAQmxGetDeviceAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes_byte_str, ctypes.c_int32]

        temp_size = 0
        while True:
            value = numpy.zeros(temp_size, dtype=numpy.float64)
            size_or_code = c_func(
                device_name, attribute, value.ctypes.data_as(ctypes.c_void_p),
                temp_size)
            if is_array_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break
        self.check_for_error(size_or_code)
        return value.tolist()

    def get_device_attribute_int32(self, device_name, attribute):
        value = ctypes.c_int32()

        c_func = lib_importer.cdll.DAQmxGetDeviceAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes_byte_str, ctypes.c_int32]

        error_code = c_func(
            device_name, attribute, ctypes.byref(value))
        self.check_for_error(error_code)
        return value.value

    def get_device_attribute_int32_array(self, device_name, attribute):
        c_func = lib_importer.cdll.DAQmxGetDeviceAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes_byte_str, ctypes.c_int32]

        temp_size = 0
        while True:
            value = numpy.zeros(temp_size, dtype=numpy.int32)
            size_or_code = c_func(
                device_name, attribute, value.ctypes.data_as(ctypes.c_void_p),
                temp_size)
            if is_array_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break
        self.check_for_error(size_or_code)
        return value.tolist()

    def get_device_attribute_string(self, device_name, attribute):
        c_func = lib_importer.cdll.DAQmxGetDeviceAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes_byte_str, ctypes.c_int32]

        temp_size = 0
        while True:
            value = ctypes.create_string_buffer(temp_size)
            size_or_code = c_func(
                device_name, attribute, value, temp_size)
            if is_string_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break
        self.check_for_error(size_or_code)
        return value.value.decode(lib_importer.encoding)

    def get_device_attribute_uint32(self, device_name, attribute):
        value = ctypes.c_uint32()

        c_func = lib_importer.cdll.DAQmxGetDeviceAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes_byte_str, ctypes.c_int32]

        error_code = c_func(
            device_name, attribute, ctypes.byref(value))
        self.check_for_error(error_code)
        return value.value

    def get_device_attribute_uint32_array(self, device_name, attribute):
        c_func = lib_importer.cdll.DAQmxGetDeviceAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes_byte_str, ctypes.c_int32]

        temp_size = 0
        while True:
            value = numpy.zeros(temp_size, dtype=numpy.uint32)
            size_or_code = c_func(
                device_name, attribute, value.ctypes.data_as(ctypes.c_void_p),
                temp_size)
            if is_array_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break
        self.check_for_error(size_or_code)
        return value.tolist()

    def get_digital_logic_family_power_up_state(self, device_name):
        logic_family = ctypes.c_int()

        c_func = lib_importer.windll.DAQmxGetDigitalLogicFamilyPowerUpState
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes_byte_str, ctypes.POINTER(ctypes.c_int)]

        error_code = c_func(
            device_name, ctypes.byref(logic_family))
        self.check_for_error(error_code)
        return logic_family.value

    def get_digital_power_up_states(self, device_name, channel_name):
        state = []

        args = [device_name]
        argtypes: list[type] = [ctypes_byte_str]

        for index in range(len(channel_name)):
            state_element = ctypes.c_int32()
            state.append(state_element)

            args.append(channel_name[index])
            argtypes.append(ctypes_byte_str)
            
            args.append(ctypes.byref(state_element))
            argtypes.append(ctypes.POINTER(ctypes.c_int32))
            
        args.append(None)
        argtypes.append(ctypes.c_void_p)

        c_func = lib_importer.cdll.DAQmxGetDigitalPowerUpStates
        with c_func.arg_lock:
            c_func.argtypes = argtypes
            error_code = c_func(*args)
        self.check_for_error(error_code)
        return [state_element.value for state_element in state]

    def get_digital_pull_up_pull_down_states(self, device_name, channel_name):
        state = []

        args = [device_name]
        argtypes: list[type] = [ctypes_byte_str]

        for index in range(len(channel_name)):
            state_element = ctypes.c_int32()
            state.append(state_element)

            args.append(channel_name[index])
            argtypes.append(ctypes_byte_str)
            
            args.append(ctypes.byref(state_element))
            argtypes.append(ctypes.POINTER(ctypes.c_int32))
            
        args.append(None)
        argtypes.append(ctypes.c_void_p)

        c_func = lib_importer.cdll.DAQmxGetDigitalPullUpPullDownStates
        with c_func.arg_lock:
            c_func.argtypes = argtypes
            error_code = c_func(*args)
        self.check_for_error(error_code)
        return [state_element.value for state_element in state]

    def get_disconnected_cdaq_sync_ports(self):
        c_func = lib_importer.windll.DAQmxGetDisconnectedCDAQSyncPorts
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes.c_char_p, ctypes.c_uint]

        temp_size = 0
        while True:
            port_list = ctypes.create_string_buffer(temp_size)
            size_or_code = c_func(
                port_list, temp_size)
            if is_string_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break
        self.check_for_error(size_or_code)
        return port_list.value.decode(lib_importer.encoding)

    def get_exported_signal_attribute_bool(self, task, attribute):
        value = c_bool32()

        c_func = lib_importer.cdll.DAQmxGetExportedSignalAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int32]

        error_code = c_func(
            task, attribute, ctypes.byref(value))
        self.check_for_error(error_code)
        return value.value

    def get_exported_signal_attribute_double(self, task, attribute):
        value = ctypes.c_double()

        c_func = lib_importer.cdll.DAQmxGetExportedSignalAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int32]

        error_code = c_func(
            task, attribute, ctypes.byref(value))
        self.check_for_error(error_code)
        return value.value

    def get_exported_signal_attribute_int32(self, task, attribute):
        value = ctypes.c_int32()

        c_func = lib_importer.cdll.DAQmxGetExportedSignalAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int32]

        error_code = c_func(
            task, attribute, ctypes.byref(value))
        self.check_for_error(error_code)
        return value.value

    def get_exported_signal_attribute_string(self, task, attribute):
        c_func = lib_importer.cdll.DAQmxGetExportedSignalAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int32]

        temp_size = 0
        while True:
            value = ctypes.create_string_buffer(temp_size)
            size_or_code = c_func(
                task, attribute, value, temp_size)
            if is_string_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break
        self.check_for_error(size_or_code)
        return value.value.decode(lib_importer.encoding)

    def get_exported_signal_attribute_uint32(self, task, attribute):
        value = ctypes.c_uint32()

        c_func = lib_importer.cdll.DAQmxGetExportedSignalAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int32]

        error_code = c_func(
            task, attribute, ctypes.byref(value))
        self.check_for_error(error_code)
        return value.value

    def get_ext_cal_last_date_and_time(self, device_name):
        year = ctypes.c_uint()
        month = ctypes.c_uint()
        day = ctypes.c_uint()
        hour = ctypes.c_uint()
        minute = ctypes.c_uint()

        c_func = lib_importer.windll.DAQmxGetExtCalLastDateAndTime
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes_byte_str, ctypes.POINTER(ctypes.c_uint),
                        ctypes.POINTER(ctypes.c_uint),
                        ctypes.POINTER(ctypes.c_uint),
                        ctypes.POINTER(ctypes.c_uint),
                        ctypes.POINTER(ctypes.c_uint)]

        error_code = c_func(
            device_name, ctypes.byref(year), ctypes.byref(month),
            ctypes.byref(day), ctypes.byref(hour), ctypes.byref(minute))
        self.check_for_error(error_code)
        return year.value, month.value, day.value, hour.value, minute.value

    def get_persisted_chan_attribute_bool(self, channel, attribute):
        value = c_bool32()

        c_func = lib_importer.cdll.DAQmxGetPersistedChanAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes_byte_str, ctypes.c_int32]

        error_code = c_func(
            channel, attribute, ctypes.byref(value))
        self.check_for_error(error_code)
        return value.value

    def get_persisted_chan_attribute_string(self, channel, attribute):
        c_func = lib_importer.cdll.DAQmxGetPersistedChanAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes_byte_str, ctypes.c_int32]

        temp_size = 0
        while True:
            value = ctypes.create_string_buffer(temp_size)
            size_or_code = c_func(
                channel, attribute, value, temp_size)
            if is_string_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break
        self.check_for_error(size_or_code)
        return value.value.decode(lib_importer.encoding)

    def get_persisted_scale_attribute_bool(self, scale_name, attribute):
        value = c_bool32()

        c_func = lib_importer.cdll.DAQmxGetPersistedScaleAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes_byte_str, ctypes.c_int32]

        error_code = c_func(
            scale_name, attribute, ctypes.byref(value))
        self.check_for_error(error_code)
        return value.value

    def get_persisted_scale_attribute_string(self, scale_name, attribute):
        c_func = lib_importer.cdll.DAQmxGetPersistedScaleAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes_byte_str, ctypes.c_int32]

        temp_size = 0
        while True:
            value = ctypes.create_string_buffer(temp_size)
            size_or_code = c_func(
                scale_name, attribute, value, temp_size)
            if is_string_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break
        self.check_for_error(size_or_code)
        return value.value.decode(lib_importer.encoding)

    def get_persisted_task_attribute_bool(self, task_name, attribute):
        value = c_bool32()

        c_func = lib_importer.cdll.DAQmxGetPersistedTaskAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes_byte_str, ctypes.c_int32]

        error_code = c_func(
            task_name, attribute, ctypes.byref(value))
        self.check_for_error(error_code)
        return value.value

    def get_persisted_task_attribute_string(self, task_name, attribute):
        c_func = lib_importer.cdll.DAQmxGetPersistedTaskAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes_byte_str, ctypes.c_int32]

        temp_size = 0
        while True:
            value = ctypes.create_string_buffer(temp_size)
            size_or_code = c_func(
                task_name, attribute, value, temp_size)
            if is_string_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break
        self.check_for_error(size_or_code)
        return value.value.decode(lib_importer.encoding)

    def get_physical_chan_attribute_bool(self, physical_channel, attribute):
        value = c_bool32()

        c_func = lib_importer.cdll.DAQmxGetPhysicalChanAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes_byte_str, ctypes.c_int32]

        error_code = c_func(
            physical_channel, attribute, ctypes.byref(value))
        self.check_for_error(error_code)
        return value.value

    def get_physical_chan_attribute_bytes(self, physical_channel, attribute):
        c_func = lib_importer.cdll.DAQmxGetPhysicalChanAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes_byte_str, ctypes.c_int32]

        temp_size = 0
        while True:
            value = numpy.zeros(temp_size, dtype=numpy.uint8)
            size_or_code = c_func(
                physical_channel, attribute,
                value.ctypes.data_as(ctypes.c_void_p), temp_size)
            if is_array_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break
        self.check_for_error(size_or_code)
        return value.tolist()

    def get_physical_chan_attribute_double(self, physical_channel, attribute):
        value = ctypes.c_double()

        c_func = lib_importer.cdll.DAQmxGetPhysicalChanAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes_byte_str, ctypes.c_int32]

        error_code = c_func(
            physical_channel, attribute, ctypes.byref(value))
        self.check_for_error(error_code)
        return value.value

    def get_physical_chan_attribute_double_array(
            self, physical_channel, attribute):
        c_func = lib_importer.cdll.DAQmxGetPhysicalChanAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes_byte_str, ctypes.c_int32]

        temp_size = 0
        while True:
            value = numpy.zeros(temp_size, dtype=numpy.float64)
            size_or_code = c_func(
                physical_channel, attribute,
                value.ctypes.data_as(ctypes.c_void_p), temp_size)
            if is_array_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break
        self.check_for_error(size_or_code)
        return value.tolist()

    def get_physical_chan_attribute_int32(self, physical_channel, attribute):
        value = ctypes.c_int32()

        c_func = lib_importer.cdll.DAQmxGetPhysicalChanAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes_byte_str, ctypes.c_int32]

        error_code = c_func(
            physical_channel, attribute, ctypes.byref(value))
        self.check_for_error(error_code)
        return value.value

    def get_physical_chan_attribute_int32_array(
            self, physical_channel, attribute):
        c_func = lib_importer.cdll.DAQmxGetPhysicalChanAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes_byte_str, ctypes.c_int32]

        temp_size = 0
        while True:
            value = numpy.zeros(temp_size, dtype=numpy.int32)
            size_or_code = c_func(
                physical_channel, attribute,
                value.ctypes.data_as(ctypes.c_void_p), temp_size)
            if is_array_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break
        self.check_for_error(size_or_code)
        return value.tolist()

    def get_physical_chan_attribute_string(self, physical_channel, attribute):
        c_func = lib_importer.cdll.DAQmxGetPhysicalChanAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes_byte_str, ctypes.c_int32]

        temp_size = 0
        while True:
            value = ctypes.create_string_buffer(temp_size)
            size_or_code = c_func(
                physical_channel, attribute, value, temp_size)
            if is_string_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break
        self.check_for_error(size_or_code)
        return value.value.decode(lib_importer.encoding)

    def get_physical_chan_attribute_uint32(self, physical_channel, attribute):
        value = ctypes.c_uint32()

        c_func = lib_importer.cdll.DAQmxGetPhysicalChanAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes_byte_str, ctypes.c_int32]

        error_code = c_func(
            physical_channel, attribute, ctypes.byref(value))
        self.check_for_error(error_code)
        return value.value

    def get_physical_chan_attribute_uint32_array(
            self, physical_channel, attribute):
        c_func = lib_importer.cdll.DAQmxGetPhysicalChanAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes_byte_str, ctypes.c_int32]

        temp_size = 0
        while True:
            value = numpy.zeros(temp_size, dtype=numpy.uint32)
            size_or_code = c_func(
                physical_channel, attribute,
                value.ctypes.data_as(ctypes.c_void_p), temp_size)
            if is_array_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break
        self.check_for_error(size_or_code)
        return value.tolist()

    def get_read_attribute_bool(self, task, attribute):
        value = c_bool32()

        c_func = lib_importer.cdll.DAQmxGetReadAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int32]

        error_code = c_func(
            task, attribute, ctypes.byref(value))
        self.check_for_error(error_code)
        return value.value

    def get_read_attribute_double(self, task, attribute):
        value = ctypes.c_double()

        c_func = lib_importer.cdll.DAQmxGetReadAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int32]

        error_code = c_func(
            task, attribute, ctypes.byref(value))
        self.check_for_error(error_code)
        return value.value

    def get_read_attribute_int32(self, task, attribute):
        value = ctypes.c_int32()

        c_func = lib_importer.cdll.DAQmxGetReadAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int32]

        error_code = c_func(
            task, attribute, ctypes.byref(value))
        self.check_for_error(error_code)
        return value.value

    def get_read_attribute_string(self, task, attribute, size_hint=0):
        c_func = lib_importer.cdll.DAQmxGetReadAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int32]

        temp_size = size_hint
        while True:
            value = ctypes.create_string_buffer(temp_size)
            size_or_code = c_func(
                task, attribute, value, temp_size)
            if is_string_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break
        self.check_for_error(size_or_code)
        return value.value.decode(lib_importer.encoding)

    def get_read_attribute_uint32(self, task, attribute):
        value = ctypes.c_uint32()

        c_func = lib_importer.cdll.DAQmxGetReadAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int32]

        error_code = c_func(
            task, attribute, ctypes.byref(value))
        self.check_for_error(error_code)
        return value.value

    def get_read_attribute_uint64(self, task, attribute):
        value = ctypes.c_uint64()

        c_func = lib_importer.cdll.DAQmxGetReadAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int32]

        error_code = c_func(
            task, attribute, ctypes.byref(value))
        self.check_for_error(error_code)
        return value.value

    def get_scale_attribute_double(self, scale_name, attribute):
        value = ctypes.c_double()

        c_func = lib_importer.cdll.DAQmxGetScaleAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes_byte_str, ctypes.c_int32]

        error_code = c_func(
            scale_name, attribute, ctypes.byref(value))
        self.check_for_error(error_code)
        return value.value

    def get_scale_attribute_double_array(self, scale_name, attribute):
        c_func = lib_importer.cdll.DAQmxGetScaleAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes_byte_str, ctypes.c_int32]

        temp_size = 0
        while True:
            value = numpy.zeros(temp_size, dtype=numpy.float64)
            size_or_code = c_func(
                scale_name, attribute, value.ctypes.data_as(ctypes.c_void_p),
                temp_size)
            if is_array_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break
        self.check_for_error(size_or_code)
        return value.tolist()

    def get_scale_attribute_int32(self, scale_name, attribute):
        value = ctypes.c_int32()

        c_func = lib_importer.cdll.DAQmxGetScaleAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes_byte_str, ctypes.c_int32]

        error_code = c_func(
            scale_name, attribute, ctypes.byref(value))
        self.check_for_error(error_code)
        return value.value

    def get_scale_attribute_string(self, scale_name, attribute):
        c_func = lib_importer.cdll.DAQmxGetScaleAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes_byte_str, ctypes.c_int32]

        temp_size = 0
        while True:
            value = ctypes.create_string_buffer(temp_size)
            size_or_code = c_func(
                scale_name, attribute, value, temp_size)
            if is_string_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break
        self.check_for_error(size_or_code)
        return value.value.decode(lib_importer.encoding)

    def get_self_cal_last_date_and_time(self, device_name):
        year = ctypes.c_uint()
        month = ctypes.c_uint()
        day = ctypes.c_uint()
        hour = ctypes.c_uint()
        minute = ctypes.c_uint()

        c_func = lib_importer.windll.DAQmxGetSelfCalLastDateAndTime
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes_byte_str, ctypes.POINTER(ctypes.c_uint),
                        ctypes.POINTER(ctypes.c_uint),
                        ctypes.POINTER(ctypes.c_uint),
                        ctypes.POINTER(ctypes.c_uint),
                        ctypes.POINTER(ctypes.c_uint)]

        error_code = c_func(
            device_name, ctypes.byref(year), ctypes.byref(month),
            ctypes.byref(day), ctypes.byref(hour), ctypes.byref(minute))
        self.check_for_error(error_code)
        return year.value, month.value, day.value, hour.value, minute.value

    def get_system_info_attribute_string(self, attribute):
        c_func = lib_importer.cdll.DAQmxGetSystemInfoAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes.c_int32]

        temp_size = 0
        while True:
            value = ctypes.create_string_buffer(temp_size)
            size_or_code = c_func(
                attribute, value, temp_size)
            if is_string_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break
        self.check_for_error(size_or_code)
        return value.value.decode(lib_importer.encoding)

    def get_system_info_attribute_uint32(self, attribute):
        value = ctypes.c_uint32()

        c_func = lib_importer.cdll.DAQmxGetSystemInfoAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes.c_int32]

        error_code = c_func(
            attribute, ctypes.byref(value))
        self.check_for_error(error_code)
        return value.value

    def get_task_attribute_bool(self, task, attribute):
        value = c_bool32()

        c_func = lib_importer.cdll.DAQmxGetTaskAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int32]

        error_code = c_func(
            task, attribute, ctypes.byref(value))
        self.check_for_error(error_code)
        return value.value

    def get_task_attribute_string(self, task, attribute):
        c_func = lib_importer.cdll.DAQmxGetTaskAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int32]

        temp_size = 0
        while True:
            value = ctypes.create_string_buffer(temp_size)
            size_or_code = c_func(
                task, attribute, value, temp_size)
            if is_string_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break
        self.check_for_error(size_or_code)
        return value.value.decode(lib_importer.encoding)

    def get_task_attribute_uint32(self, task, attribute):
        value = ctypes.c_uint32()

        c_func = lib_importer.cdll.DAQmxGetTaskAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int32]

        error_code = c_func(
            task, attribute, ctypes.byref(value))
        self.check_for_error(error_code)
        return value.value

    def get_timing_attribute_bool(self, task, attribute):
        value = c_bool32()

        c_func = lib_importer.cdll.DAQmxGetTimingAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int32]

        error_code = c_func(
            task, attribute, ctypes.byref(value))
        self.check_for_error(error_code)
        return value.value

    def get_timing_attribute_double(self, task, attribute):
        value = ctypes.c_double()

        c_func = lib_importer.cdll.DAQmxGetTimingAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int32]

        error_code = c_func(
            task, attribute, ctypes.byref(value))
        self.check_for_error(error_code)
        return value.value

    def get_timing_attribute_ex_bool(self, task, device_names, attribute):
        value = c_bool32()

        c_func = lib_importer.cdll.DAQmxGetTimingAttributeEx
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int32]

        error_code = c_func(
            task, device_names, attribute, ctypes.byref(value))
        self.check_for_error(error_code)
        return value.value

    def get_timing_attribute_ex_double(self, task, device_names, attribute):
        value = ctypes.c_double()

        c_func = lib_importer.cdll.DAQmxGetTimingAttributeEx
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int32]

        error_code = c_func(
            task, device_names, attribute, ctypes.byref(value))
        self.check_for_error(error_code)
        return value.value

    def get_timing_attribute_ex_int32(self, task, device_names, attribute):
        value = ctypes.c_int32()

        c_func = lib_importer.cdll.DAQmxGetTimingAttributeEx
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int32]

        error_code = c_func(
            task, device_names, attribute, ctypes.byref(value))
        self.check_for_error(error_code)
        return value.value

    def get_timing_attribute_ex_string(self, task, device_names, attribute):
        c_func = lib_importer.cdll.DAQmxGetTimingAttributeEx
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int32]

        temp_size = 0
        while True:
            value = ctypes.create_string_buffer(temp_size)
            size_or_code = c_func(
                task, device_names, attribute, value, temp_size)
            if is_string_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break
        self.check_for_error(size_or_code)
        return value.value.decode(lib_importer.encoding)

    def get_timing_attribute_ex_uint32(self, task, device_names, attribute):
        value = ctypes.c_uint32()

        c_func = lib_importer.cdll.DAQmxGetTimingAttributeEx
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int32]

        error_code = c_func(
            task, device_names, attribute, ctypes.byref(value))
        self.check_for_error(error_code)
        return value.value

    def get_timing_attribute_ex_uint64(self, task, device_names, attribute):
        value = ctypes.c_uint64()

        c_func = lib_importer.cdll.DAQmxGetTimingAttributeEx
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int32]

        error_code = c_func(
            task, device_names, attribute, ctypes.byref(value))
        self.check_for_error(error_code)
        return value.value

    def get_timing_attribute_int32(self, task, attribute):
        value = ctypes.c_int32()

        c_func = lib_importer.cdll.DAQmxGetTimingAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int32]

        error_code = c_func(
            task, attribute, ctypes.byref(value))
        self.check_for_error(error_code)
        return value.value

    def get_timing_attribute_string(self, task, attribute):
        c_func = lib_importer.cdll.DAQmxGetTimingAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int32]

        temp_size = 0
        while True:
            value = ctypes.create_string_buffer(temp_size)
            size_or_code = c_func(
                task, attribute, value, temp_size)
            if is_string_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break
        self.check_for_error(size_or_code)
        return value.value.decode(lib_importer.encoding)

    def get_timing_attribute_timestamp(self, task, attribute):
        value = AbsoluteTime()

        c_func = lib_importer.cdll.DAQmxGetTimingAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int32]

        error_code = c_func(
            task, attribute, ctypes.byref(value))
        self.check_for_error(error_code)
        return value.to_datetime()

    def get_timing_attribute_uint32(self, task, attribute):
        value = ctypes.c_uint32()

        c_func = lib_importer.cdll.DAQmxGetTimingAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int32]

        error_code = c_func(
            task, attribute, ctypes.byref(value))
        self.check_for_error(error_code)
        return value.value

    def get_timing_attribute_uint64(self, task, attribute):
        value = ctypes.c_uint64()

        c_func = lib_importer.cdll.DAQmxGetTimingAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int32]

        error_code = c_func(
            task, attribute, ctypes.byref(value))
        self.check_for_error(error_code)
        return value.value

    def get_trig_attribute_bool(self, task, attribute):
        value = c_bool32()

        c_func = lib_importer.cdll.DAQmxGetTrigAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int32]

        error_code = c_func(
            task, attribute, ctypes.byref(value))
        self.check_for_error(error_code)
        return value.value

    def get_trig_attribute_double(self, task, attribute):
        value = ctypes.c_double()

        c_func = lib_importer.cdll.DAQmxGetTrigAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int32]

        error_code = c_func(
            task, attribute, ctypes.byref(value))
        self.check_for_error(error_code)
        return value.value

    def get_trig_attribute_double_array(self, task, attribute):
        c_func = lib_importer.cdll.DAQmxGetTrigAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int32]

        temp_size = 0
        while True:
            value = numpy.zeros(temp_size, dtype=numpy.float64)
            size_or_code = c_func(
                task, attribute, value.ctypes.data_as(ctypes.c_void_p),
                temp_size)
            if is_array_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break
        self.check_for_error(size_or_code)
        return value.tolist()

    def get_trig_attribute_int32(self, task, attribute):
        value = ctypes.c_int32()

        c_func = lib_importer.cdll.DAQmxGetTrigAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int32]

        error_code = c_func(
            task, attribute, ctypes.byref(value))
        self.check_for_error(error_code)
        return value.value

    def get_trig_attribute_int32_array(self, task, attribute):
        c_func = lib_importer.cdll.DAQmxGetTrigAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int32]

        temp_size = 0
        while True:
            value = numpy.zeros(temp_size, dtype=numpy.int32)
            size_or_code = c_func(
                task, attribute, value.ctypes.data_as(ctypes.c_void_p),
                temp_size)
            if is_array_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break
        self.check_for_error(size_or_code)
        return value.tolist()

    def get_trig_attribute_string(self, task, attribute):
        c_func = lib_importer.cdll.DAQmxGetTrigAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int32]

        temp_size = 0
        while True:
            value = ctypes.create_string_buffer(temp_size)
            size_or_code = c_func(
                task, attribute, value, temp_size)
            if is_string_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break
        self.check_for_error(size_or_code)
        return value.value.decode(lib_importer.encoding)

    def get_trig_attribute_timestamp(self, task, attribute):
        value = AbsoluteTime()

        c_func = lib_importer.cdll.DAQmxGetTrigAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int32]

        error_code = c_func(
            task, attribute, ctypes.byref(value))
        self.check_for_error(error_code)
        return value.to_datetime()

    def get_trig_attribute_uint32(self, task, attribute):
        value = ctypes.c_uint32()

        c_func = lib_importer.cdll.DAQmxGetTrigAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int32]

        error_code = c_func(
            task, attribute, ctypes.byref(value))
        self.check_for_error(error_code)
        return value.value

    def get_watchdog_attribute_bool(self, task, lines, attribute):
        value = c_bool32()

        c_func = lib_importer.cdll.DAQmxGetWatchdogAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int32]

        error_code = c_func(
            task, lines, attribute, ctypes.byref(value))
        self.check_for_error(error_code)
        return value.value

    def get_watchdog_attribute_double(self, task, lines, attribute):
        value = ctypes.c_double()

        c_func = lib_importer.cdll.DAQmxGetWatchdogAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int32]

        error_code = c_func(
            task, lines, attribute, ctypes.byref(value))
        self.check_for_error(error_code)
        return value.value

    def get_watchdog_attribute_int32(self, task, lines, attribute):
        value = ctypes.c_int32()

        c_func = lib_importer.cdll.DAQmxGetWatchdogAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int32]

        error_code = c_func(
            task, lines, attribute, ctypes.byref(value))
        self.check_for_error(error_code)
        return value.value

    def get_watchdog_attribute_string(self, task, lines, attribute):
        c_func = lib_importer.cdll.DAQmxGetWatchdogAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int32]

        temp_size = 0
        while True:
            value = ctypes.create_string_buffer(temp_size)
            size_or_code = c_func(
                task, lines, attribute, value, temp_size)
            if is_string_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break
        self.check_for_error(size_or_code)
        return value.value.decode(lib_importer.encoding)

    def get_write_attribute_bool(self, task, attribute):
        value = c_bool32()

        c_func = lib_importer.cdll.DAQmxGetWriteAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int32]

        error_code = c_func(
            task, attribute, ctypes.byref(value))
        self.check_for_error(error_code)
        return value.value

    def get_write_attribute_double(self, task, attribute):
        value = ctypes.c_double()

        c_func = lib_importer.cdll.DAQmxGetWriteAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int32]

        error_code = c_func(
            task, attribute, ctypes.byref(value))
        self.check_for_error(error_code)
        return value.value

    def get_write_attribute_int32(self, task, attribute):
        value = ctypes.c_int32()

        c_func = lib_importer.cdll.DAQmxGetWriteAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int32]

        error_code = c_func(
            task, attribute, ctypes.byref(value))
        self.check_for_error(error_code)
        return value.value

    def get_write_attribute_string(self, task, attribute, size_hint=0):
        c_func = lib_importer.cdll.DAQmxGetWriteAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int32]

        temp_size = size_hint
        while True:
            value = ctypes.create_string_buffer(temp_size)
            size_or_code = c_func(
                task, attribute, value, temp_size)
            if is_string_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break
        self.check_for_error(size_or_code)
        return value.value.decode(lib_importer.encoding)

    def get_write_attribute_uint32(self, task, attribute):
        value = ctypes.c_uint32()

        c_func = lib_importer.cdll.DAQmxGetWriteAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int32]

        error_code = c_func(
            task, attribute, ctypes.byref(value))
        self.check_for_error(error_code)
        return value.value

    def get_write_attribute_uint64(self, task, attribute):
        value = ctypes.c_uint64()

        c_func = lib_importer.cdll.DAQmxGetWriteAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int32]

        error_code = c_func(
            task, attribute, ctypes.byref(value))
        self.check_for_error(error_code)
        return value.value

    def internal_get_last_created_chan(self):
        c_func = lib_importer.windll.DAQmxInternalGetLastCreatedChan
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes.c_char_p, ctypes.c_uint]

        temp_size = 0
        while True:
            value = ctypes.create_string_buffer(temp_size)
            size_or_code = c_func(
                value, temp_size)
            if is_string_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break
        self.check_for_error(size_or_code)
        return value.value.decode(lib_importer.encoding)

    def is_task_done(self, task):
        is_task_done = c_bool32()

        c_func = lib_importer.windll.DAQmxIsTaskDone
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(c_bool32)]

        error_code = c_func(
            task, ctypes.byref(is_task_done))
        self.check_for_error(error_code)
        return is_task_done.value

    def load_task(self, session_name):
        new_session_initialized = True
        task = lib_importer.task_handle(0)

        c_func = lib_importer.windll.DAQmxLoadTask
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes_byte_str,
                        ctypes.POINTER(lib_importer.task_handle)]

        error_code = c_func(
            session_name, ctypes.byref(task))
        self.check_for_error(error_code)
        return task, new_session_initialized

    def perform_bridge_offset_nulling_cal_ex(
            self, task, channel, skip_unsupported_channels):
        c_func = lib_importer.windll.DAQmxPerformBridgeOffsetNullingCalEx
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str, c_bool32]

        error_code = c_func(
            task, channel, skip_unsupported_channels)
        self.check_for_error(error_code)

    def perform_bridge_shunt_cal_ex(
            self, task, channel, shunt_resistor_value,
            shunt_resistor_location, shunt_resistor_select,
            shunt_resistor_source, bridge_resistance,
            skip_unsupported_channels):
        c_func = lib_importer.windll.DAQmxPerformBridgeShuntCalEx
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double, ctypes.c_int, ctypes.c_int,
                        ctypes.c_int, ctypes.c_double, c_bool32]

        error_code = c_func(
            task, channel, shunt_resistor_value, shunt_resistor_location,
            shunt_resistor_select, shunt_resistor_source, bridge_resistance,
            skip_unsupported_channels)
        self.check_for_error(error_code)

    def perform_strain_shunt_cal_ex(
            self, task, channel, shunt_resistor_value,
            shunt_resistor_location, shunt_resistor_select,
            shunt_resistor_source, skip_unsupported_channels):
        c_func = lib_importer.windll.DAQmxPerformStrainShuntCalEx
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_double, ctypes.c_int, ctypes.c_int,
                        ctypes.c_int, c_bool32]

        error_code = c_func(
            task, channel, shunt_resistor_value, shunt_resistor_location,
            shunt_resistor_select, shunt_resistor_source,
            skip_unsupported_channels)
        self.check_for_error(error_code)

    def perform_thrmcpl_lead_offset_nulling_cal(
            self, task, channel, skip_unsupported_channels):
        c_func = lib_importer.windll.DAQmxPerformThrmcplLeadOffsetNullingCal
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str, c_bool32]

        error_code = c_func(
            task, channel, skip_unsupported_channels)
        self.check_for_error(error_code)

    def read_analog_f64(
            self, task, num_samps_per_chan, timeout, fill_mode, read_array):
        samps_per_chan_read = ctypes.c_int()

        c_func = lib_importer.windll.DAQmxReadAnalogF64
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int,
                        ctypes.c_double, ctypes.c_int,
                        wrapped_ndpointer(dtype=numpy.float64,
                        flags=('C','W')), ctypes.c_uint,
                        ctypes.POINTER(ctypes.c_int), ctypes.POINTER(c_bool32)]

        error_code = c_func(
            task, num_samps_per_chan, timeout, fill_mode, read_array,
            read_array.size, ctypes.byref(samps_per_chan_read), None)
        self.check_for_error(error_code, samps_per_chan_read=samps_per_chan_read.value)
        return read_array, samps_per_chan_read.value

    def read_analog_scalar_f64(self, task, timeout):
        value = ctypes.c_double()

        c_func = lib_importer.windll.DAQmxReadAnalogScalarF64
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_double,
                        ctypes.POINTER(ctypes.c_double),
                        ctypes.POINTER(c_bool32)]

        error_code = c_func(
            task, timeout, ctypes.byref(value), None)
        self.check_for_error(error_code)
        return value.value

    def read_binary_i16(
            self, task, num_samps_per_chan, timeout, fill_mode, read_array):
        samps_per_chan_read = ctypes.c_int()

        c_func = lib_importer.windll.DAQmxReadBinaryI16
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int,
                        ctypes.c_double, ctypes.c_int,
                        wrapped_ndpointer(dtype=numpy.int16, flags=('C','W')),
                        ctypes.c_uint, ctypes.POINTER(ctypes.c_int),
                        ctypes.POINTER(c_bool32)]

        error_code = c_func(
            task, num_samps_per_chan, timeout, fill_mode, read_array,
            read_array.size, ctypes.byref(samps_per_chan_read), None)
        self.check_for_error(error_code, samps_per_chan_read=samps_per_chan_read.value)
        return read_array, samps_per_chan_read.value

    def read_binary_i32(
            self, task, num_samps_per_chan, timeout, fill_mode, read_array):
        samps_per_chan_read = ctypes.c_int()

        c_func = lib_importer.windll.DAQmxReadBinaryI32
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int,
                        ctypes.c_double, ctypes.c_int,
                        wrapped_ndpointer(dtype=numpy.int32, flags=('C','W')),
                        ctypes.c_uint, ctypes.POINTER(ctypes.c_int),
                        ctypes.POINTER(c_bool32)]

        error_code = c_func(
            task, num_samps_per_chan, timeout, fill_mode, read_array,
            read_array.size, ctypes.byref(samps_per_chan_read), None)
        self.check_for_error(error_code, samps_per_chan_read=samps_per_chan_read.value)
        return read_array, samps_per_chan_read.value

    def read_binary_u16(
            self, task, num_samps_per_chan, timeout, fill_mode, read_array):
        samps_per_chan_read = ctypes.c_int()

        c_func = lib_importer.windll.DAQmxReadBinaryU16
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int,
                        ctypes.c_double, ctypes.c_int,
                        wrapped_ndpointer(dtype=numpy.uint16,
                        flags=('C','W')), ctypes.c_uint,
                        ctypes.POINTER(ctypes.c_int), ctypes.POINTER(c_bool32)]

        error_code = c_func(
            task, num_samps_per_chan, timeout, fill_mode, read_array,
            read_array.size, ctypes.byref(samps_per_chan_read), None)
        self.check_for_error(error_code, samps_per_chan_read=samps_per_chan_read.value)
        return read_array, samps_per_chan_read.value

    def read_binary_u32(
            self, task, num_samps_per_chan, timeout, fill_mode, read_array):
        samps_per_chan_read = ctypes.c_int()

        c_func = lib_importer.windll.DAQmxReadBinaryU32
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int,
                        ctypes.c_double, ctypes.c_int,
                        wrapped_ndpointer(dtype=numpy.uint32,
                        flags=('C','W')), ctypes.c_uint,
                        ctypes.POINTER(ctypes.c_int), ctypes.POINTER(c_bool32)]

        error_code = c_func(
            task, num_samps_per_chan, timeout, fill_mode, read_array,
            read_array.size, ctypes.byref(samps_per_chan_read), None)
        self.check_for_error(error_code, samps_per_chan_read=samps_per_chan_read.value)
        return read_array, samps_per_chan_read.value

    def read_counter_f64(self, task, num_samps_per_chan, timeout, read_array):
        samps_per_chan_read = ctypes.c_int()

        c_func = lib_importer.windll.DAQmxReadCounterF64
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int,
                        ctypes.c_double,
                        wrapped_ndpointer(dtype=numpy.float64,
                        flags=('C','W')), ctypes.c_uint,
                        ctypes.POINTER(ctypes.c_int), ctypes.POINTER(c_bool32)]

        error_code = c_func(
            task, num_samps_per_chan, timeout, read_array, read_array.size,
            ctypes.byref(samps_per_chan_read), None)
        self.check_for_error(error_code, samps_per_chan_read=samps_per_chan_read.value)
        return read_array, samps_per_chan_read.value

    def read_counter_f64_ex(
            self, task, num_samps_per_chan, timeout, fill_mode, read_array):
        samps_per_chan_read = ctypes.c_int()

        c_func = lib_importer.windll.DAQmxReadCounterF64Ex
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int,
                        ctypes.c_double, ctypes.c_int,
                        wrapped_ndpointer(dtype=numpy.float64,
                        flags=('C','W')), ctypes.c_uint,
                        ctypes.POINTER(ctypes.c_int), ctypes.POINTER(c_bool32)]

        error_code = c_func(
            task, num_samps_per_chan, timeout, fill_mode, read_array,
            read_array.size, ctypes.byref(samps_per_chan_read), None)
        self.check_for_error(error_code, samps_per_chan_read=samps_per_chan_read.value)
        return read_array, samps_per_chan_read.value

    def read_counter_scalar_f64(self, task, timeout):
        value = ctypes.c_double()

        c_func = lib_importer.windll.DAQmxReadCounterScalarF64
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_double,
                        ctypes.POINTER(ctypes.c_double),
                        ctypes.POINTER(c_bool32)]

        error_code = c_func(
            task, timeout, ctypes.byref(value), None)
        self.check_for_error(error_code)
        return value.value

    def read_counter_scalar_u32(self, task, timeout):
        value = ctypes.c_uint()

        c_func = lib_importer.windll.DAQmxReadCounterScalarU32
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_double,
                        ctypes.POINTER(ctypes.c_uint),
                        ctypes.POINTER(c_bool32)]

        error_code = c_func(
            task, timeout, ctypes.byref(value), None)
        self.check_for_error(error_code)
        return value.value

    def read_counter_u32(self, task, num_samps_per_chan, timeout, read_array):
        samps_per_chan_read = ctypes.c_int()

        c_func = lib_importer.windll.DAQmxReadCounterU32
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int,
                        ctypes.c_double, wrapped_ndpointer(dtype=numpy.uint32,
                        flags=('C','W')), ctypes.c_uint,
                        ctypes.POINTER(ctypes.c_int), ctypes.POINTER(c_bool32)]

        error_code = c_func(
            task, num_samps_per_chan, timeout, read_array, read_array.size,
            ctypes.byref(samps_per_chan_read), None)
        self.check_for_error(error_code, samps_per_chan_read=samps_per_chan_read.value)
        return read_array, samps_per_chan_read.value

    def read_counter_u32_ex(
            self, task, num_samps_per_chan, timeout, fill_mode, read_array):
        samps_per_chan_read = ctypes.c_int()

        c_func = lib_importer.windll.DAQmxReadCounterU32Ex
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int,
                        ctypes.c_double, ctypes.c_int,
                        wrapped_ndpointer(dtype=numpy.uint32,
                        flags=('C','W')), ctypes.c_uint,
                        ctypes.POINTER(ctypes.c_int), ctypes.POINTER(c_bool32)]

        error_code = c_func(
            task, num_samps_per_chan, timeout, fill_mode, read_array,
            read_array.size, ctypes.byref(samps_per_chan_read), None)
        self.check_for_error(error_code, samps_per_chan_read=samps_per_chan_read.value)
        return read_array, samps_per_chan_read.value

    def read_ctr_freq(
            self, task, num_samps_per_chan, timeout, interleaved,
            read_array_frequency, read_array_duty_cycle):
        samps_per_chan_read = ctypes.c_int()

        c_func = lib_importer.windll.DAQmxReadCtrFreq
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int,
                        ctypes.c_double, ctypes.c_int,
                        wrapped_ndpointer(dtype=numpy.float64,
                        flags=('C','W')),
                        wrapped_ndpointer(dtype=numpy.float64,
                        flags=('C','W')), ctypes.c_uint,
                        ctypes.POINTER(ctypes.c_int), ctypes.POINTER(c_bool32)]

        error_code = c_func(
            task, num_samps_per_chan, timeout, interleaved,
            read_array_frequency, read_array_duty_cycle,
            read_array_duty_cycle.size, ctypes.byref(samps_per_chan_read),
            None)
        self.check_for_error(error_code, samps_per_chan_read=samps_per_chan_read.value)
        return read_array_frequency, read_array_duty_cycle, samps_per_chan_read.value

    def read_ctr_freq_scalar(self, task, timeout):
        frequency = ctypes.c_double()
        duty_cycle = ctypes.c_double()

        c_func = lib_importer.windll.DAQmxReadCtrFreqScalar
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_double,
                        ctypes.POINTER(ctypes.c_double),
                        ctypes.POINTER(ctypes.c_double),
                        ctypes.POINTER(c_bool32)]

        error_code = c_func(
            task, timeout, ctypes.byref(frequency), ctypes.byref(duty_cycle),
            None)
        self.check_for_error(error_code)
        return frequency.value, duty_cycle.value

    def read_ctr_ticks(
            self, task, num_samps_per_chan, timeout, interleaved,
            read_array_high_ticks, read_array_low_ticks):
        samps_per_chan_read = ctypes.c_int()

        c_func = lib_importer.windll.DAQmxReadCtrTicks
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int,
                        ctypes.c_double, ctypes.c_int,
                        wrapped_ndpointer(dtype=numpy.uint32,
                        flags=('C','W')),
                        wrapped_ndpointer(dtype=numpy.uint32,
                        flags=('C','W')), ctypes.c_uint,
                        ctypes.POINTER(ctypes.c_int), ctypes.POINTER(c_bool32)]

        error_code = c_func(
            task, num_samps_per_chan, timeout, interleaved,
            read_array_high_ticks, read_array_low_ticks,
            read_array_low_ticks.size, ctypes.byref(samps_per_chan_read), None)
        self.check_for_error(error_code, samps_per_chan_read=samps_per_chan_read.value)
        return read_array_high_ticks, read_array_low_ticks, samps_per_chan_read.value

    def read_ctr_ticks_scalar(self, task, timeout):
        high_ticks = ctypes.c_uint32()
        low_ticks = ctypes.c_uint32()

        c_func = lib_importer.windll.DAQmxReadCtrTicksScalar
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_double,
                        ctypes.POINTER(ctypes.c_uint32),
                        ctypes.POINTER(ctypes.c_uint32),
                        ctypes.POINTER(c_bool32)]

        error_code = c_func(
            task, timeout, ctypes.byref(high_ticks), ctypes.byref(low_ticks),
            None)
        self.check_for_error(error_code)
        return high_ticks.value, low_ticks.value

    def read_ctr_time(
            self, task, num_samps_per_chan, timeout, interleaved,
            read_array_high_time, read_array_low_time):
        samps_per_chan_read = ctypes.c_int()

        c_func = lib_importer.windll.DAQmxReadCtrTime
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int,
                        ctypes.c_double, ctypes.c_int,
                        wrapped_ndpointer(dtype=numpy.float64,
                        flags=('C','W')),
                        wrapped_ndpointer(dtype=numpy.float64,
                        flags=('C','W')), ctypes.c_uint,
                        ctypes.POINTER(ctypes.c_int), ctypes.POINTER(c_bool32)]

        error_code = c_func(
            task, num_samps_per_chan, timeout, interleaved,
            read_array_high_time, read_array_low_time,
            read_array_low_time.size, ctypes.byref(samps_per_chan_read), None)
        self.check_for_error(error_code, samps_per_chan_read=samps_per_chan_read.value)
        return read_array_high_time, read_array_low_time, samps_per_chan_read.value

    def read_ctr_time_scalar(self, task, timeout):
        high_time = ctypes.c_double()
        low_time = ctypes.c_double()

        c_func = lib_importer.windll.DAQmxReadCtrTimeScalar
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_double,
                        ctypes.POINTER(ctypes.c_double),
                        ctypes.POINTER(ctypes.c_double),
                        ctypes.POINTER(c_bool32)]

        error_code = c_func(
            task, timeout, ctypes.byref(high_time), ctypes.byref(low_time),
            None)
        self.check_for_error(error_code)
        return high_time.value, low_time.value

    def read_digital_lines(
            self, task, num_samps_per_chan, timeout, fill_mode, read_array):
        samps_per_chan_read = ctypes.c_int()
        num_bytes_per_samp = ctypes.c_int()

        c_func = lib_importer.windll.DAQmxReadDigitalLines
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int,
                        ctypes.c_double, ctypes.c_int,
                        wrapped_ndpointer(dtype=bool, flags=('C','W')),
                        ctypes.c_uint, ctypes.POINTER(ctypes.c_int),
                        ctypes.POINTER(ctypes.c_int), ctypes.POINTER(c_bool32)]

        error_code = c_func(
            task, num_samps_per_chan, timeout, fill_mode, read_array,
            read_array.size, ctypes.byref(samps_per_chan_read),
            ctypes.byref(num_bytes_per_samp), None)
        self.check_for_error(error_code, samps_per_chan_read=samps_per_chan_read.value)
        return read_array, samps_per_chan_read.value, num_bytes_per_samp.value

    def read_digital_scalar_u32(self, task, timeout):
        value = ctypes.c_uint()

        c_func = lib_importer.windll.DAQmxReadDigitalScalarU32
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_double,
                        ctypes.POINTER(ctypes.c_uint),
                        ctypes.POINTER(c_bool32)]

        error_code = c_func(
            task, timeout, ctypes.byref(value), None)
        self.check_for_error(error_code)
        return value.value

    def read_digital_u16(
            self, task, num_samps_per_chan, timeout, fill_mode, read_array):
        samps_per_chan_read = ctypes.c_int()

        c_func = lib_importer.windll.DAQmxReadDigitalU16
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int,
                        ctypes.c_double, ctypes.c_int,
                        wrapped_ndpointer(dtype=numpy.uint16,
                        flags=('C','W')), ctypes.c_uint,
                        ctypes.POINTER(ctypes.c_int), ctypes.POINTER(c_bool32)]

        error_code = c_func(
            task, num_samps_per_chan, timeout, fill_mode, read_array,
            read_array.size, ctypes.byref(samps_per_chan_read), None)
        self.check_for_error(error_code, samps_per_chan_read=samps_per_chan_read.value)
        return read_array, samps_per_chan_read.value

    def read_digital_u32(
            self, task, num_samps_per_chan, timeout, fill_mode, read_array):
        samps_per_chan_read = ctypes.c_int()

        c_func = lib_importer.windll.DAQmxReadDigitalU32
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int,
                        ctypes.c_double, ctypes.c_int,
                        wrapped_ndpointer(dtype=numpy.uint32,
                        flags=('C','W')), ctypes.c_uint,
                        ctypes.POINTER(ctypes.c_int), ctypes.POINTER(c_bool32)]

        error_code = c_func(
            task, num_samps_per_chan, timeout, fill_mode, read_array,
            read_array.size, ctypes.byref(samps_per_chan_read), None)
        self.check_for_error(error_code, samps_per_chan_read=samps_per_chan_read.value)
        return read_array, samps_per_chan_read.value

    def read_digital_u8(
            self, task, num_samps_per_chan, timeout, fill_mode, read_array):
        samps_per_chan_read = ctypes.c_int()

        c_func = lib_importer.windll.DAQmxReadDigitalU8
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int,
                        ctypes.c_double, ctypes.c_int,
                        wrapped_ndpointer(dtype=numpy.uint8, flags=('C','W')),
                        ctypes.c_uint, ctypes.POINTER(ctypes.c_int),
                        ctypes.POINTER(c_bool32)]

        error_code = c_func(
            task, num_samps_per_chan, timeout, fill_mode, read_array,
            read_array.size, ctypes.byref(samps_per_chan_read), None)
        self.check_for_error(error_code, samps_per_chan_read=samps_per_chan_read.value)
        return read_array, samps_per_chan_read.value

    def read_power_scalar_f64(self, task, timeout):
        voltage = ctypes.c_double()
        current = ctypes.c_double()

        c_func = lib_importer.windll.DAQmxReadPowerScalarF64
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_double,
                        ctypes.POINTER(ctypes.c_double),
                        ctypes.POINTER(ctypes.c_double),
                        ctypes.POINTER(c_bool32)]

        error_code = c_func(
            task, timeout, ctypes.byref(voltage), ctypes.byref(current), None)
        self.check_for_error(error_code)
        return voltage.value, current.value

    def register_done_event(
            self, task, options, callback_function, callback_data):
        DAQmxDoneEventCallbackPtr = ctypes.CFUNCTYPE(
            ctypes.c_int32, lib_importer.task_handle, ctypes.c_int,
            ctypes.c_void_p)

        c_func = lib_importer.windll.DAQmxRegisterDoneEvent
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_uint,
                        DAQmxDoneEventCallbackPtr,
                        ctypes.POINTER(ctypes.c_void_p)]

        assert callback_function is not None
        callback_method_ptr = DAQmxDoneEventCallbackPtr(callback_function)

        error_code = c_func(
            task, options, callback_method_ptr, callback_data)
        self.check_for_error(error_code)

        return LibraryEventHandler(callback_method_ptr)

    def register_every_n_samples_event(
            self, task, every_n_samples_event_type, n_samples, options,
            callback_function, callback_data):
        DAQmxEveryNSamplesEventCallbackPtr = ctypes.CFUNCTYPE(
            ctypes.c_int32, lib_importer.task_handle, ctypes.c_int,
            ctypes.c_uint, ctypes.c_void_p)

        c_func = lib_importer.windll.DAQmxRegisterEveryNSamplesEvent
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int, ctypes.c_uint,
                        ctypes.c_uint, DAQmxEveryNSamplesEventCallbackPtr,
                        ctypes.POINTER(ctypes.c_void_p)]

        assert callback_function is not None
        callback_method_ptr = DAQmxEveryNSamplesEventCallbackPtr(callback_function)

        error_code = c_func(
            task, every_n_samples_event_type, n_samples, options,
            callback_method_ptr, callback_data)
        self.check_for_error(error_code)

        return LibraryEventHandler(callback_method_ptr)

    def register_signal_event(
            self, task, signal_id, options, callback_function, callback_data):
        DAQmxSignalEventCallbackPtr = ctypes.CFUNCTYPE(
            ctypes.c_int32, lib_importer.task_handle, ctypes.c_int,
            ctypes.c_void_p)

        c_func = lib_importer.windll.DAQmxRegisterSignalEvent
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int, ctypes.c_uint,
                        DAQmxSignalEventCallbackPtr,
                        ctypes.POINTER(ctypes.c_void_p)]

        assert callback_function is not None
        callback_method_ptr = DAQmxSignalEventCallbackPtr(callback_function)

        error_code = c_func(
            task, signal_id, options, callback_method_ptr, callback_data)
        self.check_for_error(error_code)

        return LibraryEventHandler(callback_method_ptr)

    def remove_cdaq_sync_connection(self, port_list):
        c_func = lib_importer.windll.DAQmxRemoveCDAQSyncConnection
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes_byte_str]

        error_code = c_func(
            port_list)
        self.check_for_error(error_code)

    def reserve_network_device(self, device_name, override_reservation):
        c_func = lib_importer.windll.DAQmxReserveNetworkDevice
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes_byte_str, c_bool32]

        error_code = c_func(
            device_name, override_reservation)
        self.check_for_error(error_code)

    def reset_buffer_attribute(self, task, attribute):
        c_func = lib_importer.windll.DAQmxResetBufferAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int32]

        error_code = c_func(
            task, attribute)
        self.check_for_error(error_code)

    def reset_chan_attribute(self, task, channel, attribute):
        c_func = lib_importer.windll.DAQmxResetChanAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int32]

        error_code = c_func(
            task, channel, attribute)
        self.check_for_error(error_code)

    def reset_device(self, device_name):
        c_func = lib_importer.windll.DAQmxResetDevice
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes_byte_str]

        error_code = c_func(
            device_name)
        self.check_for_error(error_code)

    def reset_exported_signal_attribute(self, task, attribute):
        c_func = lib_importer.windll.DAQmxResetExportedSignalAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int]

        error_code = c_func(
            task, attribute)
        self.check_for_error(error_code)

    def reset_read_attribute(self, task, attribute):
        c_func = lib_importer.windll.DAQmxResetReadAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int]

        error_code = c_func(
            task, attribute)
        self.check_for_error(error_code)

    def reset_timing_attribute(self, task, attribute):
        c_func = lib_importer.windll.DAQmxResetTimingAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int]

        error_code = c_func(
            task, attribute)
        self.check_for_error(error_code)

    def reset_timing_attribute_ex(self, task, device_names, attribute):
        c_func = lib_importer.windll.DAQmxResetTimingAttributeEx
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = c_func(
            task, device_names, attribute)
        self.check_for_error(error_code)

    def reset_trig_attribute(self, task, attribute):
        c_func = lib_importer.windll.DAQmxResetTrigAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int]

        error_code = c_func(
            task, attribute)
        self.check_for_error(error_code)

    def reset_watchdog_attribute(self, task, lines, attribute):
        c_func = lib_importer.windll.DAQmxResetWatchdogAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int]

        error_code = c_func(
            task, lines, attribute)
        self.check_for_error(error_code)

    def reset_write_attribute(self, task, attribute):
        c_func = lib_importer.windll.DAQmxResetWriteAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int]

        error_code = c_func(
            task, attribute)
        self.check_for_error(error_code)

    def restore_last_ext_cal_const(self, device_name):
        c_func = lib_importer.windll.DAQmxRestoreLastExtCalConst
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes_byte_str]

        error_code = c_func(
            device_name)
        self.check_for_error(error_code)

    def save_global_chan(self, task, channel_name, save_as, author, options):
        c_func = lib_importer.windll.DAQmxSaveGlobalChan
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes_byte_str, ctypes.c_uint32]

        error_code = c_func(
            task, channel_name, save_as, author, options)
        self.check_for_error(error_code)

    def save_scale(self, scale_name, save_as, author, options):
        c_func = lib_importer.windll.DAQmxSaveScale
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes_byte_str, ctypes_byte_str, ctypes_byte_str,
                        ctypes.c_uint32]

        error_code = c_func(
            scale_name, save_as, author, options)
        self.check_for_error(error_code)

    def save_task(self, task, save_as, author, options):
        c_func = lib_importer.windll.DAQmxSaveTask
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_uint32]

        error_code = c_func(
            task, save_as, author, options)
        self.check_for_error(error_code)

    def self_cal(self, device_name):
        c_func = lib_importer.windll.DAQmxSelfCal
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes_byte_str]

        error_code = c_func(
            device_name)
        self.check_for_error(error_code)

    def self_test_device(self, device_name):
        c_func = lib_importer.windll.DAQmxSelfTestDevice
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes_byte_str]

        error_code = c_func(
            device_name)
        self.check_for_error(error_code)

    def set_analog_power_up_states(
            self, device_name, channel_names, state, channel_type):
        args = [device_name]
        argtypes: list[type] = [ctypes_byte_str]

        for index in range(len(channel_names)):

            args.append(channel_names[index])
            argtypes.append(ctypes_byte_str)
            
            args.append(state[index])
            argtypes.append(ctypes.c_double)
            
            args.append(channel_type[index])
            argtypes.append(ctypes.c_int32)
            
        args.append(None)
        argtypes.append(ctypes.c_void_p)

        c_func = lib_importer.cdll.DAQmxSetAnalogPowerUpStates
        with c_func.arg_lock:
            c_func.argtypes = argtypes
            error_code = c_func(*args)
        self.check_for_error(error_code)

    def set_analog_power_up_states_with_output_type(
            self, channel_names, state_array, channel_type_array):
        c_func = lib_importer.cdll.DAQmxSetAnalogPowerUpStatesWithOutputType
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes_byte_str,
                        wrapped_ndpointer(dtype=numpy.float64, flags=('C')),
                        wrapped_ndpointer(dtype=numpy.int32, flags=('C')),
                        ctypes.c_uint]

        error_code = c_func(
            channel_names, state_array, channel_type_array,
            len(channel_type_array))
        self.check_for_error(error_code)

    def set_buffer_attribute_uint32(self, task, attribute, value):
        c_func = lib_importer.cdll.DAQmxSetBufferAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int32]

        error_code = c_func(
            task, attribute, ctypes.c_uint32(value))
        self.check_for_error(error_code)

    def set_cal_info_attribute_bool(self, device_name, attribute, value):
        c_func = lib_importer.cdll.DAQmxSetCalInfoAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes_byte_str, ctypes.c_int32]

        error_code = c_func(
            device_name, attribute, c_bool32(value))
        self.check_for_error(error_code)

    def set_cal_info_attribute_double(self, device_name, attribute, value):
        c_func = lib_importer.cdll.DAQmxSetCalInfoAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes_byte_str, ctypes.c_int32]

        error_code = c_func(
            device_name, attribute, ctypes.c_double(value))
        self.check_for_error(error_code)

    def set_cal_info_attribute_string(self, device_name, attribute, value):
        c_func = lib_importer.cdll.DAQmxSetCalInfoAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes_byte_str, ctypes.c_int32]

        error_code = c_func(
            device_name, attribute, value.encode(lib_importer.encoding))
        self.check_for_error(error_code)

    def set_cal_info_attribute_uint32(self, device_name, attribute, value):
        c_func = lib_importer.cdll.DAQmxSetCalInfoAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes_byte_str, ctypes.c_int32]

        error_code = c_func(
            device_name, attribute, ctypes.c_uint32(value))
        self.check_for_error(error_code)

    def set_chan_attribute_bool(self, task, channel, attribute, value):
        c_func = lib_importer.cdll.DAQmxSetChanAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int32]

        error_code = c_func(
            task, channel, attribute, c_bool32(value))
        self.check_for_error(error_code)

    def set_chan_attribute_double(self, task, channel, attribute, value):
        c_func = lib_importer.cdll.DAQmxSetChanAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int32]

        error_code = c_func(
            task, channel, attribute, ctypes.c_double(value))
        self.check_for_error(error_code)

    def set_chan_attribute_double_array(self, task, channel, attribute, value):
        c_func = lib_importer.cdll.DAQmxSetChanAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int32]

        error_code = c_func(
            task, channel, attribute, value.ctypes.data_as(ctypes.c_void_p),
            len(value))
        self.check_for_error(error_code)

    def set_chan_attribute_int32(self, task, channel, attribute, value):
        c_func = lib_importer.cdll.DAQmxSetChanAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int32]

        error_code = c_func(
            task, channel, attribute, ctypes.c_int32(value))
        self.check_for_error(error_code)

    def set_chan_attribute_string(self, task, channel, attribute, value):
        c_func = lib_importer.cdll.DAQmxSetChanAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int32]

        error_code = c_func(
            task, channel, attribute, value.encode(lib_importer.encoding))
        self.check_for_error(error_code)

    def set_chan_attribute_uint32(self, task, channel, attribute, value):
        c_func = lib_importer.cdll.DAQmxSetChanAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int32]

        error_code = c_func(
            task, channel, attribute, ctypes.c_uint32(value))
        self.check_for_error(error_code)

    def set_digital_logic_family_power_up_state(
            self, device_name, logic_family):
        c_func = lib_importer.windll.DAQmxSetDigitalLogicFamilyPowerUpState
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes_byte_str, ctypes.c_int]

        error_code = c_func(
            device_name, logic_family)
        self.check_for_error(error_code)

    def set_digital_power_up_states(self, device_name, channel_names, state):
        args = [device_name]
        argtypes: list[type] = [ctypes_byte_str]

        for index in range(len(channel_names)):

            args.append(channel_names[index])
            argtypes.append(ctypes_byte_str)
            
            args.append(state[index])
            argtypes.append(ctypes.c_int32)
            
        args.append(None)
        argtypes.append(ctypes.c_void_p)

        c_func = lib_importer.cdll.DAQmxSetDigitalPowerUpStates
        with c_func.arg_lock:
            c_func.argtypes = argtypes
            error_code = c_func(*args)
        self.check_for_error(error_code)

    def set_digital_pull_up_pull_down_states(
            self, device_name, channel_names, state):
        args = [device_name]
        argtypes: list[type] = [ctypes_byte_str]

        for index in range(len(channel_names)):

            args.append(channel_names[index])
            argtypes.append(ctypes_byte_str)
            
            args.append(state[index])
            argtypes.append(ctypes.c_int32)
            
        args.append(None)
        argtypes.append(ctypes.c_void_p)

        c_func = lib_importer.cdll.DAQmxSetDigitalPullUpPullDownStates
        with c_func.arg_lock:
            c_func.argtypes = argtypes
            error_code = c_func(*args)
        self.check_for_error(error_code)

    def set_exported_signal_attribute_bool(self, task, attribute, value):
        c_func = lib_importer.cdll.DAQmxSetExportedSignalAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int32]

        error_code = c_func(
            task, attribute, c_bool32(value))
        self.check_for_error(error_code)

    def set_exported_signal_attribute_double(self, task, attribute, value):
        c_func = lib_importer.cdll.DAQmxSetExportedSignalAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int32]

        error_code = c_func(
            task, attribute, ctypes.c_double(value))
        self.check_for_error(error_code)

    def set_exported_signal_attribute_int32(self, task, attribute, value):
        c_func = lib_importer.cdll.DAQmxSetExportedSignalAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int32]

        error_code = c_func(
            task, attribute, ctypes.c_int32(value))
        self.check_for_error(error_code)

    def set_exported_signal_attribute_string(self, task, attribute, value):
        c_func = lib_importer.cdll.DAQmxSetExportedSignalAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int32]

        error_code = c_func(
            task, attribute, value.encode(lib_importer.encoding))
        self.check_for_error(error_code)

    def set_exported_signal_attribute_uint32(self, task, attribute, value):
        c_func = lib_importer.cdll.DAQmxSetExportedSignalAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int32]

        error_code = c_func(
            task, attribute, ctypes.c_uint32(value))
        self.check_for_error(error_code)

    def set_read_attribute_bool(self, task, attribute, value):
        c_func = lib_importer.cdll.DAQmxSetReadAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int32]

        error_code = c_func(
            task, attribute, c_bool32(value))
        self.check_for_error(error_code)

    def set_read_attribute_double(self, task, attribute, value):
        c_func = lib_importer.cdll.DAQmxSetReadAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int32]

        error_code = c_func(
            task, attribute, ctypes.c_double(value))
        self.check_for_error(error_code)

    def set_read_attribute_int32(self, task, attribute, value):
        c_func = lib_importer.cdll.DAQmxSetReadAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int32]

        error_code = c_func(
            task, attribute, ctypes.c_int32(value))
        self.check_for_error(error_code)

    def set_read_attribute_string(self, task, attribute, value):
        c_func = lib_importer.cdll.DAQmxSetReadAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int32]

        error_code = c_func(
            task, attribute, value.encode(lib_importer.encoding))
        self.check_for_error(error_code)

    def set_read_attribute_uint32(self, task, attribute, value):
        c_func = lib_importer.cdll.DAQmxSetReadAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int32]

        error_code = c_func(
            task, attribute, ctypes.c_uint32(value))
        self.check_for_error(error_code)

    def set_read_attribute_uint64(self, task, attribute, value):
        c_func = lib_importer.cdll.DAQmxSetReadAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int32]

        error_code = c_func(
            task, attribute, ctypes.c_uint64(value))
        self.check_for_error(error_code)

    def set_runtime_environment(
            self, environment, environment_version, reserved_1, reserved_2):
        c_func = lib_importer.windll.DAQmxSetRuntimeEnvironment
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes_byte_str, ctypes_byte_str, ctypes_byte_str,
                        ctypes_byte_str]

        error_code = c_func(
            environment, environment_version, reserved_1, reserved_2)
        self.check_for_error(error_code)

    def set_scale_attribute_double(self, scale_name, attribute, value):
        c_func = lib_importer.cdll.DAQmxSetScaleAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes_byte_str, ctypes.c_int32]

        error_code = c_func(
            scale_name, attribute, ctypes.c_double(value))
        self.check_for_error(error_code)

    def set_scale_attribute_double_array(self, scale_name, attribute, value):
        c_func = lib_importer.cdll.DAQmxSetScaleAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes_byte_str, ctypes.c_int32]

        error_code = c_func(
            scale_name, attribute, value.ctypes.data_as(ctypes.c_void_p),
            len(value))
        self.check_for_error(error_code)

    def set_scale_attribute_int32(self, scale_name, attribute, value):
        c_func = lib_importer.cdll.DAQmxSetScaleAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes_byte_str, ctypes.c_int32]

        error_code = c_func(
            scale_name, attribute, ctypes.c_int32(value))
        self.check_for_error(error_code)

    def set_scale_attribute_string(self, scale_name, attribute, value):
        c_func = lib_importer.cdll.DAQmxSetScaleAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes_byte_str, ctypes.c_int32]

        error_code = c_func(
            scale_name, attribute, value.encode(lib_importer.encoding))
        self.check_for_error(error_code)

    def set_timing_attribute_bool(self, task, attribute, value):
        c_func = lib_importer.cdll.DAQmxSetTimingAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int32]

        error_code = c_func(
            task, attribute, c_bool32(value))
        self.check_for_error(error_code)

    def set_timing_attribute_double(self, task, attribute, value):
        c_func = lib_importer.cdll.DAQmxSetTimingAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int32]

        error_code = c_func(
            task, attribute, ctypes.c_double(value))
        self.check_for_error(error_code)

    def set_timing_attribute_ex_bool(
            self, task, device_names, attribute, value):
        c_func = lib_importer.cdll.DAQmxSetTimingAttributeEx
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int32]

        error_code = c_func(
            task, device_names, attribute, c_bool32(value))
        self.check_for_error(error_code)

    def set_timing_attribute_ex_double(
            self, task, device_names, attribute, value):
        c_func = lib_importer.cdll.DAQmxSetTimingAttributeEx
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int32]

        error_code = c_func(
            task, device_names, attribute, ctypes.c_double(value))
        self.check_for_error(error_code)

    def set_timing_attribute_ex_int32(
            self, task, device_names, attribute, value):
        c_func = lib_importer.cdll.DAQmxSetTimingAttributeEx
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int32]

        error_code = c_func(
            task, device_names, attribute, ctypes.c_int32(value))
        self.check_for_error(error_code)

    def set_timing_attribute_ex_string(
            self, task, device_names, attribute, value):
        c_func = lib_importer.cdll.DAQmxSetTimingAttributeEx
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int32]

        error_code = c_func(
            task, device_names, attribute, value.encode(lib_importer.encoding))
        self.check_for_error(error_code)

    def set_timing_attribute_ex_uint32(
            self, task, device_names, attribute, value):
        c_func = lib_importer.cdll.DAQmxSetTimingAttributeEx
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int32]

        error_code = c_func(
            task, device_names, attribute, ctypes.c_uint32(value))
        self.check_for_error(error_code)

    def set_timing_attribute_ex_uint64(
            self, task, device_names, attribute, value):
        c_func = lib_importer.cdll.DAQmxSetTimingAttributeEx
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int32]

        error_code = c_func(
            task, device_names, attribute, ctypes.c_uint64(value))
        self.check_for_error(error_code)

    def set_timing_attribute_int32(self, task, attribute, value):
        c_func = lib_importer.cdll.DAQmxSetTimingAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int32]

        error_code = c_func(
            task, attribute, ctypes.c_int32(value))
        self.check_for_error(error_code)

    def set_timing_attribute_string(self, task, attribute, value):
        c_func = lib_importer.cdll.DAQmxSetTimingAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int32]

        error_code = c_func(
            task, attribute, value.encode(lib_importer.encoding))
        self.check_for_error(error_code)

    def set_timing_attribute_uint32(self, task, attribute, value):
        c_func = lib_importer.cdll.DAQmxSetTimingAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int32]

        error_code = c_func(
            task, attribute, ctypes.c_uint32(value))
        self.check_for_error(error_code)

    def set_timing_attribute_uint64(self, task, attribute, value):
        c_func = lib_importer.cdll.DAQmxSetTimingAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int32]

        error_code = c_func(
            task, attribute, ctypes.c_uint64(value))
        self.check_for_error(error_code)

    def set_trig_attribute_bool(self, task, attribute, value):
        c_func = lib_importer.cdll.DAQmxSetTrigAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int32]

        error_code = c_func(
            task, attribute, c_bool32(value))
        self.check_for_error(error_code)

    def set_trig_attribute_double(self, task, attribute, value):
        c_func = lib_importer.cdll.DAQmxSetTrigAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int32]

        error_code = c_func(
            task, attribute, ctypes.c_double(value))
        self.check_for_error(error_code)

    def set_trig_attribute_double_array(self, task, attribute, value):
        c_func = lib_importer.cdll.DAQmxSetTrigAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int32]

        error_code = c_func(
            task, attribute, value.ctypes.data_as(ctypes.c_void_p), len(value))
        self.check_for_error(error_code)

    def set_trig_attribute_int32(self, task, attribute, value):
        c_func = lib_importer.cdll.DAQmxSetTrigAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int32]

        error_code = c_func(
            task, attribute, ctypes.c_int32(value))
        self.check_for_error(error_code)

    def set_trig_attribute_int32_array(self, task, attribute, value):
        c_func = lib_importer.cdll.DAQmxSetTrigAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int32]

        error_code = c_func(
            task, attribute, value.ctypes.data_as(ctypes.c_void_p), len(value))
        self.check_for_error(error_code)

    def set_trig_attribute_string(self, task, attribute, value):
        c_func = lib_importer.cdll.DAQmxSetTrigAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int32]

        error_code = c_func(
            task, attribute, value.encode(lib_importer.encoding))
        self.check_for_error(error_code)

    def set_trig_attribute_timestamp(self, task, attribute, value):
        c_func = lib_importer.cdll.DAQmxSetTrigAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int32]

        error_code = c_func(
            task, attribute, AbsoluteTime.from_datetime(value))
        self.check_for_error(error_code)

    def set_trig_attribute_uint32(self, task, attribute, value):
        c_func = lib_importer.cdll.DAQmxSetTrigAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int32]

        error_code = c_func(
            task, attribute, ctypes.c_uint32(value))
        self.check_for_error(error_code)

    def set_watchdog_attribute_bool(self, task, lines, attribute, value):
        c_func = lib_importer.cdll.DAQmxSetWatchdogAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int32]

        error_code = c_func(
            task, lines, attribute, c_bool32(value))
        self.check_for_error(error_code)

    def set_watchdog_attribute_double(self, task, lines, attribute, value):
        c_func = lib_importer.cdll.DAQmxSetWatchdogAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int32]

        error_code = c_func(
            task, lines, attribute, ctypes.c_double(value))
        self.check_for_error(error_code)

    def set_watchdog_attribute_int32(self, task, lines, attribute, value):
        c_func = lib_importer.cdll.DAQmxSetWatchdogAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int32]

        error_code = c_func(
            task, lines, attribute, ctypes.c_int32(value))
        self.check_for_error(error_code)

    def set_watchdog_attribute_string(self, task, lines, attribute, value):
        c_func = lib_importer.cdll.DAQmxSetWatchdogAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int32]

        error_code = c_func(
            task, lines, attribute, value.encode(lib_importer.encoding))
        self.check_for_error(error_code)

    def set_write_attribute_bool(self, task, attribute, value):
        c_func = lib_importer.cdll.DAQmxSetWriteAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int32]

        error_code = c_func(
            task, attribute, c_bool32(value))
        self.check_for_error(error_code)

    def set_write_attribute_double(self, task, attribute, value):
        c_func = lib_importer.cdll.DAQmxSetWriteAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int32]

        error_code = c_func(
            task, attribute, ctypes.c_double(value))
        self.check_for_error(error_code)

    def set_write_attribute_int32(self, task, attribute, value):
        c_func = lib_importer.cdll.DAQmxSetWriteAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int32]

        error_code = c_func(
            task, attribute, ctypes.c_int32(value))
        self.check_for_error(error_code)

    def set_write_attribute_string(self, task, attribute, value):
        c_func = lib_importer.cdll.DAQmxSetWriteAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int32]

        error_code = c_func(
            task, attribute, value.encode(lib_importer.encoding))
        self.check_for_error(error_code)

    def set_write_attribute_uint32(self, task, attribute, value):
        c_func = lib_importer.cdll.DAQmxSetWriteAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int32]

        error_code = c_func(
            task, attribute, ctypes.c_uint32(value))
        self.check_for_error(error_code)

    def set_write_attribute_uint64(self, task, attribute, value):
        c_func = lib_importer.cdll.DAQmxSetWriteAttribute
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int32]

        error_code = c_func(
            task, attribute, ctypes.c_uint64(value))
        self.check_for_error(error_code)

    def start_new_file(self, task, file_path):
        c_func = lib_importer.windll.DAQmxStartNewFile
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = c_func(
            task, file_path)
        self.check_for_error(error_code)

    def start_task(self, task):
        c_func = lib_importer.windll.DAQmxStartTask
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle]

        error_code = c_func(
            task)
        self.check_for_error(error_code)

    def stop_task(self, task):
        c_func = lib_importer.windll.DAQmxStopTask
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle]

        error_code = c_func(
            task)
        self.check_for_error(error_code)

    def task_control(self, task, action):
        c_func = lib_importer.windll.DAQmxTaskControl
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int]

        error_code = c_func(
            task, action)
        self.check_for_error(error_code)

    def tristate_output_term(self, output_terminal):
        c_func = lib_importer.windll.DAQmxTristateOutputTerm
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes_byte_str]

        error_code = c_func(
            output_terminal)
        self.check_for_error(error_code)

    def unregister_done_event(self, task):
        DAQmxDoneEventCallbackPtr = ctypes.CFUNCTYPE(
            ctypes.c_int32, lib_importer.task_handle, ctypes.c_int,
            ctypes.c_void_p)

        c_func = lib_importer.windll.DAQmxRegisterDoneEvent
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_uint,
                        DAQmxDoneEventCallbackPtr,
                        ctypes.POINTER(ctypes.c_void_p)]

        options = 0
        callback_method_ptr = DAQmxDoneEventCallbackPtr()
        callback_data = None

        error_code = c_func(
            task, options, callback_method_ptr, callback_data)
        self.check_for_error(error_code)

    def unregister_every_n_samples_event(
            self, task, every_n_samples_event_type):
        DAQmxEveryNSamplesEventCallbackPtr = ctypes.CFUNCTYPE(
            ctypes.c_int32, lib_importer.task_handle, ctypes.c_int,
            ctypes.c_uint, ctypes.c_void_p)

        c_func = lib_importer.windll.DAQmxRegisterEveryNSamplesEvent
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int, ctypes.c_uint,
                        ctypes.c_uint, DAQmxEveryNSamplesEventCallbackPtr,
                        ctypes.POINTER(ctypes.c_void_p)]

        n_samples = 0
        options = 0
        callback_method_ptr = DAQmxEveryNSamplesEventCallbackPtr()
        callback_data = None

        error_code = c_func(
            task, every_n_samples_event_type, n_samples, options,
            callback_method_ptr, callback_data)
        self.check_for_error(error_code)

    def unregister_signal_event(self, task, signal_id):
        DAQmxSignalEventCallbackPtr = ctypes.CFUNCTYPE(
            ctypes.c_int32, lib_importer.task_handle, ctypes.c_int,
            ctypes.c_void_p)

        c_func = lib_importer.windll.DAQmxRegisterSignalEvent
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int, ctypes.c_uint,
                        DAQmxSignalEventCallbackPtr,
                        ctypes.POINTER(ctypes.c_void_p)]

        options = 0
        callback_method_ptr = DAQmxSignalEventCallbackPtr()
        callback_data = None

        error_code = c_func(
            task, signal_id, options, callback_method_ptr, callback_data)
        self.check_for_error(error_code)

    def unreserve_network_device(self, device_name):
        c_func = lib_importer.windll.DAQmxUnreserveNetworkDevice
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes_byte_str]

        error_code = c_func(
            device_name)
        self.check_for_error(error_code)

    def wait_for_valid_timestamp(self, task, timestamp_event, timeout):
        timestamp = AbsoluteTime()

        c_func = lib_importer.windll.DAQmxWaitForValidTimestamp
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int32,
                        ctypes.c_double, ctypes.POINTER(AbsoluteTime)]

        error_code = c_func(
            task, timestamp_event, timeout, ctypes.byref(timestamp))
        self.check_for_error(error_code)
        return timestamp.to_datetime()

    def wait_until_task_done(self, task, time_to_wait):
        c_func = lib_importer.windll.DAQmxWaitUntilTaskDone
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_double]

        error_code = c_func(
            task, time_to_wait)
        self.check_for_error(error_code)

    def write_analog_f64(
            self, task, num_samps_per_chan, auto_start, timeout, data_layout,
            write_array):
        samps_per_chan_written = ctypes.c_int()

        c_func = lib_importer.windll.DAQmxWriteAnalogF64
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int, c_bool32,
                        ctypes.c_double, ctypes.c_int,
                        wrapped_ndpointer(dtype=numpy.float64, flags=('C')),
                        ctypes.POINTER(ctypes.c_int), ctypes.POINTER(c_bool32)]

        error_code = c_func(
            task, num_samps_per_chan, auto_start, timeout, data_layout,
            write_array, ctypes.byref(samps_per_chan_written), None)
        self.check_for_error(error_code, samps_per_chan_written=samps_per_chan_written.value)
        return samps_per_chan_written.value

    def write_analog_scalar_f64(self, task, auto_start, timeout, value):
        c_func = lib_importer.windll.DAQmxWriteAnalogScalarF64
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, c_bool32, ctypes.c_double,
                        ctypes.c_double, ctypes.POINTER(c_bool32)]

        error_code = c_func(
            task, auto_start, timeout, value, None)
        self.check_for_error(error_code)

    def write_binary_i16(
            self, task, num_samps_per_chan, auto_start, timeout, data_layout,
            write_array):
        samps_per_chan_written = ctypes.c_int()

        c_func = lib_importer.windll.DAQmxWriteBinaryI16
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int, c_bool32,
                        ctypes.c_double, ctypes.c_int,
                        wrapped_ndpointer(dtype=numpy.int16, flags=('C')),
                        ctypes.POINTER(ctypes.c_int), ctypes.POINTER(c_bool32)]

        error_code = c_func(
            task, num_samps_per_chan, auto_start, timeout, data_layout,
            write_array, ctypes.byref(samps_per_chan_written), None)
        self.check_for_error(error_code, samps_per_chan_written=samps_per_chan_written.value)
        return samps_per_chan_written.value

    def write_binary_i32(
            self, task, num_samps_per_chan, auto_start, timeout, data_layout,
            write_array):
        samps_per_chan_written = ctypes.c_int()

        c_func = lib_importer.windll.DAQmxWriteBinaryI32
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int, c_bool32,
                        ctypes.c_double, ctypes.c_int,
                        wrapped_ndpointer(dtype=numpy.int32, flags=('C')),
                        ctypes.POINTER(ctypes.c_int), ctypes.POINTER(c_bool32)]

        error_code = c_func(
            task, num_samps_per_chan, auto_start, timeout, data_layout,
            write_array, ctypes.byref(samps_per_chan_written), None)
        self.check_for_error(error_code, samps_per_chan_written=samps_per_chan_written.value)
        return samps_per_chan_written.value

    def write_binary_u16(
            self, task, num_samps_per_chan, auto_start, timeout, data_layout,
            write_array):
        samps_per_chan_written = ctypes.c_int()

        c_func = lib_importer.windll.DAQmxWriteBinaryU16
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int, c_bool32,
                        ctypes.c_double, ctypes.c_int,
                        wrapped_ndpointer(dtype=numpy.uint16, flags=('C')),
                        ctypes.POINTER(ctypes.c_int), ctypes.POINTER(c_bool32)]

        error_code = c_func(
            task, num_samps_per_chan, auto_start, timeout, data_layout,
            write_array, ctypes.byref(samps_per_chan_written), None)
        self.check_for_error(error_code, samps_per_chan_written=samps_per_chan_written.value)
        return samps_per_chan_written.value

    def write_binary_u32(
            self, task, num_samps_per_chan, auto_start, timeout, data_layout,
            write_array):
        samps_per_chan_written = ctypes.c_int()

        c_func = lib_importer.windll.DAQmxWriteBinaryU32
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int, c_bool32,
                        ctypes.c_double, ctypes.c_int,
                        wrapped_ndpointer(dtype=numpy.uint32, flags=('C')),
                        ctypes.POINTER(ctypes.c_int), ctypes.POINTER(c_bool32)]

        error_code = c_func(
            task, num_samps_per_chan, auto_start, timeout, data_layout,
            write_array, ctypes.byref(samps_per_chan_written), None)
        self.check_for_error(error_code, samps_per_chan_written=samps_per_chan_written.value)
        return samps_per_chan_written.value

    def write_ctr_freq(
            self, task, num_samps_per_chan, auto_start, timeout, data_layout,
            frequency, duty_cycle):
        num_samps_per_chan_written = ctypes.c_int()

        c_func = lib_importer.windll.DAQmxWriteCtrFreq
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int, c_bool32,
                        ctypes.c_double, ctypes.c_int,
                        wrapped_ndpointer(dtype=numpy.float64, flags=('C')),
                        wrapped_ndpointer(dtype=numpy.float64, flags=('C')),
                        ctypes.POINTER(ctypes.c_int), ctypes.POINTER(c_bool32)]

        error_code = c_func(
            task, num_samps_per_chan, auto_start, timeout, data_layout,
            frequency, duty_cycle, ctypes.byref(num_samps_per_chan_written),
            None)
        self.check_for_error(error_code, samps_per_chan_written=num_samps_per_chan_written.value)
        return num_samps_per_chan_written.value

    def write_ctr_freq_scalar(
            self, task, auto_start, timeout, frequency, duty_cycle):
        c_func = lib_importer.windll.DAQmxWriteCtrFreqScalar
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, c_bool32, ctypes.c_double,
                        ctypes.c_double, ctypes.c_double,
                        ctypes.POINTER(c_bool32)]

        error_code = c_func(
            task, auto_start, timeout, frequency, duty_cycle, None)
        self.check_for_error(error_code)

    def write_ctr_ticks(
            self, task, num_samps_per_chan, auto_start, timeout, data_layout,
            high_ticks, low_ticks):
        num_samps_per_chan_written = ctypes.c_int()

        c_func = lib_importer.windll.DAQmxWriteCtrTicks
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int, c_bool32,
                        ctypes.c_double, ctypes.c_int,
                        wrapped_ndpointer(dtype=numpy.uint32, flags=('C')),
                        wrapped_ndpointer(dtype=numpy.uint32, flags=('C')),
                        ctypes.POINTER(ctypes.c_int), ctypes.POINTER(c_bool32)]

        error_code = c_func(
            task, num_samps_per_chan, auto_start, timeout, data_layout,
            high_ticks, low_ticks, ctypes.byref(num_samps_per_chan_written),
            None)
        self.check_for_error(error_code, samps_per_chan_written=num_samps_per_chan_written.value)
        return num_samps_per_chan_written.value

    def write_ctr_ticks_scalar(
            self, task, auto_start, timeout, high_ticks, low_ticks):
        c_func = lib_importer.windll.DAQmxWriteCtrTicksScalar
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, c_bool32, ctypes.c_double,
                        ctypes.c_uint32, ctypes.c_uint32,
                        ctypes.POINTER(c_bool32)]

        error_code = c_func(
            task, auto_start, timeout, high_ticks, low_ticks, None)
        self.check_for_error(error_code)

    def write_ctr_time(
            self, task, num_samps_per_chan, auto_start, timeout, data_layout,
            high_time, low_time):
        num_samps_per_chan_written = ctypes.c_int()

        c_func = lib_importer.windll.DAQmxWriteCtrTime
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int, c_bool32,
                        ctypes.c_double, ctypes.c_int,
                        wrapped_ndpointer(dtype=numpy.float64, flags=('C')),
                        wrapped_ndpointer(dtype=numpy.float64, flags=('C')),
                        ctypes.POINTER(ctypes.c_int), ctypes.POINTER(c_bool32)]

        error_code = c_func(
            task, num_samps_per_chan, auto_start, timeout, data_layout,
            high_time, low_time, ctypes.byref(num_samps_per_chan_written),
            None)
        self.check_for_error(error_code, samps_per_chan_written=num_samps_per_chan_written.value)
        return num_samps_per_chan_written.value

    def write_ctr_time_scalar(
            self, task, auto_start, timeout, high_time, low_time):
        c_func = lib_importer.windll.DAQmxWriteCtrTimeScalar
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, c_bool32, ctypes.c_double,
                        ctypes.c_double, ctypes.c_double,
                        ctypes.POINTER(c_bool32)]

        error_code = c_func(
            task, auto_start, timeout, high_time, low_time, None)
        self.check_for_error(error_code)

    def write_digital_lines(
            self, task, num_samps_per_chan, auto_start, timeout, data_layout,
            write_array):
        samps_per_chan_written = ctypes.c_int()

        c_func = lib_importer.windll.DAQmxWriteDigitalLines
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int, c_bool32,
                        ctypes.c_double, ctypes.c_int,
                        wrapped_ndpointer(dtype=bool, flags=('C')),
                        ctypes.POINTER(ctypes.c_int), ctypes.POINTER(c_bool32)]

        error_code = c_func(
            task, num_samps_per_chan, auto_start, timeout, data_layout,
            write_array, ctypes.byref(samps_per_chan_written), None)
        self.check_for_error(error_code, samps_per_chan_written=samps_per_chan_written.value)
        return samps_per_chan_written.value

    def write_digital_scalar_u32(self, task, auto_start, timeout, value):
        c_func = lib_importer.windll.DAQmxWriteDigitalScalarU32
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, c_bool32, ctypes.c_double,
                        ctypes.c_uint, ctypes.POINTER(c_bool32)]

        error_code = c_func(
            task, auto_start, timeout, value, None)
        self.check_for_error(error_code)

    def write_digital_u16(
            self, task, num_samps_per_chan, auto_start, timeout, data_layout,
            write_array):
        samps_per_chan_written = ctypes.c_int()

        c_func = lib_importer.windll.DAQmxWriteDigitalU16
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int, c_bool32,
                        ctypes.c_double, ctypes.c_int,
                        wrapped_ndpointer(dtype=numpy.uint16, flags=('C')),
                        ctypes.POINTER(ctypes.c_int), ctypes.POINTER(c_bool32)]

        error_code = c_func(
            task, num_samps_per_chan, auto_start, timeout, data_layout,
            write_array, ctypes.byref(samps_per_chan_written), None)
        self.check_for_error(error_code, samps_per_chan_written=samps_per_chan_written.value)
        return samps_per_chan_written.value

    def write_digital_u32(
            self, task, num_samps_per_chan, auto_start, timeout, data_layout,
            write_array):
        samps_per_chan_written = ctypes.c_int()

        c_func = lib_importer.windll.DAQmxWriteDigitalU32
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int, c_bool32,
                        ctypes.c_double, ctypes.c_int,
                        wrapped_ndpointer(dtype=numpy.uint32, flags=('C')),
                        ctypes.POINTER(ctypes.c_int), ctypes.POINTER(c_bool32)]

        error_code = c_func(
            task, num_samps_per_chan, auto_start, timeout, data_layout,
            write_array, ctypes.byref(samps_per_chan_written), None)
        self.check_for_error(error_code, samps_per_chan_written=samps_per_chan_written.value)
        return samps_per_chan_written.value

    def write_digital_u8(
            self, task, num_samps_per_chan, auto_start, timeout, data_layout,
            write_array):
        samps_per_chan_written = ctypes.c_int()

        c_func = lib_importer.windll.DAQmxWriteDigitalU8
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int, c_bool32,
                        ctypes.c_double, ctypes.c_int,
                        wrapped_ndpointer(dtype=numpy.uint8, flags=('C')),
                        ctypes.POINTER(ctypes.c_int), ctypes.POINTER(c_bool32)]

        error_code = c_func(
            task, num_samps_per_chan, auto_start, timeout, data_layout,
            write_array, ctypes.byref(samps_per_chan_written), None)
        self.check_for_error(error_code, samps_per_chan_written=samps_per_chan_written.value)
        return samps_per_chan_written.value

    def write_id_pin_memory(self, device_name, id_pin_name, data, format_code):
        c_func = lib_importer.windll.DAQmxWriteIDPinMemory
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes_byte_str, ctypes_byte_str,
                        wrapped_ndpointer(dtype=numpy.uint8, flags=('C')),
                        ctypes.c_uint, ctypes.c_uint]

        error_code = c_func(
            device_name, id_pin_name, data, len(data), format_code)
        self.check_for_error(error_code)

    def write_to_teds_from_array(
            self, physical_channel, bit_stream, basic_teds_options):
        c_func = lib_importer.windll.DAQmxWriteToTEDSFromArray
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes_byte_str, wrapped_ndpointer(dtype=numpy.uint8,
                        flags=('C')), ctypes.c_uint, ctypes.c_int]

        error_code = c_func(
            physical_channel, bit_stream, len(bit_stream), basic_teds_options)
        self.check_for_error(error_code)

    def write_to_teds_from_file(
            self, physical_channel, file_path, basic_teds_options):
        c_func = lib_importer.windll.DAQmxWriteToTEDSFromFile
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes_byte_str, ctypes_byte_str, ctypes.c_int]

        error_code = c_func(
            physical_channel, file_path, basic_teds_options)
        self.check_for_error(error_code)

    def get_error_string(self, error_code):
        error_buffer = ctypes.create_string_buffer(2048)

        c_func = lib_importer.windll.DAQmxGetErrorString
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [ctypes.c_int, ctypes.c_char_p,
                                      ctypes.c_uint]

        query_error_code = c_func(error_code, error_buffer, 2048)
        if query_error_code < 0:
            _logger.error('Failed to get error string for error code %d. DAQmxGetErrorString returned error code %d.', error_code, query_error_code)
            return 'Failed to retrieve error description.'
        return error_buffer.value.decode(lib_importer.encoding)

    def get_extended_error_info(self):
        error_buffer = ctypes.create_string_buffer(2048)

        c_func = lib_importer.windll.DAQmxGetExtendedErrorInfo
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [ctypes.c_char_p, ctypes.c_uint]

        query_error_code = c_func(error_buffer, 2048)
        if query_error_code < 0:
            _logger.error('Failed to get extended error info. DAQmxGetExtendedErrorInfo returned error code %d.', query_error_code)
            return 'Failed to retrieve error description.'
        return error_buffer.value.decode(lib_importer.encoding)

    def read_analog_waveform(
        self,
        task_handle: object,
        number_of_samples_per_channel: int,
        timeout: float,
        waveform: AnalogWaveform[numpy.float64],
        waveform_attribute_mode: WaveformAttributeMode
    ) -> int:
        """Read an analog waveform with timing and attributes."""
        if WaveformAttributeMode.EXTENDED_PROPERTIES in waveform_attribute_mode:
            properties = [waveform.extended_properties]
        else:
            properties = None

        if WaveformAttributeMode.TIMING in waveform_attribute_mode:
            t0_array = numpy.zeros(1, dtype=numpy.int64)
            dt_array = numpy.zeros(1, dtype=numpy.int64)
        else:
            t0_array = None
            dt_array = None

        waveform.sample_count = number_of_samples_per_channel

        error_code, samples_read = self._internal_read_analog_waveform_ex(
            task_handle,
            number_of_samples_per_channel,
            timeout,
            FillMode.GROUP_BY_CHANNEL.value,
            waveform.raw_data,
            properties,
            t0_array,
            dt_array,
        )

        waveform.sample_count = samples_read

        if t0_array is not None and dt_array is not None:
            self._set_waveform_timings([waveform], t0_array, dt_array)

        self.check_for_error(error_code, samps_per_chan_read=samples_read)
        return samples_read

    def read_analog_waveforms(
        self,
        task_handle: object,
        number_of_samples_per_channel: int,
        timeout: float,
        waveforms: Sequence[AnalogWaveform[numpy.float64]],
        waveform_attribute_mode: WaveformAttributeMode
    ) -> int:
        """Read a set of analog waveforms with timing and attributes. All of the waveforms must be the same size."""
        if WaveformAttributeMode.EXTENDED_PROPERTIES in waveform_attribute_mode:
            properties = [waveform.extended_properties for waveform in waveforms]
        else:
            properties = None

        if WaveformAttributeMode.TIMING in waveform_attribute_mode:
            t0_array = numpy.zeros(len(waveforms), dtype=numpy.int64)
            dt_array = numpy.zeros(len(waveforms), dtype=numpy.int64)
        else:
            t0_array = None
            dt_array = None

        for waveform in waveforms:
            waveform.sample_count = number_of_samples_per_channel

        error_code, samples_read = self._internal_read_analog_waveform_per_chan(
            task_handle,
            number_of_samples_per_channel,
            timeout,
            [waveform.raw_data for waveform in waveforms],
            properties,
            t0_array,
            dt_array,
        )

        for waveform in waveforms:
            waveform.sample_count = samples_read
            
        if t0_array is not None and dt_array is not None:
            self._set_waveform_timings(waveforms, t0_array, dt_array)

        self.check_for_error(error_code, samps_per_chan_read=samples_read)
        return samples_read

    def _internal_read_analog_waveform_ex(
        self,
        task_handle: object,
        number_of_samples_per_channel: int,
        timeout: float,
        fill_mode: int,
        read_array: numpy.typing.NDArray[numpy.float64],
        properties: Sequence[ExtendedPropertyDictionary] | None,
        t0_array: numpy.typing.NDArray[numpy.int64] | None,
        dt_array: numpy.typing.NDArray[numpy.int64] | None,
    ) -> tuple[
        int, # error code
        int, # The number of samples per channel that were read
    ]:
        assert isinstance(task_handle, TaskHandle)
        samps_per_chan_read = ctypes.c_int()

        c_func = lib_importer.windll.DAQmxInternalReadAnalogWaveformEx
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        TaskHandle,
                        ctypes.c_int,
                        ctypes.c_double,
                        ctypes.c_int,
                        wrapped_ndpointer(dtype=numpy.int64, flags=("C", "W")),
                        wrapped_ndpointer(dtype=numpy.int64, flags=("C", "W")),
                        ctypes.c_uint,
                        CSetWfmAttrCallbackPtr,
                        ctypes.c_void_p,
                        wrapped_ndpointer(dtype=numpy.float64, flags=("C", "W")),
                        ctypes.c_uint,
                        ctypes.POINTER(ctypes.c_int),
                        ctypes.POINTER(c_bool32),
                    ]

        error_code = c_func(
            task_handle,
            number_of_samples_per_channel,
            timeout,
            fill_mode,
            t0_array,
            dt_array,
            0 if t0_array is None else t0_array.size,
            self._get_wfm_attr_callback(properties),
            None,
            read_array,
            read_array.size,
            ctypes.byref(samps_per_chan_read),
            None,
        )

        return error_code, samps_per_chan_read.value

    def _internal_read_analog_waveform_per_chan(
        self,
        task_handle: object,
        num_samps_per_chan: int,
        timeout: float,
        read_arrays: Sequence[numpy.typing.NDArray[numpy.float64]],
        properties: Sequence[ExtendedPropertyDictionary] | None,
        t0_array: numpy.typing.NDArray[numpy.int64] | None,
        dt_array: numpy.typing.NDArray[numpy.int64] | None,
    ) -> tuple[
        int, # error code
        int, # The number of samples per channel that were read
    ]:
        assert isinstance(task_handle, TaskHandle)
        samps_per_chan_read = ctypes.c_int()

        channel_count = len(read_arrays)
        assert channel_count > 0
        array_size = read_arrays[0].size
        assert all(read_array.size == array_size for read_array in read_arrays)

        c_func = lib_importer.windll.DAQmxInternalReadAnalogWaveformPerChan
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        TaskHandle,
                        ctypes.c_int,
                        ctypes.c_double,
                        wrapped_ndpointer(dtype=numpy.int64, flags=("C", "W")),
                        wrapped_ndpointer(dtype=numpy.int64, flags=("C", "W")),
                        ctypes.c_uint,
                        CSetWfmAttrCallbackPtr,
                        ctypes.c_void_p,
                        ctypes.POINTER(ctypes.POINTER(ctypes.c_double)),
                        ctypes.c_uint,
                        ctypes.c_uint,
                        ctypes.POINTER(ctypes.c_int),
                        ctypes.POINTER(c_bool32),
                    ]

        read_array_pointers = (ctypes.POINTER(ctypes.c_double) * channel_count)()
        for i, read_array in enumerate(read_arrays):
            read_array_pointers[i] = read_array.ctypes.data_as(ctypes.POINTER(ctypes.c_double))

        error_code = c_func(
            task_handle,
            num_samps_per_chan,
            timeout,
            t0_array,
            dt_array,
            0 if t0_array is None else t0_array.size,
            self._get_wfm_attr_callback(properties),
            None,
            read_array_pointers,
            channel_count,
            array_size,
            ctypes.byref(samps_per_chan_read),
            None,
        )
        self.check_for_error(error_code, samps_per_chan_read=samps_per_chan_read.value)

        return error_code, samps_per_chan_read.value

    def _get_wfm_attr_callback(self, properties):
        if properties is not None:
            def set_wfm_attr_callback(
                channel_index: int,
                attribute_name: str,
                attribute_type: WfmAttrType,
                value: ExtendedPropertyValue,
                callback_data: object,
            ) -> int:
                properties[channel_index][attribute_name] = value
                return 0
            return self._get_wfm_attr_callback_ptr(set_wfm_attr_callback)
        else:
            return CSetWfmAttrCallbackPtr()

    def _get_wfm_attr_value(
        self, attribute_type: int, value: ctypes.c_void_p, value_size_in_bytes: int
    ) -> ExtendedPropertyValue:
        if attribute_type == WfmAttrType.BOOL32.value:
            assert value_size_in_bytes == 4
            return ctypes.cast(value, ctypes.POINTER(ctypes.c_int32))[0] != 0
        elif attribute_type == WfmAttrType.FLOAT64.value:
            assert value_size_in_bytes == 8
            return float(ctypes.cast(value, ctypes.POINTER(ctypes.c_double))[0])
        elif attribute_type == WfmAttrType.INT32.value:
            assert value_size_in_bytes == 4
            return int(ctypes.cast(value, ctypes.POINTER(ctypes.c_int32))[0])
        elif attribute_type == WfmAttrType.STRING.value:
            value_c_bytes = ctypes.cast(value, ctypes.POINTER(ctypes.c_byte))
            assert value_c_bytes[value_size_in_bytes - 1] == 0
            return bytes(value_c_bytes[0 : value_size_in_bytes - 1]).decode(lib_importer.encoding)
        else:
            raise ValueError(f"Unsupported attribute type {attribute_type}")

    def _get_wfm_attr_callback_ptr(
        self, set_wfm_attr_callback: SetWfmAttrCallback
    ) -> ctypes._FuncPointer:
        def _invoke_callback(
            channel_index: int,
            attribute_name: bytes,
            attribute_type: int,
            value: ctypes.c_void_p,
            value_size_in_bytes: int,
            callback_data: object,
        ) -> int:
            try:
                return set_wfm_attr_callback(
                    channel_index,
                    attribute_name.decode(lib_importer.encoding),
                    WfmAttrType(attribute_type),
                    self._get_wfm_attr_value(attribute_type, value, value_size_in_bytes),
                    callback_data,
                )
            except Exception:
                _logger.exception("Unhandled exception in set_wfm_attr_callback")
                return -1

        return CSetWfmAttrCallbackPtr(_invoke_callback)

    def _set_waveform_timings(
        self, 
        waveforms: Sequence[AnalogWaveform[numpy.float64] | DigitalWaveform[numpy.uint8]], 
        t0_array: numpy.typing.NDArray[numpy.int64], 
        dt_array: numpy.typing.NDArray[numpy.int64]
    ) -> None:
        for i, waveform in enumerate(waveforms):
            waveform.timing = Timing(
                sample_interval_mode=SampleIntervalMode.REGULAR,
                timestamp=_T0_EPOCH + ht_timedelta(seconds=t0_array[i] * _INT64_WFM_SEC_PER_TICK),
                sample_interval=ht_timedelta(seconds=dt_array[i] * _INT64_WFM_SEC_PER_TICK),
            )

    def read_digital_waveform(
        self,
        task_handle: object,
        number_of_samples_per_channel: int,
        timeout: float,
        waveform: DigitalWaveform[Any],
        waveform_attribute_mode: WaveformAttributeMode
    ) -> int:
        """Read a digital waveform with timing and attributes."""
        if WaveformAttributeMode.EXTENDED_PROPERTIES in waveform_attribute_mode:
            properties = [waveform.extended_properties]
        else:
            properties = None

        if WaveformAttributeMode.TIMING in waveform_attribute_mode:
            t0_array = numpy.zeros(1, dtype=numpy.int64)
            dt_array = numpy.zeros(1, dtype=numpy.int64)
        else:
            t0_array = None
            dt_array = None

        waveform.sample_count = number_of_samples_per_channel

        error_code, samples_read = self._internal_read_digital_waveform(
            task_handle,
            number_of_samples_per_channel,
            timeout,
            FillMode.GROUP_BY_CHANNEL.value,
            self._get_digital_read_array(waveform),
            properties,
            t0_array,
            dt_array,
            None,
        )

        waveform.sample_count = samples_read
        
        if t0_array is not None and dt_array is not None:
            self._set_waveform_timings([waveform], t0_array, dt_array)

        self.check_for_error(error_code, samps_per_chan_read=samples_read)
        return samples_read

    def _get_digital_read_array(self, waveform: DigitalWaveform[Any]) -> numpy.typing.NDArray[numpy.uint8]:  
        data = waveform.data
        if data.dtype != numpy.uint8:
            data = data.view(numpy.uint8)
        return data

    def read_digital_waveforms(
        self,
        task_handle: object,
        channel_count: int,
        number_of_samples_per_channel: int,
        number_of_signals_per_sample: int,
        timeout: float,
        waveforms: Sequence[DigitalWaveform[Any]],
        waveform_attribute_mode: WaveformAttributeMode,
    ) -> int:
        """Read a digital waveform with timing and attributes."""
        if WaveformAttributeMode.EXTENDED_PROPERTIES in waveform_attribute_mode:
            properties = [waveform.extended_properties for waveform in waveforms]
        else:
            properties = None

        if WaveformAttributeMode.TIMING in waveform_attribute_mode:
            t0_array = numpy.zeros(channel_count, dtype=numpy.int64)
            dt_array = numpy.zeros(channel_count, dtype=numpy.int64)
        else:
            t0_array = None
            dt_array = None

        # Since there's no DAQmxInternalReadDigitalWaveformPerChan, we have to allocate a
        # temporary contiguous array to read the data from multiple channels into.
        read_array = numpy.zeros(
            (number_of_samples_per_channel, channel_count, number_of_signals_per_sample),
            dtype=numpy.uint8)

        bytes_per_chan_array = numpy.zeros(channel_count, dtype=numpy.uint32)

        error_code, samples_read = self._internal_read_digital_waveform(
            task_handle,
            number_of_samples_per_channel,
            timeout,
            FillMode.GROUP_BY_SCAN_NUMBER.value, # GROUP_BY_SCAN_NUMBER handles short reads better than GROUP_BY_CHANNEL
            read_array,
            properties,
            t0_array,
            dt_array,
            bytes_per_chan_array,
        )

        for i, waveform in enumerate(waveforms):        
            waveform.sample_count = samples_read
            waveform_signal_count = waveform.data.shape[1]
            channel_signal_count = bytes_per_chan_array[i]
            if waveform_signal_count != channel_signal_count:
                raise ValueError(f"waveforms[{i}].data has {waveform_signal_count} signals, but expected {channel_signal_count}")
            waveform.data[:] = read_array[:, i, :channel_signal_count]

        if t0_array is not None and dt_array is not None:
            self._set_waveform_timings(waveforms, t0_array, dt_array)

        self.check_for_error(error_code, samps_per_chan_read=samples_read)
        return samples_read

    def read_new_digital_waveforms(
        self,
        task_handle: object,
        channel_count: int,
        number_of_samples_per_channel: int,
        number_of_signals_per_sample: int,
        timeout: float,
        waveform_attribute_mode: WaveformAttributeMode,
    ) -> Sequence[DigitalWaveform[numpy.uint8]]:
        """Read a digital waveform with timing and attributes."""
        if WaveformAttributeMode.EXTENDED_PROPERTIES in waveform_attribute_mode:
            properties = [ExtendedPropertyDictionary() for _ in range(channel_count)]
        else:
            properties = None

        if WaveformAttributeMode.TIMING in waveform_attribute_mode:
            t0_array = numpy.zeros(channel_count, dtype=numpy.int64)
            dt_array = numpy.zeros(channel_count, dtype=numpy.int64)
        else:
            t0_array = None
            dt_array = None

        read_array = numpy.zeros(
            (number_of_samples_per_channel, channel_count, number_of_signals_per_sample),
            dtype=numpy.uint8)

        bytes_per_chan_array = numpy.zeros(channel_count, dtype=numpy.uint32)

        error_code, samples_read = self._internal_read_digital_waveform(
            task_handle,
            number_of_samples_per_channel,
            timeout,
            FillMode.GROUP_BY_SCAN_NUMBER.value, # GROUP_BY_SCAN_NUMBER handles short reads better than GROUP_BY_CHANNEL
            read_array,
            properties,
            t0_array,
            dt_array,
            bytes_per_chan_array,
        )

        waveforms = []
        for i in range(channel_count):
            channel_signal_count = bytes_per_chan_array[i]
            waveform = DigitalWaveform(
                sample_count=samples_read,
                data=read_array[:, i, :channel_signal_count],
                copy_extended_properties=False,
                extended_properties=properties[i] if properties else None)
            waveforms.append(waveform)

        if t0_array is not None and dt_array is not None:
            self._set_waveform_timings(waveforms, t0_array, dt_array)

        self.check_for_error(error_code, samps_per_chan_read=samples_read)
        return waveforms

    def _internal_read_digital_waveform(
        self,
        task_handle: object,
        number_of_samples_per_channel: int,
        timeout: float,
        fill_mode: int,
        read_array: numpy.typing.NDArray[numpy.uint8],
        properties: Sequence[ExtendedPropertyDictionary] | None,
        t0_array: numpy.typing.NDArray[numpy.int64] | None,
        dt_array: numpy.typing.NDArray[numpy.int64] | None,
        bytes_per_chan_array: numpy.typing.NDArray[numpy.uint32] | None = None,
    ) -> tuple[
        int, # error code
        int, # The number of samples per channel that were read
    ]:
        assert isinstance(task_handle, TaskHandle)
        samps_per_chan_read = ctypes.c_int()
        num_bytes_per_samp = ctypes.c_int()

        c_func = lib_importer.windll.DAQmxInternalReadDigitalWaveform
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        TaskHandle,
                        ctypes.c_int,
                        ctypes.c_double,
                        ctypes.c_int,
                        wrapped_ndpointer(dtype=numpy.int64, flags=("C", "W")),
                        wrapped_ndpointer(dtype=numpy.int64, flags=("C", "W")),
                        ctypes.c_uint,
                        CSetWfmAttrCallbackPtr,
                        ctypes.c_void_p,
                        wrapped_ndpointer(dtype=numpy.uint8, flags=("C", "W")),
                        ctypes.c_uint,
                        ctypes.POINTER(ctypes.c_int),
                        ctypes.POINTER(ctypes.c_int),
                        wrapped_ndpointer(dtype=numpy.uint32, flags=("C", "W")),
                        ctypes.c_uint,
                        ctypes.POINTER(c_bool32),
                    ]

        error_code = c_func(
            task_handle,
            number_of_samples_per_channel,
            timeout,
            fill_mode,
            t0_array,
            dt_array,
            0 if t0_array is None else t0_array.size,
            self._get_wfm_attr_callback(properties),
            None,
            read_array,
            read_array.size,
            ctypes.byref(samps_per_chan_read),
            ctypes.byref(num_bytes_per_samp),
            bytes_per_chan_array,
            0 if bytes_per_chan_array is None else bytes_per_chan_array.size,
            None,
        )

        return error_code, samps_per_chan_read.value

    def read_id_pin_memory(self, device_name, id_pin_name):
        data_length_read = ctypes.c_uint()
        format_code = ctypes.c_uint()

        c_func = lib_importer.windll.DAQmxReadIDPinMemory
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes_byte_str, ctypes_byte_str,
                        wrapped_ndpointer(dtype=numpy.uint8, flags=('C','W')),
                        ctypes.c_uint, ctypes.POINTER(ctypes.c_uint),
                        ctypes.POINTER(ctypes.c_uint)]

        array_size = c_func(
            device_name, id_pin_name, None, 0,
            ctypes.byref(data_length_read), ctypes.byref(format_code))

        if array_size < 0:
            self.check_for_error(array_size)

        data = numpy.zeros(array_size, dtype=numpy.uint8)

        error_code = c_func(
            device_name, id_pin_name, data, array_size,
            ctypes.byref(data_length_read), ctypes.byref(format_code))
        self.check_for_error(error_code)
        return data.tolist(), data_length_read.value, format_code.value

    def read_power_binary_i16(
            self, task, num_samps_per_chan, timeout, fill_mode,
            read_voltage_array, read_current_array):
        samps_per_chan_read = ctypes.c_int()

        c_func = lib_importer.windll.DAQmxReadPowerBinaryI16
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int, ctypes.c_double,
                        c_bool32,
                        wrapped_ndpointer(dtype=numpy.int16, flags=('C', 'W')),
                        wrapped_ndpointer(dtype=numpy.int16, flags=('C', 'W')),
                        ctypes.c_uint, ctypes.POINTER(ctypes.c_int),
                        ctypes.POINTER(c_bool32)]

        error_code = c_func(
            task, num_samps_per_chan, timeout, fill_mode,
            read_voltage_array, read_current_array, read_voltage_array.size,
            ctypes.byref(samps_per_chan_read), None)
        self.check_for_error(error_code, samps_per_chan_read=samps_per_chan_read.value)

        return read_voltage_array, read_current_array, samps_per_chan_read.value

    def read_power_f64(
            self, task, num_samps_per_chan, timeout, fill_mode,
            read_voltage_array, read_current_array):
        samps_per_chan_read = ctypes.c_int()

        c_func = lib_importer.windll.DAQmxReadPowerF64
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int, ctypes.c_double,
                        c_bool32,
                        wrapped_ndpointer(dtype=numpy.float64, flags=('C', 'W')),
                        wrapped_ndpointer(dtype=numpy.float64, flags=('C', 'W')),
                        ctypes.c_uint, ctypes.POINTER(ctypes.c_int),
                        ctypes.POINTER(c_bool32)]

        error_code = c_func(
            task, num_samps_per_chan, timeout, fill_mode,
            read_voltage_array, read_current_array, read_voltage_array.size,
            ctypes.byref(samps_per_chan_read), None)
        self.check_for_error(error_code, samps_per_chan_read=samps_per_chan_read.value)

        return read_voltage_array, read_current_array, samps_per_chan_read.value

    def read_raw(self, task, num_samps_per_chan, timeout, read_array):
        samples_read = ctypes.c_int()
        number_of_bytes_per_sample = ctypes.c_int()

        c_func = lib_importer.windll.DAQmxReadRaw
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int, ctypes.c_double,
                        wrapped_ndpointer(dtype=read_array.dtype, flags=('C', 'W')),
                        ctypes.c_uint, ctypes.POINTER(ctypes.c_int),
                        ctypes.POINTER(ctypes.c_int), ctypes.POINTER(c_bool32)]

        error_code = c_func(
            task, num_samps_per_chan, timeout, read_array,
            read_array.nbytes, ctypes.byref(samples_read),
            ctypes.byref(number_of_bytes_per_sample), None)
        self.check_for_error(error_code, samps_per_chan_read=samples_read.value)

        return read_array, samples_read.value, number_of_bytes_per_sample.value

    def write_analog_waveform(
        self,
        task_handle: object,
        waveform: AnalogWaveform[Any],
        auto_start: bool,
        timeout: float
    ) -> int:
        """Write an analog waveform."""
        return self.write_analog_f64(
            task_handle,
            waveform.sample_count,
            auto_start,
            timeout,
            FillMode.GROUP_BY_CHANNEL.value,
            self._get_analog_write_array(waveform),
        )

    def write_analog_waveforms(
        self,
        task_handle: object,
        waveforms: Sequence[AnalogWaveform[Any]],
        auto_start: bool,
        timeout: float
    ) -> int:
        """Write analog waveforms."""
        num_samps_per_chan = get_num_samps_per_chan(waveforms)

        write_arrays = [self._get_analog_write_array(waveform) for waveform in waveforms]

        error_code, samples_written = self._internal_write_analog_waveform_per_chan(
            task_handle,
            num_samps_per_chan,
            auto_start,
            timeout,
            write_arrays,
        )

        self.check_for_error(error_code, samps_per_chan_written=samples_written)
        return samples_written

    def _get_analog_write_array(self, waveform: AnalogWaveform[Any]) -> numpy.typing.NDArray[numpy.float64]:  
        scaled_data = waveform.scaled_data
        if scaled_data.flags.c_contiguous:
            return scaled_data
        return scaled_data.copy(order="C")

    def _internal_write_analog_waveform_per_chan(
        self,
        task_handle: object,
        num_samps_per_chan: int,
        auto_start: bool,
        timeout: float,
        write_arrays: Sequence[numpy.typing.NDArray[numpy.float64]],
    ) -> tuple[
        int, # error code
        int, # The number of samples per channel that were written
    ]:
        assert isinstance(task_handle, TaskHandle)
        samps_per_chan_written = ctypes.c_int()

        channel_count = len(write_arrays)
        assert channel_count > 0
        assert all(write_array.size >= num_samps_per_chan for write_array in write_arrays)

        c_func = lib_importer.windll.DAQmxInternalWriteAnalogWaveformPerChan
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        TaskHandle,
                        ctypes.c_int,
                        c_bool32,
                        ctypes.c_double,
                        ctypes.POINTER(ctypes.POINTER(ctypes.c_double)),
                        ctypes.c_uint,
                        ctypes.POINTER(ctypes.c_int),
                        ctypes.POINTER(c_bool32),
                    ]

        write_array_pointers = (ctypes.POINTER(ctypes.c_double) * channel_count)()
        for i, write_array in enumerate(write_arrays):
            write_array_pointers[i] = write_array.ctypes.data_as(ctypes.POINTER(ctypes.c_double))

        error_code = c_func(
            task_handle,
            num_samps_per_chan,
            auto_start,
            timeout,
            write_array_pointers,
            channel_count,
            ctypes.byref(samps_per_chan_written),
            None,
        )

        return error_code, samps_per_chan_written.value

    def write_digital_waveform(
        self,
        task_handle: object,
        waveform: DigitalWaveform[Any],
        auto_start: bool,
        timeout: float,
    ) -> int:
        """Write a digital waveform."""
        bytes_per_chan_array = numpy.array([waveform.signal_count], dtype=numpy.uint32)

        error_code, samples_written = self._internal_write_digital_waveform(
            task_handle,
            waveform.sample_count,
            auto_start,
            timeout,
            FillMode.GROUP_BY_CHANNEL.value,
            self._get_digital_write_array(waveform),
            bytes_per_chan_array,
        )

        self.check_for_error(error_code, samps_per_chan_written=samples_written)
        return samples_written

    def _get_digital_write_array(self, waveform: DigitalWaveform[Any]) -> numpy.typing.NDArray[numpy.uint8]:  
        data = waveform.data
        if data.dtype != numpy.uint8:
            data = data.view(numpy.uint8)
        if data.flags.c_contiguous:
            return data
        return data.copy(order="C")

    def write_digital_waveforms(
        self,
        task_handle: object,
        waveforms: Sequence[DigitalWaveform[Any]],
        auto_start: bool,
        timeout: float,
    ) -> int:
        """Write digital waveforms."""
        channel_count = len(waveforms)
        sample_count = get_num_samps_per_chan(waveforms)
                
        bytes_per_chan_array = numpy.array([wf.signal_count for wf in waveforms], dtype=numpy.uint32)

        # build a temporary contiguous array to write the data from multiple channels into.
        # write_array must be in the format (numChans x numSampsPerChan x maxDataWidth)
        write_array = numpy.zeros(
            (channel_count, sample_count, max(bytes_per_chan_array)),
            dtype=numpy.uint8,
        )
        for i, waveform in enumerate(waveforms):
            signal_count = waveform.signal_count
            write_array[i, :, :signal_count] = waveform.data

        error_code, samples_written = self._internal_write_digital_waveform(
            task_handle,
            sample_count,
            auto_start,
            timeout,
            FillMode.GROUP_BY_CHANNEL.value,
            write_array,
            bytes_per_chan_array,
        )

        self.check_for_error(error_code, samps_per_chan_written=samples_written)
        return samples_written

    def _internal_write_digital_waveform(
        self,
        task_handle: object,
        num_samps_per_chan: int,
        auto_start: bool,
        timeout: float,
        data_layout: int,
        write_array: numpy.typing.NDArray[numpy.uint8],
        bytes_per_chan_array: numpy.typing.NDArray[numpy.uint32] | None = None,
    ) -> tuple[
        int, # error code
        int, # The number of samples per channel that were written
    ]:
        assert isinstance(task_handle, TaskHandle)
        samps_per_chan_written = ctypes.c_int()

        c_func = lib_importer.windll.DAQmxInternalWriteDigitalWaveform
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        TaskHandle,
                        ctypes.c_int,
                        c_bool32,
                        ctypes.c_double,
                        c_bool32,
                        wrapped_ndpointer(dtype=numpy.uint8, flags=("C",)),
                        wrapped_ndpointer(dtype=numpy.uint32, flags=("C",)),
                        ctypes.c_uint,
                        ctypes.POINTER(ctypes.c_int),
                        ctypes.POINTER(c_bool32),
                    ]

        error_code = c_func(
            task_handle,
            num_samps_per_chan,
            auto_start,
            timeout,
            data_layout,
            write_array,
            bytes_per_chan_array,
            0 if bytes_per_chan_array is None else bytes_per_chan_array.size,
            ctypes.byref(samps_per_chan_written),
            None,
        )

        return error_code, samps_per_chan_written.value

    def write_raw(
            self, task_handle, num_samps_per_chan, auto_start, timeout, numpy_array):
        samps_per_chan_written = ctypes.c_int()

        c_func = lib_importer.windll.DAQmxWriteRaw
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int, c_bool32,
                        ctypes.c_double,
                        wrapped_ndpointer(dtype=numpy_array.dtype,
                                        flags=('C')),
                        ctypes.POINTER(ctypes.c_int), ctypes.POINTER(c_bool32)]

        error_code = c_func(
            task_handle, num_samps_per_chan, auto_start, timeout, numpy_array,
            ctypes.byref(samps_per_chan_written), None)
        self.check_for_error(error_code, samps_per_chan_written=samps_per_chan_written.value)

        return samps_per_chan_written.value

    def hash_task_handle(self, task_handle):
        return hash(task_handle.value)

    def check_for_error(self, error_code, samps_per_chan_written=None, samps_per_chan_read=None):
        if not error_code:
            return

        if error_code < 0:
            extended_error_info = self.get_extended_error_info()

            if samps_per_chan_read is not None:
                raise DaqReadError(extended_error_info, error_code, samps_per_chan_read)
            elif samps_per_chan_written is not None:
                raise DaqWriteError(extended_error_info, error_code, samps_per_chan_written)
            else:
                raise DaqError(extended_error_info, error_code)

        elif error_code > 0:
            error_string = self.get_error_string(error_code)

            warnings.warn(DaqWarning(error_string, error_code))


def is_string_buffer_too_small(error_code):
    return (
        error_code == DAQmxErrors.BUFFER_TOO_SMALL_FOR_STRING or
        error_code == DAQmxWarnings.CAPI_STRING_TRUNCATED_TO_FIT_BUFFER)


def is_array_buffer_too_small(error_code):
    return error_code == DAQmxErrors.WRITE_BUFFER_TOO_SMALL
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=generated/nidaqmx/_linux_installation_commands.py sha256=69c34019fc77080173bf1c6c361853e2b6dbd8f1df23bacd09ba142ff4836536 bytes=3036 -->
## FILE: generated/nidaqmx/_linux_installation_commands.py

- repository: `ni/nidaqmx-python`
- source_path: `generated/nidaqmx/_linux_installation_commands.py`
- sha256: `69c34019fc77080173bf1c6c361853e2b6dbd8f1df23bacd09ba142ff4836536`
- bytes: 3036

````python
from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass


def _get_version_ubuntu(dist_version: str) -> str:
    return dist_version.replace(".", "")


def _get_version_opensuse(dist_version: str) -> str:
    return dist_version.replace(".", "")


def _get_version_rhel(dist_version: str) -> str:
    return dist_version.split(".")[0]


# Command templates
_APT_INSTALL_COMMANDS = [
    ["apt", "update"],
    [
        "apt",
        "install",
        "{directory}/NILinux{release}DeviceDrivers/ni-ubuntu{version}-drivers-{release}.deb",
    ],
    ["apt", "update"],
    ["apt", "install", "ni-daqmx"],
    ["dkms", "autoinstall"],
]

_ZYPPER_INSTALL_COMMANDS = [
    ["zypper", "update"],
    ["zypper", "install", "insserv"],
    [
        "zypper",
        "--no-gpg-checks",
        "install",
        "{directory}/NILinux{release}DeviceDrivers/ni-opensuse{version}-drivers-{release}.rpm",
    ],
    ["zypper", "refresh"],
    ["zypper", "install", "ni-daqmx"],
    ["dkms", "autoinstall"],
]

_YUM_INSTALL_COMMANDS = [
    ["yum", "update"],
    ["yum", "install", "chkconfig"],
    [
        "yum",
        "install",
        "{directory}/NILinux{release}DeviceDrivers/ni-rhel{version}-drivers-{release}.rpm",
    ],
    ["yum", "install", "ni-daqmx"],
    ["dkms", "autoinstall"],
]

_DEBIAN_DAQMX_VERSION_COMMAND = ["dpkg", "-l", "ni-daqmx"]
_RPM_DAQMX_VERSION_COMMAND = ["rpm", "-q", "ni-daqmx"]


@dataclass
class DistroInfo:  # noqa: D101 - Missing docstring in public class (auto-generated noqa)
    get_distro_version: Callable[[str], str]
    get_daqmx_version: list[str]
    install_commands: list[list[str]]


# Mapping of Linux distributions to their command templates and version handlers
LINUX_COMMANDS = {
    "ubuntu": DistroInfo(_get_version_ubuntu, _DEBIAN_DAQMX_VERSION_COMMAND, _APT_INSTALL_COMMANDS),
    "opensuse": DistroInfo(
        _get_version_opensuse, _RPM_DAQMX_VERSION_COMMAND, _ZYPPER_INSTALL_COMMANDS
    ),
    "rhel": DistroInfo(_get_version_rhel, _RPM_DAQMX_VERSION_COMMAND, _YUM_INSTALL_COMMANDS),
}


def get_linux_installation_commands(
    _directory_to_extract_to: str, dist_name: str, dist_version: str, _release_string: str
) -> list[list[str]]:
    """Get the installation commands for Linux based on the distribution."""
    if dist_name not in LINUX_COMMANDS:
        raise ValueError(f"Unsupported distribution '{dist_name}'")

    commands_info = LINUX_COMMANDS[dist_name]
    version = commands_info.get_distro_version(dist_version)
    install_commands = commands_info.install_commands

    # Format commands with the provided variables
    formatted_commands = [
        [
            cmd_part.format(
                directory=_directory_to_extract_to, release=_release_string, version=version
            )
            for cmd_part in cmd
        ]
        for cmd in install_commands
    ]

    return formatted_commands
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=generated/nidaqmx/_stubs/__init__.py sha256=6b8633e3b4868086a9b007d445d75572ddfc0bedfb22cfb4b3b5300fe6aba250 bytes=34 -->
## FILE: generated/nidaqmx/_stubs/__init__.py

- repository: `ni/nidaqmx-python`
- source_path: `generated/nidaqmx/_stubs/__init__.py`
- sha256: `6b8633e3b4868086a9b007d445d75572ddfc0bedfb22cfb4b3b5300fe6aba250`
- bytes: 34

````python
"""Auto generated gRPC files."""
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=generated/nidaqmx/_stubs/data_moniker_pb2.py sha256=519fe5b2789cd3e241adc28d8e1ff5236626ca535e57f2c475e4742f57327568 bytes=4663 -->
## FILE: generated/nidaqmx/_stubs/data_moniker_pb2.py

- repository: `ni/nidaqmx-python`
- source_path: `generated/nidaqmx/_stubs/data_moniker_pb2.py`
- sha256: `519fe5b2789cd3e241adc28d8e1ff5236626ca535e57f2c475e4742f57327568`
- bytes: 4663

````python
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: data_moniker.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12\x64\x61ta_moniker.proto\x12\x10ni.data_monikers\x1a\x19google/protobuf/any.proto\"\x8a\x01\n!BeginMonikerSidebandStreamRequest\x12\x34\n\x08strategy\x18\x01 \x01(\x0e\x32\".ni.data_monikers.SidebandStrategy\x12/\n\x08monikers\x18\x02 \x01(\x0b\x32\x1d.ni.data_monikers.MonikerList\"\xa4\x01\n\"BeginMonikerSidebandStreamResponse\x12\x34\n\x08strategy\x18\x01 \x01(\x0e\x32\".ni.data_monikers.SidebandStrategy\x12\x16\n\x0e\x63onnection_url\x18\x02 \x01(\t\x12\x1b\n\x13sideband_identifier\x18\x03 \x01(\t\x12\x13\n\x0b\x62uffer_size\x18\x04 \x01(\x12\"O\n\x07Moniker\x12\x18\n\x10service_location\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x61ta_source\x18\x02 \x01(\t\x12\x15\n\rdata_instance\x18\x03 \x01(\x03\"\x87\x01\n\x13MonikerWriteRequest\x12\x31\n\x08monikers\x18\x01 \x01(\x0b\x32\x1d.ni.data_monikers.MonikerListH\x00\x12/\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x1f.ni.data_monikers.MonikerValuesH\x00\x42\x0c\n\nwrite_data\"D\n\x13MonikerReadResponse\x12-\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\x1f.ni.data_monikers.MonikerValues\"r\n\x0bMonikerList\x12\x30\n\rread_monikers\x18\x02 \x03(\x0b\x32\x19.ni.data_monikers.Moniker\x12\x31\n\x0ewrite_monikers\x18\x03 \x03(\x0b\x32\x19.ni.data_monikers.Moniker\"5\n\rMonikerValues\x12$\n\x06values\x18\x01 \x03(\x0b\x32\x14.google.protobuf.Any\"W\n\x14SidebandWriteRequest\x12\x0e\n\x06\x63\x61ncel\x18\x01 \x01(\x08\x12/\n\x06values\x18\x02 \x01(\x0b\x32\x1f.ni.data_monikers.MonikerValues\"W\n\x14SidebandReadResponse\x12\x0e\n\x06\x63\x61ncel\x18\x01 \x01(\x08\x12/\n\x06values\x18\x02 \x01(\x0b\x32\x1f.ni.data_monikers.MonikerValues\"\x15\n\x13StreamWriteResponse*\xbd\x01\n\x10SidebandStrategy\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x08\n\x04GRPC\x10\x01\x12\x11\n\rSHARED_MEMORY\x10\x02\x12!\n\x1d\x44OUBLE_BUFFERED_SHARED_MEMORY\x10\x03\x12\x0b\n\x07SOCKETS\x10\x04\x12\x17\n\x13SOCKETS_LOW_LATENCY\x10\x05\x12\x16\n\x12HYPERVISOR_SOCKETS\x10\x06\x12\x08\n\x04RDMA\x10\x07\x12\x14\n\x10RDMA_LOW_LATENCY\x10\x08\x32\xb4\x03\n\x0b\x44\x61taMoniker\x12\x82\x01\n\x13\x42\x65ginSidebandStream\x12\x33.ni.data_monikers.BeginMonikerSidebandStreamRequest\x1a\x34.ni.data_monikers.BeginMonikerSidebandStreamResponse\"\x00\x12\x65\n\x0fStreamReadWrite\x12%.ni.data_monikers.MonikerWriteRequest\x1a%.ni.data_monikers.MonikerReadResponse\"\x00(\x01\x30\x01\x12V\n\nStreamRead\x12\x1d.ni.data_monikers.MonikerList\x1a%.ni.data_monikers.MonikerReadResponse\"\x00\x30\x01\x12\x61\n\x0bStreamWrite\x12%.ni.data_monikers.MonikerWriteRequest\x1a%.ni.data_monikers.StreamWriteResponse\"\x00(\x01\x30\x01\x42&\xf8\x01\x01\xaa\x02 NationalInstruments.DataMonikersb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'data_moniker_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\370\001\001\252\002 NationalInstruments.DataMonikers'
  _SIDEBANDSTRATEGY._serialized_start=1037
  _SIDEBANDSTRATEGY._serialized_end=1226
  _BEGINMONIKERSIDEBANDSTREAMREQUEST._serialized_start=68
  _BEGINMONIKERSIDEBANDSTREAMREQUEST._serialized_end=206
  _BEGINMONIKERSIDEBANDSTREAMRESPONSE._serialized_start=209
  _BEGINMONIKERSIDEBANDSTREAMRESPONSE._serialized_end=373
  _MONIKER._serialized_start=375
  _MONIKER._serialized_end=454
  _MONIKERWRITEREQUEST._serialized_start=457
  _MONIKERWRITEREQUEST._serialized_end=592
  _MONIKERREADRESPONSE._serialized_start=594
  _MONIKERREADRESPONSE._serialized_end=662
  _MONIKERLIST._serialized_start=664
  _MONIKERLIST._serialized_end=778
  _MONIKERVALUES._serialized_start=780
  _MONIKERVALUES._serialized_end=833
  _SIDEBANDWRITEREQUEST._serialized_start=835
  _SIDEBANDWRITEREQUEST._serialized_end=922
  _SIDEBANDREADRESPONSE._serialized_start=924
  _SIDEBANDREADRESPONSE._serialized_end=1011
  _STREAMWRITERESPONSE._serialized_start=1013
  _STREAMWRITERESPONSE._serialized_end=1034
  _DATAMONIKER._serialized_start=1229
  _DATAMONIKER._serialized_end=1665
# @@protoc_insertion_point(module_scope)
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=generated/nidaqmx/_stubs/data_moniker_pb2.pyi sha256=cf984cc193b84014307877d40b00661b4f58756f4bcdee7924af18aef358845e bytes=9312 -->
## FILE: generated/nidaqmx/_stubs/data_moniker_pb2.pyi

- repository: `ni/nidaqmx-python`
- source_path: `generated/nidaqmx/_stubs/data_moniker_pb2.pyi`
- sha256: `cf984cc193b84014307877d40b00661b4f58756f4bcdee7924af18aef358845e`
- bytes: 9312

````python
"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.any_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _SidebandStrategy:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _SidebandStrategyEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_SidebandStrategy.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    UNKNOWN: _SidebandStrategy.ValueType  # 0
    GRPC: _SidebandStrategy.ValueType  # 1
    SHARED_MEMORY: _SidebandStrategy.ValueType  # 2
    DOUBLE_BUFFERED_SHARED_MEMORY: _SidebandStrategy.ValueType  # 3
    SOCKETS: _SidebandStrategy.ValueType  # 4
    SOCKETS_LOW_LATENCY: _SidebandStrategy.ValueType  # 5
    HYPERVISOR_SOCKETS: _SidebandStrategy.ValueType  # 6
    RDMA: _SidebandStrategy.ValueType  # 7
    RDMA_LOW_LATENCY: _SidebandStrategy.ValueType  # 8

class SidebandStrategy(_SidebandStrategy, metaclass=_SidebandStrategyEnumTypeWrapper): ...

UNKNOWN: SidebandStrategy.ValueType  # 0
GRPC: SidebandStrategy.ValueType  # 1
SHARED_MEMORY: SidebandStrategy.ValueType  # 2
DOUBLE_BUFFERED_SHARED_MEMORY: SidebandStrategy.ValueType  # 3
SOCKETS: SidebandStrategy.ValueType  # 4
SOCKETS_LOW_LATENCY: SidebandStrategy.ValueType  # 5
HYPERVISOR_SOCKETS: SidebandStrategy.ValueType  # 6
RDMA: SidebandStrategy.ValueType  # 7
RDMA_LOW_LATENCY: SidebandStrategy.ValueType  # 8
global___SidebandStrategy = SidebandStrategy

@typing.final
class BeginMonikerSidebandStreamRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STRATEGY_FIELD_NUMBER: builtins.int
    MONIKERS_FIELD_NUMBER: builtins.int
    strategy: global___SidebandStrategy.ValueType
    @property
    def monikers(self) -> global___MonikerList: ...
    def __init__(
        self,
        *,
        strategy: global___SidebandStrategy.ValueType = ...,
        monikers: global___MonikerList | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["monikers", b"monikers"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["monikers", b"monikers", "strategy", b"strategy"]) -> None: ...

global___BeginMonikerSidebandStreamRequest = BeginMonikerSidebandStreamRequest

@typing.final
class BeginMonikerSidebandStreamResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STRATEGY_FIELD_NUMBER: builtins.int
    CONNECTION_URL_FIELD_NUMBER: builtins.int
    SIDEBAND_IDENTIFIER_FIELD_NUMBER: builtins.int
    BUFFER_SIZE_FIELD_NUMBER: builtins.int
    strategy: global___SidebandStrategy.ValueType
    connection_url: builtins.str
    sideband_identifier: builtins.str
    buffer_size: builtins.int
    def __init__(
        self,
        *,
        strategy: global___SidebandStrategy.ValueType = ...,
        connection_url: builtins.str = ...,
        sideband_identifier: builtins.str = ...,
        buffer_size: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["buffer_size", b"buffer_size", "connection_url", b"connection_url", "sideband_identifier", b"sideband_identifier", "strategy", b"strategy"]) -> None: ...

global___BeginMonikerSidebandStreamResponse = BeginMonikerSidebandStreamResponse

@typing.final
class Moniker(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERVICE_LOCATION_FIELD_NUMBER: builtins.int
    DATA_SOURCE_FIELD_NUMBER: builtins.int
    DATA_INSTANCE_FIELD_NUMBER: builtins.int
    service_location: builtins.str
    data_source: builtins.str
    data_instance: builtins.int
    def __init__(
        self,
        *,
        service_location: builtins.str = ...,
        data_source: builtins.str = ...,
        data_instance: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["data_instance", b"data_instance", "data_source", b"data_source", "service_location", b"service_location"]) -> None: ...

global___Moniker = Moniker

@typing.final
class MonikerWriteRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MONIKERS_FIELD_NUMBER: builtins.int
    DATA_FIELD_NUMBER: builtins.int
    @property
    def monikers(self) -> global___MonikerList: ...
    @property
    def data(self) -> global___MonikerValues: ...
    def __init__(
        self,
        *,
        monikers: global___MonikerList | None = ...,
        data: global___MonikerValues | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["data", b"data", "monikers", b"monikers", "write_data", b"write_data"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["data", b"data", "monikers", b"monikers", "write_data", b"write_data"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["write_data", b"write_data"]) -> typing.Literal["monikers", "data"] | None: ...

global___MonikerWriteRequest = MonikerWriteRequest

@typing.final
class MonikerReadResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATA_FIELD_NUMBER: builtins.int
    @property
    def data(self) -> global___MonikerValues: ...
    def __init__(
        self,
        *,
        data: global___MonikerValues | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["data", b"data"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["data", b"data"]) -> None: ...

global___MonikerReadResponse = MonikerReadResponse

@typing.final
class MonikerList(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    READ_MONIKERS_FIELD_NUMBER: builtins.int
    WRITE_MONIKERS_FIELD_NUMBER: builtins.int
    @property
    def read_monikers(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Moniker]: ...
    @property
    def write_monikers(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Moniker]: ...
    def __init__(
        self,
        *,
        read_monikers: collections.abc.Iterable[global___Moniker] | None = ...,
        write_monikers: collections.abc.Iterable[global___Moniker] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["read_monikers", b"read_monikers", "write_monikers", b"write_monikers"]) -> None: ...

global___MonikerList = MonikerList

@typing.final
class MonikerValues(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VALUES_FIELD_NUMBER: builtins.int
    @property
    def values(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.protobuf.any_pb2.Any]: ...
    def __init__(
        self,
        *,
        values: collections.abc.Iterable[google.protobuf.any_pb2.Any] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["values", b"values"]) -> None: ...

global___MonikerValues = MonikerValues

@typing.final
class SidebandWriteRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CANCEL_FIELD_NUMBER: builtins.int
    VALUES_FIELD_NUMBER: builtins.int
    cancel: builtins.bool
    @property
    def values(self) -> global___MonikerValues: ...
    def __init__(
        self,
        *,
        cancel: builtins.bool = ...,
        values: global___MonikerValues | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["values", b"values"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["cancel", b"cancel", "values", b"values"]) -> None: ...

global___SidebandWriteRequest = SidebandWriteRequest

@typing.final
class SidebandReadResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CANCEL_FIELD_NUMBER: builtins.int
    VALUES_FIELD_NUMBER: builtins.int
    cancel: builtins.bool
    @property
    def values(self) -> global___MonikerValues: ...
    def __init__(
        self,
        *,
        cancel: builtins.bool = ...,
        values: global___MonikerValues | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["values", b"values"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["cancel", b"cancel", "values", b"values"]) -> None: ...

global___SidebandReadResponse = SidebandReadResponse

@typing.final
class StreamWriteResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___StreamWriteResponse = StreamWriteResponse
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=generated/nidaqmx/_stubs/data_moniker_pb2_grpc.py sha256=4e0ff7db7ba4739768c10ae0a747e1864e1e972431246f13a3310ab74c48977c bytes=7697 -->
## FILE: generated/nidaqmx/_stubs/data_moniker_pb2_grpc.py

- repository: `ni/nidaqmx-python`
- source_path: `generated/nidaqmx/_stubs/data_moniker_pb2_grpc.py`
- sha256: `4e0ff7db7ba4739768c10ae0a747e1864e1e972431246f13a3310ab74c48977c`
- bytes: 7697

````python
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from nidaqmx._stubs import data_moniker_pb2 as data__moniker__pb2


class DataMonikerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.BeginSidebandStream = channel.unary_unary(
                '/ni.data_monikers.DataMoniker/BeginSidebandStream',
                request_serializer=data__moniker__pb2.BeginMonikerSidebandStreamRequest.SerializeToString,
                response_deserializer=data__moniker__pb2.BeginMonikerSidebandStreamResponse.FromString,
                )
        self.StreamReadWrite = channel.stream_stream(
                '/ni.data_monikers.DataMoniker/StreamReadWrite',
                request_serializer=data__moniker__pb2.MonikerWriteRequest.SerializeToString,
                response_deserializer=data__moniker__pb2.MonikerReadResponse.FromString,
                )
        self.StreamRead = channel.unary_stream(
                '/ni.data_monikers.DataMoniker/StreamRead',
                request_serializer=data__moniker__pb2.MonikerList.SerializeToString,
                response_deserializer=data__moniker__pb2.MonikerReadResponse.FromString,
                )
        self.StreamWrite = channel.stream_stream(
                '/ni.data_monikers.DataMoniker/StreamWrite',
                request_serializer=data__moniker__pb2.MonikerWriteRequest.SerializeToString,
                response_deserializer=data__moniker__pb2.StreamWriteResponse.FromString,
                )


class DataMonikerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def BeginSidebandStream(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamReadWrite(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamRead(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamWrite(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DataMonikerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'BeginSidebandStream': grpc.unary_unary_rpc_method_handler(
                    servicer.BeginSidebandStream,
                    request_deserializer=data__moniker__pb2.BeginMonikerSidebandStreamRequest.FromString,
                    response_serializer=data__moniker__pb2.BeginMonikerSidebandStreamResponse.SerializeToString,
            ),
            'StreamReadWrite': grpc.stream_stream_rpc_method_handler(
                    servicer.StreamReadWrite,
                    request_deserializer=data__moniker__pb2.MonikerWriteRequest.FromString,
                    response_serializer=data__moniker__pb2.MonikerReadResponse.SerializeToString,
            ),
            'StreamRead': grpc.unary_stream_rpc_method_handler(
                    servicer.StreamRead,
                    request_deserializer=data__moniker__pb2.MonikerList.FromString,
                    response_serializer=data__moniker__pb2.MonikerReadResponse.SerializeToString,
            ),
            'StreamWrite': grpc.stream_stream_rpc_method_handler(
                    servicer.StreamWrite,
                    request_deserializer=data__moniker__pb2.MonikerWriteRequest.FromString,
                    response_serializer=data__moniker__pb2.StreamWriteResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ni.data_monikers.DataMoniker', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DataMoniker(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def BeginSidebandStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ni.data_monikers.DataMoniker/BeginSidebandStream',
            data__moniker__pb2.BeginMonikerSidebandStreamRequest.SerializeToString,
            data__moniker__pb2.BeginMonikerSidebandStreamResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StreamReadWrite(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/ni.data_monikers.DataMoniker/StreamReadWrite',
            data__moniker__pb2.MonikerWriteRequest.SerializeToString,
            data__moniker__pb2.MonikerReadResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StreamRead(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/ni.data_monikers.DataMoniker/StreamRead',
            data__moniker__pb2.MonikerList.SerializeToString,
            data__moniker__pb2.MonikerReadResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StreamWrite(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/ni.data_monikers.DataMoniker/StreamWrite',
            data__moniker__pb2.MonikerWriteRequest.SerializeToString,
            data__moniker__pb2.StreamWriteResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=generated/nidaqmx/_stubs/data_moniker_pb2_grpc.pyi sha256=b3cbb8ec86e4796157547f44de7ae1b39f37ea93304ca03be850aa75ab0f41f5 bytes=3451 -->
## FILE: generated/nidaqmx/_stubs/data_moniker_pb2_grpc.pyi

- repository: `ni/nidaqmx-python`
- source_path: `generated/nidaqmx/_stubs/data_moniker_pb2_grpc.pyi`
- sha256: `b3cbb8ec86e4796157547f44de7ae1b39f37ea93304ca03be850aa75ab0f41f5`
- bytes: 3451

````python
"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
from nidaqmx._stubs import data_moniker_pb2
import grpc
import grpc.aio
import typing

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class DataMonikerStub:
    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    BeginSidebandStream: grpc.UnaryUnaryMultiCallable[
        data_moniker_pb2.BeginMonikerSidebandStreamRequest,
        data_moniker_pb2.BeginMonikerSidebandStreamResponse,
    ]

    StreamReadWrite: grpc.StreamStreamMultiCallable[
        data_moniker_pb2.MonikerWriteRequest,
        data_moniker_pb2.MonikerReadResponse,
    ]

    StreamRead: grpc.UnaryStreamMultiCallable[
        data_moniker_pb2.MonikerList,
        data_moniker_pb2.MonikerReadResponse,
    ]

    StreamWrite: grpc.StreamStreamMultiCallable[
        data_moniker_pb2.MonikerWriteRequest,
        data_moniker_pb2.StreamWriteResponse,
    ]

class DataMonikerAsyncStub:
    BeginSidebandStream: grpc.aio.UnaryUnaryMultiCallable[
        data_moniker_pb2.BeginMonikerSidebandStreamRequest,
        data_moniker_pb2.BeginMonikerSidebandStreamResponse,
    ]

    StreamReadWrite: grpc.aio.StreamStreamMultiCallable[
        data_moniker_pb2.MonikerWriteRequest,
        data_moniker_pb2.MonikerReadResponse,
    ]

    StreamRead: grpc.aio.UnaryStreamMultiCallable[
        data_moniker_pb2.MonikerList,
        data_moniker_pb2.MonikerReadResponse,
    ]

    StreamWrite: grpc.aio.StreamStreamMultiCallable[
        data_moniker_pb2.MonikerWriteRequest,
        data_moniker_pb2.StreamWriteResponse,
    ]

class DataMonikerServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def BeginSidebandStream(
        self,
        request: data_moniker_pb2.BeginMonikerSidebandStreamRequest,
        context: _ServicerContext,
    ) -> typing.Union[data_moniker_pb2.BeginMonikerSidebandStreamResponse, collections.abc.Awaitable[data_moniker_pb2.BeginMonikerSidebandStreamResponse]]: ...

    @abc.abstractmethod
    def StreamReadWrite(
        self,
        request_iterator: _MaybeAsyncIterator[data_moniker_pb2.MonikerWriteRequest],
        context: _ServicerContext,
    ) -> typing.Union[collections.abc.Iterator[data_moniker_pb2.MonikerReadResponse], collections.abc.AsyncIterator[data_moniker_pb2.MonikerReadResponse]]: ...

    @abc.abstractmethod
    def StreamRead(
        self,
        request: data_moniker_pb2.MonikerList,
        context: _ServicerContext,
    ) -> typing.Union[collections.abc.Iterator[data_moniker_pb2.MonikerReadResponse], collections.abc.AsyncIterator[data_moniker_pb2.MonikerReadResponse]]: ...

    @abc.abstractmethod
    def StreamWrite(
        self,
        request_iterator: _MaybeAsyncIterator[data_moniker_pb2.MonikerWriteRequest],
        context: _ServicerContext,
    ) -> typing.Union[collections.abc.Iterator[data_moniker_pb2.StreamWriteResponse], collections.abc.AsyncIterator[data_moniker_pb2.StreamWriteResponse]]: ...

def add_DataMonikerServicer_to_server(servicer: DataMonikerServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
````
