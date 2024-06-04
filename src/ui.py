"""Main UI for Shiny App"""

from shiny import ui

from src.utils import letters


ui = ui.page_auto(
    ui.row(ui.h1("Letters App")),
    ui.row(ui.p("Read your letters here.")),
    ui.row(
        ui.input_select(
            id="file_select",
            label="Select a letter",
            choices=letters(),
        ),
    ),
    ui.row(
        ui.card(
            ui.output_text_verbatim(id="letter"),
        ),
    ),
)
