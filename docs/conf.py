# ruff: noqa: F405

import sys
from pathlib import Path

sys.path.insert(0, str(Path().absolute()))

from _conf.defaults import *  # noqa: F403
from _conf.needs_options import *  # noqa: F403
from _conf.theme_options import *  # noqa: F403

####
project = "Example"

# Override theme options

# You can override the logo images here if needed
# html_theme_options = {
#     "logo": {
#         "image_light": "_static/images/Orc2_TeamLogo.png",
#         "image_dark": "_static/images/Orc2_TeamLogo.png",
#     },
# }

# Set the text on the right of the logo
html_theme_options["logo"]["text"] = project

# Add sidebar logo
# html_logo = "_static/images/Orc2_TeamLogo.png"

# Add project specific extensions
extensions += [
    "breathe",
    'sphinx_codelinks', # extension to add one liners to link code to requirements
]

exclude_patterns += [
    "README.md",
    "**/README.md",
    "**/info.md",  # info.md are temp placeholder files. This exclude can perhaps later be removed
    "build",
]

## TODOs
todo_include_todos = True

master_doc = "docs/index"

# Project specific settings

_base_dir = Path(__file__).parent.absolute()

robot_base = str(GitWrapper().toplevel() / "tests")

#codelinks configuration
src_trace_config_from_toml = "src_trace.toml"
