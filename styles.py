BIG_FONT_SIZE = 40
MEDIUM_FONT_SIZE = 24
SMALL_FONT_SIZE = 18

TEXT_MARGIN = 13

MINIMUM_WIDTH = 450

PRIMARY_COLOR = '#1e81b0'
DARKER_PRIMARY_COLOR = '#16658a'
DARKEST_PRIMARY_COLOR = '#115270'

import qdarktheme

qss = f"""
    QPushButton[cssClass="specialButton"] {{
        color: #fff;
        background: {PRIMARY_COLOR};
    }}
    QPushButton[cssClass="specialButton"]:hover {{
        color: #fff;
        background: {DARKER_PRIMARY_COLOR};
    }}
    QPushButton[cssClass="specialButton"]:pressed {{
        color: #fff;
        background: {DARKEST_PRIMARY_COLOR};
    }}
"""

def changeTheme():
    qdarktheme.setup_theme(theme='dark', corner_shape='rounded', custom_colors={
        "[dark]": {
            "primary": "#1e81b0"
        },
        "[light]": {
            "primary": "1e81b0"
        }}, additional_qss=qss)
