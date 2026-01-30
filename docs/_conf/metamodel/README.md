# Metamodel Documentation

This folder contains the configuration of the Sphinx-Needs metamodel used throughout the documentation. The metamodel
defines the structure and relationships between different types of needs (requirements, architecture elements,
implementation elements, and test cases).

## Need Types Overview

The metamodel defines the following need types:

### Requirements

| Directive | Title | Prefix |
|-----------|-------|--------|
| `req-sh` | Stakeholder Requirement | REQ_SH_ |
| `req-sys` | System Requirement | REQ_SYS_ |
| `req-sw` | Software Requirement | REQ_SW_ |

### Architecture

| Directive | Title | Prefix |
|-----------|-------|--------|
| `arch-composite` | Software Composite | ARCH_SW_ |
| `arch-swc` | Software Component | SWC_ |

### Implementation

| Directive | Title | Prefix |
|-----------|-------|--------|
| `impl` | Implementation | IMPL_ |

### Test

| Directive | Title | Prefix |
|-----------|-------|--------|
| `test` | Test Case | TC_ |

## Extra Options

Different need types support additional options to provide more specific information:

### Requirements Extra Options

| Option | Description | Applicable to |
|--------|-------------|---------------|
| `safety_integrity` | Safety integrity level | req-sh, req-sys, req-sw |
| `security_relevance` | Security relevance flag | req-sh, req-sys, req-sw |
| `legal_relevance` | Legal requirement | req-sh, req-sys, req-sw |
| `verification_method` | Method used to verify the requirement | req-sh, req-sys, req-sw |
| `verification_criteria` | Criteria for successful verification | req-sh, req-sys, req-sw |

### Architecture Extra Options

| Option | Description | Applicable to |
|--------|-------------|---------------|
| `ram_budget` | RAM allocation budget | arch-composite, arch-swc |
| `rom_budget` | ROM allocation budget | arch-composite, arch-swc |
| `cpu_budget` | CPU resource allocation budget | arch-composite, arch-swc |
| `cpu_allocation` | Actual CPU resource allocation | arch-composite, arch-swc |

## Link Types

The metamodel defines various link types to establish relationships between needs:

| Link Option | From → To Direction | To → From Direction | Description |
|-------------|---------------------|---------------------|-------------|
| `satisfies` | satisfies | satisfied by | Links to upper level requirements |
| `part_of` | part of | parts | Links architecture elements to show composition |
| `specified_by` | specified by | specifies | Links architecture to requirements |
| `implements` | implements | implemented by | Links implementation to requirements |
| `design` | designed by | design for | Links implementation to architecture |
| `verify` | verifies | verified by | Links test cases to requirements |

## Status

All needs can have one of the following statuses:

| Status | Description |
|--------|-------------|
| `draft` | New/Changed |
| `accepted` | Accepted |
| `rejected` | Rejected |
| `obsolete` | Obsolete |

## Validation Rules

The metamodel enforces several validation rules to ensure process compliance:

### Requirements Validation

| Rule | Description | Valid Values |
|------|-------------|-------------|
| `req_with_no_status` | Requirements must have a status | Any non-empty status |
| `req_invalid_status` | Requirements must have a valid status | draft, accepted, rejected, obsolete |
| `req_with_no_safety` | Requirements with "accepted" status must define safety integrity | Any non-empty safety_integrity |
| `req_invalid_safety` | Safety integrity must have a valid value | QM, ASIL_A, ASIL_B, ASIL_C, ASIL_D, PL-a, PL-b, PL-c, PL-d, PL-e,  |
| `req_accepted_req_with_no_verification_criteria` | Requirements with "accepted" status must define verification criteria | Any non-empty verification_criteria |
| `req_security_relevance_not set` | Requirements must define security relevance | Any non-empty security_relevance |
| `req_invalid_value_for_security_relevance` | Security relevance must have a valid value | yes, no |
| `req_invalid_value_for_legal_relevance` | Legal relevance must have a valid value | yes, no |
| `req_valid_ID_prefix` | Requirements must use the correct ID prefix | REQ_SW_ for software requirements, REQ_SYS_ for system requirements. REQ_SH_ for stakeholder requirements |

### Architecture Validation

| Rule | Description | Valid Values |
|------|-------------|-------------|
| `arch_invalid_ID_prefix` | Software components must use the correct ID prefix | SWC_ |
| `arch_composite_invalid_ID_prefix` | Software composites must use the correct ID prefix | ARCH_SW_ |
| `arch_with_no_status` | Software components must have a status | Any non-empty status |
| `arch_invalid_status` | Software components must have a valid status | draft, accepted, rejected, obsolete |
| `arch_with_no_requirement` | Software components must be linked to requirements | Any non-empty specified_by |

### Implementation Validation

| Rule | Description | Valid Values |
|------|-------------|-------------|
| `impl_invalid_ID_prefix` | Implementation must use the correct ID prefix | IMPL_ |
| `impl_with_no_status` | Implementation must have a status | Any non-empty status |
| `impl_invalid_status` | Implementation must have a valid status | draft, accepted, rejected, obsolete |
| `impl_with_no_requirement` | Implementation must be linked to requirements | Any non-empty implements |
| `impl_with_no_architecture` | Implementation must be linked to architecture | Any non-empty design |

### Test Validation

| Rule | Description | Valid Values |
|------|-------------|-------------|
| `tc_invalid_ID_prefix` | Test cases must use the correct ID prefix | TC_ |
| `tc_with_no_status` | Test cases must have a status | Any non-empty status |
| `tc_invalid_status_sys` | Test cases must have a valid status | draft, accepted, rejected, obsolete |
| `tc_with_no_verify` | Test cases must be linked to requirements | Any non-empty verify |

## Examples

In RST:

```rst
.. req-sys::
   :id: REQ_SYS_EXAMPLE_2345
   :tags: example
   :status: accepted
   :safety_integrity: QM
   :security_relevance: no
   :verification_criteria: Review of the requirements specification.

   The API shall allow access to X.
```

```rst
.. req-sw::
   :id: REQ_SW_EXAMPLE_2345
   :tags: example
   :status: accepted
   :safety_integrity: QM
   :security_relevance: no
   :satisfies: REQ_SYS_EXAMPLE_2345
   :verification_criteria: Review of the requirements specification.

   The API shall allow access to X.
```

In Markdown:

```rst
:::{req-sys}
:id: REQ_SYS_EXAMPLE_3456
:tags: example
:status: accepted
:safety_integrity: QM
:security_relevance: no
:verification_criteria: Review of the requirements specification.

The API shall allow access to X.
:::
```

```rst
:::{req-sw}
:id: REQ_SW_EXAMPLE_3456
:tags: example
:status: accepted
:safety_integrity: QM
:security_relevance: no
:satisfies: REQ_SYS_EXAMPLE_3456
:verification_criteria: Review of the requirements specification.

The API shall allow access to X.
:::
```
