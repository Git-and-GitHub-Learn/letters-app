"""Main UI for Shiny App"""

from shiny import ui


ui = ui.page_auto(
    ui.row(ui.h1("Letters App")),
    ui.row(ui.p("Read your letters here.")),
    ui.row(
        ui.input_select(
            id="file_select",
            label="Select a letter",
            choices=["Sebástian", "Andrés", "Narváez"],
        ),
    ),
    ui.row(
        ui.card(
            ui.output_text(id="letter"),
        ),
    ),
)
