from shiny import App

from ui import ui
from server import server

app = App(ui, server)
