# Distributed under the OSI-approved BSD 3-Clause License.  See accompanying
# file Copyright.txt or https://cmake.org/licensing for details.

cmake_minimum_required(VERSION 3.26.4)

# We name the project and the target for the ExternalProject_Add() call
# to something that will highlight to the user what we are working on if
# something goes wrong and an error message is produced.

project(eego_sdk-populate NONE)



include(ExternalProject)
ExternalProject_Add(eego_sdk-populate
                     "UPDATE_DISCONNECTED" "False" "DOWNLOAD_EXTRACT_TIMESTAMP" "TRUE" "URL" "C:/Users/david/Desktop/DEMO_SDK/BUILD/eego_sdk.zip"
                    SOURCE_DIR          "C:/Users/david/Desktop/DEMO_SDK/BUILD/_deps/eego_sdk-src"
                    BINARY_DIR          "C:/Users/david/Desktop/DEMO_SDK/BUILD/_deps/eego_sdk-build"
                    CONFIGURE_COMMAND   ""
                    BUILD_COMMAND       ""
                    INSTALL_COMMAND     ""
                    TEST_COMMAND        ""
                    USES_TERMINAL_DOWNLOAD  YES
                    USES_TERMINAL_UPDATE    YES
                    USES_TERMINAL_PATCH     YES
)


