
cmake_minimum_required(VERSION 3.14)

####################################################################################################
# Toolchain Handling - MUST BE BEFORE project()
####################################################################################################


message("Toolchain Configuration:")

if(NOT DEFINED CMAKE_TOOLCHAIN_FILE OR CMAKE_TOOLCHAIN_FILE STREQUAL "")
    set(CMAKE_TOOLCHAIN_FILE "${CMAKE_CURRENT_SOURCE_DIR}/cmake/toolchains/win-gcc-x86-64.cmake" CACHE FILEPATH "Default toolchain file" FORCE)
    message(STATUS "Toolchain: ${CMAKE_TOOLCHAIN_FILE} (No CMAKE_TOOLCHAIN_FILE specified or empty, using default) ")
else()
    message(STATUS "Toolchain: ${CMAKE_TOOLCHAIN_FILE} (User-specified CMAKE_TOOLCHAIN_FILE)")
endif()

# NOW call project() - will use the toolchain file
project(basic_dev_setup C CXX) 

message("\n")

####################################################################################################
# Dev Dependency Management
####################################################################################################

# control variables for dev dependencies management
option(USE_CERTIFIED_GTEST "Use certified Google Test" OFF)

message("Dev Dependency Management:")

    message(STATUS "Unit Test Framework: Using Google Test default version")
    #GoogleTest requires at least C++17
    set(CMAKE_CXX_STANDARD 17)
    set(CMAKE_CXX_STANDARD_REQUIRED ON)

    include(FetchContent)
    FetchContent_Declare(
        googletest
        # use gtest release v1.17.0 (latest as of Nov 2025)
        URL https://github.com/google/googletest/archive/refs/tags/v1.17.0.zip
        # avoid unnecessary rebuilds, follow cmake warning advice
        DOWNLOAD_EXTRACT_TIMESTAMP true
    )
    # For Windows: Prevent overriding the parent project's compiler/linker settings
    set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
    FetchContent_MakeAvailable(googletest)

message("\n")

####################################################################################################
# Enable Testing at Project Level
####################################################################################################

# Enable testing must be called from the top-level CMakeLists.txt for CTest to work properly
enable_testing()

####################################################################################################
# Variant Handling
####################################################################################################

message("Variant Configuration:")

# Allow override via environment variables or CMake cache
if(DEFINED ENV{RC_VARIANT})
    message(STATUS "Variant: $ENV{RC_VARIANT} (from environment variable RC_VARIANT)")
    set(VARIANT "$ENV{RC_VARIANT}")
elseif(DEFINED RC_VARIANT AND NOT RC_VARIANT STREQUAL "")
    message(STATUS "Variant: ${RC_VARIANT} (from CMake variable RC_VARIANT)")
    set(VARIANT "${RC_VARIANT}")
else()
    set(VARIANT "variantX")
    message(STATUS "Variant: ${VARIANT} (default)")
endif()

message(STATUS "Variant Features: ... TODO: list of activated features / components ... ")

message("\n")

####################################################################################################
# Project Configuration
####################################################################################################

message("Project Configuration:")
if(DEFINED VARIANT)
    if(VARIANT STREQUAL "variantX")
        include(${CMAKE_CURRENT_SOURCE_DIR}/cmake/variants/variant_variantX.cmake)
    elseif(VARIANT STREQUAL "variantY")        
        include(${CMAKE_CURRENT_SOURCE_DIR}/cmake/variants/variant_variantY.cmake)
    else()
        message(FATAL_ERROR "Unknown VARIANT: ${VARIANT}. No specific configuration included.")
    endif()
else()
    message(FATAL_ERROR "VARIANT is not defined. Please set the RC_VARIANT environment variable or define VARIANT in the CMake cache.")
endif()



