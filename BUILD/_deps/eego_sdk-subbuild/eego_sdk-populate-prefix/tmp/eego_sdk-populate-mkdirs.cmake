# Distributed under the OSI-approved BSD 3-Clause License.  See accompanying
# file Copyright.txt or https://cmake.org/licensing for details.

cmake_minimum_required(VERSION 3.5)

file(MAKE_DIRECTORY
  "C:/Users/david/Desktop/DEMO_SDK/BUILD/_deps/eego_sdk-src"
  "C:/Users/david/Desktop/DEMO_SDK/BUILD/_deps/eego_sdk-build"
  "C:/Users/david/Desktop/DEMO_SDK/BUILD/_deps/eego_sdk-subbuild/eego_sdk-populate-prefix"
  "C:/Users/david/Desktop/DEMO_SDK/BUILD/_deps/eego_sdk-subbuild/eego_sdk-populate-prefix/tmp"
  "C:/Users/david/Desktop/DEMO_SDK/BUILD/_deps/eego_sdk-subbuild/eego_sdk-populate-prefix/src/eego_sdk-populate-stamp"
  "C:/Users/david/Desktop/DEMO_SDK/BUILD/_deps/eego_sdk-subbuild/eego_sdk-populate-prefix/src"
  "C:/Users/david/Desktop/DEMO_SDK/BUILD/_deps/eego_sdk-subbuild/eego_sdk-populate-prefix/src/eego_sdk-populate-stamp"
)

set(configSubDirs Debug)
foreach(subDir IN LISTS configSubDirs)
    file(MAKE_DIRECTORY "C:/Users/david/Desktop/DEMO_SDK/BUILD/_deps/eego_sdk-subbuild/eego_sdk-populate-prefix/src/eego_sdk-populate-stamp/${subDir}")
endforeach()
if(cfgdir)
  file(MAKE_DIRECTORY "C:/Users/david/Desktop/DEMO_SDK/BUILD/_deps/eego_sdk-subbuild/eego_sdk-populate-prefix/src/eego_sdk-populate-stamp${cfgdir}") # cfgdir has leading slash
endif()
