###################################################################################################
# Build Dependencies for  VARIANTY variant
###################################################################################################


# build l1 lib: uselessCmp
add_subdirectory(${CMAKE_SOURCE_DIR}/src/moduleA/l1/uselessCmp lib/uselessCmp)

# build l2 lib: uselessL2Cmp
add_subdirectory(${CMAKE_SOURCE_DIR}/src/moduleA/l2/uselessL2Cmp lib/uselessL2Cmp)

# build l0 lib: uselessL0Cmp
add_subdirectory(${CMAKE_SOURCE_DIR}/src/moduleA/l0/uselessL0Cmp lib/uselessL0Cmp)

# build services lib: uselessServicesCmp
add_subdirectory(${CMAKE_SOURCE_DIR}/src/moduleA/services/uselessServicesCmp lib/uselessServicesCmp)


###################################################################################################
# Build  VARIANTY Test Application 
###################################################################################################

add_subdirectory(${CMAKE_SOURCE_DIR}/src/tests/test_app_dummy test_appl_dummy)


###################################################################################################
# Build  Documentation
###################################################################################################

add_subdirectory(${CMAKE_SOURCE_DIR}/docs docs)