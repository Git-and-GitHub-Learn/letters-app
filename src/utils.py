"""Utilities to load files"""

import os

from pathlib import Path
from typing import Union, Tuple


LETTERS_PATH = Path(__file__).parents[1] / "letters"


def validate_path(path: Union[str, Path]) -> Path:
    """Validate the specified path."""

    if isinstance(path, str):
        return Path(path)
    if isinstance(path, Path):
        return path
    raise TypeError(f"{path} must be str or Path")


def letters(path: Union[str, Path] = LETTERS_PATH) -> Tuple[str]:
    """Return the list of letters in the specified folder.

    Parameters
    ----------
    path : str | Path
        Path to letters.

    Returns
    -------
    tuple :
        List of all letters in the specified folder.
    """

    path = validate_path(path)
    files = [file for file in os.listdir(path) if file.endswith(".txt")]

    return tuple(files)


def read_letter(filename: str, path: Union[str, Path] = LETTERS_PATH) -> str:
    """Return the text in the letter if this exists

    Parametters
    -----------
    file : str
        filename.
    path : str | Path
        Path to letters.

    Returns
    -------
    str :
        letter content.
    """

    path = validate_path(path)
    files = letters(path)
    if filename not in files:
        raise ValueError(f"{filename} does not exists in {path}")

    with open(path / filename, mode="r", encoding="utf-8") as file:
        content = file.read()

    return content
