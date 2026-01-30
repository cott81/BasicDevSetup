from . import metamodel
from .utils import GitWrapper

needs_build_json = True
needs_reproducible_json = True
needs_title_optional = True
needs_id_required = True
needs_extra_options = metamodel.needs_extra_options
needs_types = metamodel.needs_types
needs_extra_links = metamodel.needs_extra_links
needs_statuses = metamodel.needs_statuses
needs_warnings = metamodel.needs_warnings

needs_default_style = "discreet"

# Link to code in GitHub
_github_blob_url = f"{GitWrapper().url()}/blob/{GitWrapper().commit()}/"

needs_string_links = {
    "code_link": {
        "regex": r"^(?P<value>.+)$",
        "link_url": _github_blob_url + "{{value}}",
        "link_name": "{{value}}",
        "options": ["code_link"],
    },
}
