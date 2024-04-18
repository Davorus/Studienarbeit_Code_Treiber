# eego-SDK python wrapper

python wrapper for the eego-SDK, using pybind11. The wrapper tries to follow
the eego-SDK API as much as possible. Please refer to the official eego-SDK
docs how to use the API.

## requirements
* C++ compiler that supports C++11
* cmake 3.11
* git
* python
* eego-SDK

## supported platforms
* windows(32 and 64 bit)
* linux(32 and 64 bit)

## setup
create a user.cmake file in the root of this project. Add a line pointing
to the eego-SDK zip file, like so:
```
set(EEGO_SDK_ZIP /path/to/download/eego-sdk-1.3.19.40453.zip)
```

## build
build using standard cmake. i.e. create build directory and
from there, call cmake:
```
cmake -DCMAKE_BUILD_TYPE=Release /path/to/this_project && cmake --build . --config Release
```

## running
make sure python can find the created module and the eego-SDK library, i.e.
by adjusting the PYTHONPATH and/or the library search path.
take a look at the stream.py example how to interact with the factory,
amplifier and stream objects.

The provided stream.py test program loops over each amplifier, shows the
impedances, then records 10 second of EEG into a text file. Afterwards,
it puts the amplifier in a dictionary based on its type.
At the end, the dictionary is checked, and if there are 2 or 4 amplifiers
of each type, it will run a cascaded test on these 2 or 4 amplifiers, provided
that cascading is supported in the SDK.
