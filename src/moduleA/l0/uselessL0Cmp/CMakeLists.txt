####################################################################################################
# Configuration
####################################################################################################

set(MODULE_NAME "uselessL0Cmp")

####################################################################################################
# Source files
####################################################################################################

set(uselessL0Cmp_SOURCES
    src/variants/${RC_VARIANT}/uselessL0Cmp_var.c
    src/uselessL0Cmp_platform.c
)

####################################################################################################
# Create library target
####################################################################################################

# Create a hello world executable
add_library(lib_${MODULE_NAME} STATIC 
    ${uselessL0Cmp_SOURCES}
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
add_library(uselessL0Cmp::lib ALIAS lib_${MODULE_NAME})


####################################################################################################
# Enable unit testing
####################################################################################################

enable_testing()

add_executable(
  uselessL0Cmp_test
  tests/uselessL0Cmp_test.cpp
  tests/uselessL0Cmp_test_moduleA.cpp
)
target_link_libraries(
  uselessL0Cmp_test
  gtest_main
)

include(GoogleTest)
gtest_discover_tests(uselessL0Cmp_test
    DISCOVERY_MODE PRE_TEST
)

# Also add the test manually for CTest compatibility
add_test(
    NAME uselessL0Cmp_unit_tests
    COMMAND uselessL0Cmp_test
    WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
)


####################################################################################################
# Status message for build feedback
####################################################################################################

message(STATUS "Configured ${MODULE_NAME} library with ${CMAKE_CURRENT_LIST_DIR}")
message(STATUS "  - Source files: ${uselessL0Cmp_SOURCES}")
message(STATUS "  - Config files: ${CONFIG_SOURCES}")
message(STATUS "  - Output: lib_${MODULE_NAME}.a in ${CMAKE_BINARY_DIR}/lib/")