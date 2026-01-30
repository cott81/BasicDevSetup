"""Sphinx-Needs configuration for Test."""

# extra options for all sphinx needs types
needs_extra_options = ["code_link"]

# types definition for sphinx needs
needs_types = [
    {
        "directive": "test",
        "title": "Test Case",
        "prefix": "TC_",
        "color": "#DCB239",
        "style": "artifact",
    }
]

needs_extra_links = [
    {
        "option": "verify", 
        "incoming": "verified by", 
        "outgoing": "verifies",
        "style_start": "-",
        "style_end": "up->>",         
    },
]

needs_warnings = {
    # testcase section
    # must not have an invalid prefix
    "tc_invalid_ID_prefix": "(type == 'test' and not id.startswith('TC_',0))",
    # testcase status must not have an empty status field
    "tc_with_no_status": "(type == 'test') and (status is None or len(status) == 0)",
    # testcase must not have an invalid status
    "tc_invalid_status_sys": "(type == 'test') and (status is not None and len(status) != 0) \
        and (status not in \
        ['draft','accepted', 'rejected', 'obsolete'])",
    # testcase status must not have an empty verify field
    "tc_with_no_verify": "(type == 'test') and (verify is None or len(verify) == 0)",
}
