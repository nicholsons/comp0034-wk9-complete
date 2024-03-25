# Page with the map and stats card
from dash import register_page
import dash_bootstrap_components as dbc
from dash_multi import layout_events

# register the page in the app
register_page(__name__, name='Events', title='Events', path="/", )

# The rows are in a separate Python module called layout_events.py
layout = dbc.Container([
    layout_events.row_one,
    layout_events.row_two,
])
