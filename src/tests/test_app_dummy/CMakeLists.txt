message(STATUS "Test Application My:")

####################################################################################################
# Compilation 
####################################################################################################



# Create a hello world executable
add_executable(test_app_dummy 
    src/hello.c
)

# Link against all component libraries
target_link_libraries(test_app_dummy PRIVATE 
    uselessCmp::lib
    uselessL2Cmp::lib
    uselessL0Cmp::lib
    uselessServicesCmp::lib
)


# TODO: hack! fix this. needed includes need to come from the link target!

# Define paths based on the project structure
set(PLATFORM_PATH "${CMAKE_CURRENT_SOURCE_DIR}/../..")

# Include directories for all component headers
target_include_directories(test_app_dummy PRIVATE
    ${PLATFORM_PATH}/moduleA/l1/uselessCmp/api
    ${PLATFORM_PATH}/moduleA/l2/uselessL2Cmp/api
    ${PLATFORM_PATH}/moduleA/l0/uselessL0Cmp/api
    ${PLATFORM_PATH}/moduleA/services/uselessServicesCmp/api
)

