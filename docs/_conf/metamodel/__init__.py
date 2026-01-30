"""General Sphinx-Needs configuration."""

from . import arch, implementation, req, test

# extra options for all sphinx needs types
needs_extra_options = [
    *req.needs_extra_options,
    *arch.needs_extra_options,
    *implementation.needs_extra_options,
    *test.needs_extra_options,
]

# types definition for sphinx needs
needs_types = [
    *req.needs_types,
    *arch.needs_types,
    *implementation.needs_types,
    *test.needs_types,
]

# link definition for sphinx needs
needs_extra_links = [
    *req.needs_extra_links,
    *arch.needs_extra_links,
    *implementation.needs_extra_links,
    *test.needs_extra_links,
]

needs_warnings = {
    **req.needs_warnings,
    **arch.needs_warnings,
    **implementation.needs_warnings,
    **test.needs_warnings,
}


needs_statuses = [
    {"name": "draft", "description": "New/Changed"},
    {"name": "accepted", "description": "Accepted"},
    {"name": "rejected", "description": "Rejected"},
    {"name": "obsolete", "description": "Obsolete"},
]
