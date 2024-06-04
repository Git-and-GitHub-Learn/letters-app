"""Server function to handle reacitivity"""

from shiny import Inputs, render

from src.utils import read_letter


def server(inputs: Inputs):
    """Main Server function for Shiny App.

    Parameters
    ----------
    inputs : shiny.Inputs
        Shiny App inputs.
    """

    @render.text
    def letter() -> str:
        letter = inputs.file_select()
        content = read_letter(letter)
        return content
