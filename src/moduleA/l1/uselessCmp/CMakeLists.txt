####################################################################################################
# Configuration
####################################################################################################

set(MODULE_NAME "uselessCmp")

####################################################################################################
# Source files
####################################################################################################

set(uselessCmp_SOURCES
    src/variants/${RC_VARIANT}/uselessCmp_var.c
    src/uselessCmp_platform.c
)

####################################################################################################
# Create library target
####################################################################################################

# Create a hello world executable
add_library(lib_${MODULE_NAME} STATIC 
    ${uselessCmp_SOURCES}
)

# Set output name to match makefile convention
set_target_properties(lib_${MODULE_NAME} PROPERTIES
    OUTPUT_NAME "lib_${MODULE_NAME}"
)

####################################################################################################
# Include paths for header files (converted from makefile CC_INCLUDES)
####################################################################################################

target_include_directories(lib_${MODULE_NAME} PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}/include/${RC_VARIANT}
    ${CMAKE_CURRENT_SOURCE_DIR}/include
)

# Make the API headers available to other targets that link to this library
target_include_directories(lib_${MODULE_NAME} PUBLIC
    ${CMAKE_CURRENT_SOURCE_DIR}/api
)

####################################################################################################
# Create alias for easier linking
####################################################################################################

# Create an alias that matches the library filename for easy linking
add_library(uselessCmp::lib ALIAS lib_${MODULE_NAME})


####################################################################################################
# Enable unit testing
####################################################################################################

enable_testing()

add_executable(
  uselessCmp_test
  tests/uselessCmp_test.cpp
  tests/uselessCmp_test_moduleA.cpp
)
target_link_libraries(
  uselessCmp_test
  gtest_main
  gmock
  uselessCmp::lib
)

target_include_directories(uselessCmp_test PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}/include/${RC_VARIANT}
    ${CMAKE_CURRENT_SOURCE_DIR}/include
)

include(GoogleTest)
gtest_discover_tests(uselessCmp_test
    DISCOVERY_MODE PRE_TEST
)

# Also add the test manually for CTest compatibility
add_test(
    NAME uselessCmp_unit_tests
    COMMAND uselessCmp_test
    WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
)


####################################################################################################
# Status message for build feedback
####################################################################################################

message(STATUS "Configured ${MODULE_NAME} library with ${CMAKE_CURRENT_LIST_DIR}")
message(STATUS "  - Source files: ${uselessCmp_SOURCES}")
message(STATUS "  - Config files: ${CONFIG_SOURCES}")
message(STATUS "  - Output: lib_${MODULE_NAME}.a in ${CMAKE_BINARY_DIR}/lib/")