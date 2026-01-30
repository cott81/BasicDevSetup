"""Sphinx-Needs configuration for Requirements."""

needs_extra_options = [
    "safety_integrity",
    "security_relevance",
    "legal_relevance",
    "verification_method",
    "verification_criteria",
    "feature",
]

needs_types = [
    {
        "directive": "req-sh",
        "title": "Stakeholder Requirement",
        "prefix": "REQ_SH_",
        "color": "#8FAADC",
        "style": "artifact",
    },
    {
        "directive": "req-sys",
        "title": "System Requirement",
        "prefix": "REQ_SYS_",
        "color": "#F5B700",
        "style": "artifact",
    },
    {
        "directive": "req-sw",
        "title": "Software Requirement",
        "prefix": "REQ_SW_",
        "color": "#6CC24A",
        "style": "artifact",
    },
]

needs_extra_links = [
    {
        "option": "satisfies", 
        "incoming": "satisfied by", 
        "outgoing": "satisfies",
        "style_start": "-",
        "style_end": "up->>",        
    },
]


needs_warnings = {
    # req must not have an empty status field
    "req_with_no_status": "(type == 'req-sw' or type == 'req-sys' or type == 'req-sh') \
        and (status is None or len(status) == 0)",
    # req must not have an invalid status
    "req_invalid_status": "(type == 'req-sw' or type == 'req-sys' or type == 'req-sh') \
        and (status is not None and len(status) != 0) \
        and (status not in ['draft','accepted','obsolete','rejected'])",
    # req must not have an empty safety field if status is submitted or agreed
    "req_with_no_safety": "(type == 'req-sw' or type == 'req-sys') and (status == 'accepted') \
        and (safety_integrity is None or len(safety_integrity) == 0)",
    # req must not have an invalid safety value
    "req_invalid_safety": "(type == 'req-sw' or type == 'req-sys') and \
        (safety_integrity is not None and len(safety_integrity) != 0) and \
        (safety_integrity not in ['QM','ASIL_A','ASIL_B','ASIL_C','ASIL_D', 'PL-a''PL-b', 'PL-c', 'PL-d', 'PL-e'])",
    # req must not have an empty verification_criteria field if status is submitted or agreed
    "req_accepted_req_with_no_verification_criteria": "(type == 'req-sw' or type == 'req-sys') \
        and (status == 'accepted') \
          and (verification_criteria is None or len(verification_criteria) == 0)",
    # req must have security value
    "req_security_relevance_not set": "(type == 'req-sw' or type == 'req-sys') and \
        (security_relevance is None or len(security_relevance) == 0)",
    # req must not have invalid security value
    "req_invalid_value_for_security_relevance": "(type == 'req-sw' or type == 'req-sys') and \
        (security_relevance not in ['yes', 'no'])",
    # req must have valid legal value
    "req_invalid_value_for_legal_relevance": "(type == 'req-sw' or type == 'req-sys') and \
        (legal_relevance is not None and len(legal_relevance) != 0) and \
        (legal_relevance not in ['yes', 'no'])",
    # req must have valid prefix
    "req_valid_ID_prefix": "(type == 'req-sw' and not id.startswith('REQ_SW_',0)) \
        or (type == 'req-sys' and not id.startswith('REQ_SYS_',0)) \
        or (type == 'req-sh' and not id.startswith('REQ_SH_',0))",
    # req must define status
    "req_with_wrong_status_attribute": "(type == 'req-sw' or type == 'req-sys' or type == 'req-sh') \
        and status is None",
}
