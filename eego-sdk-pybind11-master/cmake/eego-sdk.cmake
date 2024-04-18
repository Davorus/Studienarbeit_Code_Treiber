include(FetchContent)
FetchContent_Declare(
  eego_sdk
  URL ${EEGO_SDK_ZIP}
)

FetchContent_GetProperties(eego_sdk)
if(NOT eego_sdk_POPULATED)
  FetchContent_Populate(eego_sdk)

  if(UNIX)
    if(CMAKE_SIZEOF_VOID_P EQUAL 4)
      find_library(EEGO_SDK_LIBRARY NAMES eego-SDK PATHS ${eego_sdk_SOURCE_DIR}/linux/32bit REQUIRED)
    else()
      find_library(EEGO_SDK_LIBRARY NAMES eego-SDK PATHS ${eego_sdk_SOURCE_DIR}/linux/64bit REQUIRED)
    endif()
  endif()

  if(WIN32)
    if(CMAKE_SIZEOF_VOID_P EQUAL 4)
      find_library(EEGO_SDK_LIBRARY NAMES eego-SDK PATHS ${eego_sdk_SOURCE_DIR}/windows/32bit REQUIRED)
    else()
      find_library(EEGO_SDK_LIBRARY NAMES eego-SDK PATHS ${eego_sdk_SOURCE_DIR}/windows/64bit REQUIRED)
    endif()
  endif()

  message("EEGO_SDK_ZIP........ ${EEGO_SDK_ZIP}")
  message("EEGO_SDK_LIBRARY.... ${EEGO_SDK_LIBRARY}")

  set(EEGO_SDK_ROOT ${eego_sdk_SOURCE_DIR})
endif()
