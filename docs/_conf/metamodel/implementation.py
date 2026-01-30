"""Sphinx-Needs configuration for Implementation."""

needs_extra_options = []

# types definition for sphinx needs
needs_types = [
    {
        "directive": "impl",
        "title": "Implementation",
        "prefix": "IMPL_",
        "color": "#8DD2FF",
        "style": "rectangle",
    },
]

needs_extra_links = [
    {
        "option": "implements",
        "incoming": "implemented by", 
        "outgoing": "implements",
        "style_start": "-",
        "style_end": "up->>",
    },
    {
        "option": "design", 
        "incoming": "design for", 
        "outgoing": "designed by",
        "style_start": "-",
        "style_end": "up->>",        
    },
]

needs_warnings = {
    # must not have an invalid prefix
    "impl_invalid_ID_prefix": "(type == 'impl' and not id.startswith('IMPL_',0))",
    # implementation status must not have an empty status field
    "impl_with_no_status": "(type == 'impl') and (status is None or len(status) == 0)",
    # implementation must not have an invalid status
    "impl_invalid_status": "(type == 'impl') and (status is not None and len(status) != 0) \
        and (status not in \
        ['draft','accepted', 'rejected', 'obsolete'])",
    # implementation status must not have an empty implements field
    "impl_with_no_requirement": "(type == 'impl') and (implements is None or len(implements) == 0)",
    # implementation status must not have an empty implements field
    "impl_with_no_architecture": "(type == 'impl') and (design is None or len(design) == 0)",
}
