"""Sphinx-Needs configuration for Architecture."""

# extra options for all sphinx needs types
needs_extra_options = [
    "ram_budget",
    "rom_budget",
    "cpu_budget",
    "cpu_allocation",
]

# types definition for sphinx needs
needs_types = [
    {
        "directive": "arch-composite",
        "title": "Software Composite",
        "prefix": "ARCH_SW_",
        "color": "#BFFFD2",
        "style": "collections",
    },
    {
        "directive": "arch-swc",
        "title": "Software Component",
        "prefix": "SWC_",
        "color": "#BFD8D2",
        "style": "component",
    },
]

needs_extra_links = [
    {
        "option": "part_of", 
        "incoming": "parts", 
        "outgoing": "part of"
    },
    {
        "option": "specified_by",
        "incoming": "specifies",
        "outgoing": "specified by",
        "style_start": "-",
        "style_end": "up->>",
    },
]

needs_warnings = {
    # must not have an invalid prefix
    "arch_invalid_ID_prefix": "(type == 'arch-swc' and not id.startswith('SWC_',0))",
    "arch_composite_invalid_ID_prefix": "(type == 'arch-composite' and not id.startswith('ARCH_SW_',0))",
    # implementation status must not have an empty status field
    "arch_with_no_status": "(type == 'arch-swc') and (status is None or len(status) == 0)",
    # implementation must not have an invalid status
    "arch_invalid_status": "(type == 'arch-swc') and (status is not None and len(status) != 0) \
        and (status not in \
        ['draft','accepted', 'rejected', 'obsolete'])",
    # traceability checks
    "arch_with_no_requirement": "(type == 'arch-swc') and (specified_by is None or len(specified_by) == 0)",
    # "arch_with_no_implementation": "(type == 'arch-swc') and (implements_back is None or len(implements_back) == 0)",
}
