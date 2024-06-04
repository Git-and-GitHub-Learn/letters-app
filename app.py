"""Main App"""

from shiny import App

from src.ui import ui
from src.server import server

app = App(ui, server)
