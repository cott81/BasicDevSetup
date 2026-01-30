from .utils import GitWrapper

####

author = "Dominik Kirchner"
copyright = f"{author} %Y, all rights reserved"  # noqa: A001

# The full version, including alpha/beta/rc tags
release = GitWrapper().describe(tags=True, always=True, dirty=True, match="v*")
version = release


extensions = [
    "myst_parser",
    "sphinx_copybutton",
    "sphinx.ext.duration",
    "sphinx.ext.todo",
    "sphinxcontrib.plantuml",
    "sphinx_needs",
    "sphinx_design",
]

nitpicky = True

exclude_patterns = [
    "_build",
    "_conf",
    "[.]*",
]

## PlantUML
plantuml = 'java -Djava.awt.headless=true -jar /usr/share/plantuml/plantuml.jar'
plantuml_output_format = "svg"

# Myst
myst_enable_extensions = ["colon_fence", "attrs_inline"]
myst_heading_anchors = 4


# new layout for test-cases
needs_layouts = {
"project-default": {
    "grid": "simple",
    "layout": {
        "head": [
            '<<meta("type_name")>>: **<<meta("title")>>** <<meta_id()>> <<collapse_button("meta", '
            'collapsed="icon:arrow-down-circle", visible="icon:arrow-right-circle", initial=True)>>'
        ],
        "meta": [
            '**Type:** <<meta("type_name")>>',
            '**ID:** <<meta("id")>>',
            "<<meta_links_all()>>",
        ],
    },
},
"project-requirement": {
    "grid": "simple",
    "layout": {
        "head": [
            '**<<meta("title")>>** <<meta_id()>> <<collapse_button("meta", '
            'collapsed="icon:arrow-down-circle", visible="icon:arrow-right-circle", initial=True)>>'
        ],
        "meta": [
            '**Type:** <<meta("type_name")>>',
            '**ID:** <<meta("id")>>',
            '**Status:** <<meta("status")>>',
            "<<meta_links_all()>>",
        ],
    },
},
"project-requirement-side": {
    "grid": "simple_side_right_partial",
    "layout": {
        "head": [
            '**<<meta("title")>>** <<collapse_button("meta", '
            'collapsed="icon:arrow-down-circle", visible="icon:arrow-right-circle", initial=True)>>'
        ],
        "meta": [
            '**Type:** <<meta("type_name")>>',
            '**ID:** <<meta("id")>>',
            '**Status:** <<meta("status")>>',
            "<<meta_links_all()>>",
        ],
        "side": [
            '<<meta("status")>>'
        ],
    },
},
"project-requirement-complex": {
    "grid": "complex",
    "layout": {
        "head_left": [
            '**<<meta("title")>>** '
        ],
        "head_right": [
            '**Status:** <<meta("status")>> '
            '<<collapse_button("meta", collapsed="icon:arrow-down-circle", visible="icon:arrow-right-circle", initial=True)>>',
        ],
        "meta_left": [
            '**Type:** <<meta("type_name")>>',
            '**ID:** <<meta("id")>>',
            '**Status:** <<meta("status")>>',
            '**Remote URL:** <<meta("remote-url")>>',
        ],
        "meta_right": [
            "<<meta_links_all()>>",
        ],
        "footer_left": [
        ],
        "footer": [
        ],
        "footer_right": [
        ],

    },
},

}

# set the default layout for all needs
needs_default_layout = 'project-requirement-complex'