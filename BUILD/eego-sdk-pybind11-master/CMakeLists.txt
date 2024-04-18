cmake_minimum_required(VERSION 3.11)

project(eego-sdk-pybind11)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_POSITION_INDEPENDENT_CODE ON)

include(user.cmake)
include(cmake/eego-sdk.cmake)
include(cmake/pybind11.cmake)

add_subdirectory(python2)
add_subdirectory(python3)
