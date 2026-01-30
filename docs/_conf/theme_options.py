from pathlib import Path

from .utils import GitWrapper

_base_dir = Path(__file__).parent.parent.absolute()

# Add any paths that contain templates here, relative to this directory.
templates_path = [str(_base_dir / "_templates")]

# -- Options for HTML output -------------------------------------------------

html_theme = "pydata_sphinx_theme"

html_static_path = [
    str(_base_dir / "_static"),
]

html_css_files = [
    "css/project_custom.css",
]

html_favicon = str(_base_dir / "_static/images/favicon.ico")

html_theme_options = {
    "use_edit_page_button": False,
    "header_links_before_dropdown": 6,
    "show_prev_next": False,
    "navbar_align": "content",
    "navbar_start": ["navbar-logo"],
    "navbar_center": ["navbar-nav"],
    "navbar_persistent": ["search-button"],
    "footer_start": ["copyright"],
    "footer_end": ["project-version.html"],
    "logo": {
        "image_light": str(_base_dir / "_static/images/genetic-algorithm-svgrepo-com.svg"),
        "image_dark": str(_base_dir / "_static/images/genetic-algorithm-svgrepo-com.svg"),
    },
    "icon_links": [
        {
            "name": "GitHub",
            "url": GitWrapper().url(),  # required
            "icon": "fa-brands fa-github",
            "type": "fontawesome",
        },
    ],
}

html_sidebars = {"**": ["project-logo", "sidebar-nav-bs"]}

html_context = {
    "default_mode": "light",
}


html_copy_source = False
html_show_sphinx = False
html_show_copyright = True
html_show_search_summary = True
html_scaled_image_link = True
