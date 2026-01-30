# Documentation build configuration
set(MODULE_NAME "SW_Docu")

set(SPHINXOPTS "-W")
set(SOURCEDIR ".")
set(BUILDDIR "_build")
set(BUILDDIR_INTERNAL "${BUILDDIR}/internal")
set(BUILDDIR_EXTERNAL "${BUILDDIR}/external")

# Get number of processors for parallel builds
include(ProcessorCount)
ProcessorCount(NPROC)
if(NPROC EQUAL 0)
    set(NPROC 1)
endif()

# Doxygen XML target (placeholder)
add_custom_target(docs-doxygen_xml
    COMMENT "Generating Doxygen XML"
)

# HTML documentation target
add_custom_target(docs-html
    COMMAND /tmp/venv/bin/uv run sphinx-build -j ${NPROC} -b html "${SOURCEDIR}" "${BUILDDIR_INTERNAL}" ${SPHINXOPTS}
    WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
    DEPENDS docs-doxygen_xml
    COMMENT "Building internal HTML documentation"
)

# # External HTML documentation target  
# add_custom_target(external
#     COMMAND uv run sphinx-build -j ${NPROC} -b html "${SOURCEDIR}/external" "${BUILDDIR_EXTERNAL}" ${SPHINXOPTS}
#     WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
#     DEPENDS docs-doxygen_xml
#     COMMENT "Building external HTML documentation"
# )

# Live reload for internal docs
add_custom_target(docs-live
    COMMAND uv run sphinx-autobuild --port=8338 "${SOURCEDIR}" "${BUILDDIR_INTERNAL}/html"
    WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
    DEPENDS docs-doxygen_xml
    COMMENT "Starting live reload server for internal documentation"
)

# # Live reload for external docs
# add_custom_target(external-live
#     COMMAND uv run sphinx-autobuild --port=8338 "${SOURCEDIR}/external/" "${BUILDDIR_EXTERNAL}/html"
#     WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
#     DEPENDS docs-doxygen_xml
#     COMMENT "Starting live reload server for external documentation"
# )

# Clean build directory
add_custom_target(docs-clean
    COMMAND ${CMAKE_COMMAND} -E remove_directory "${BUILDDIR}"
    WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
    COMMENT "Cleaning documentation build directory"
)

####################################################################################################
# Status message for build feedback
####################################################################################################

message(STATUS "Configured ${MODULE_NAME} with ${CMAKE_CURRENT_LIST_DIR}")
message(STATUS "  - Source files: ${SOURCEDIR}")
message(STATUS "  - Config files: ${CONFIG_SOURCES}")
message(STATUS "  - Output: ${BUILDDIR}")