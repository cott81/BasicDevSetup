# ruff: noqa: F405

import sys
from pathlib import Path

sys.path.insert(0, str(Path().absolute().parent))

from _conf.defaults import *  # noqa: F403
from _conf.needs_options import *  # noqa: F403
from _conf.theme_options import *  # noqa: F403

####
project = "Example (external)"

# Override theme options

# Set the text on the right of the logo
html_theme_options["logo"]["text"] = project

# Remove link to repository
html_theme_options["icon_links"] = []

# Add project specific extensions
# extensions += [
#     "breathe",
# ]
