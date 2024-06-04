"""Utilities to load files."""

import os
import pathlib

from typing import Optional, Union, Tuple


LETTERS_PATH = pathlib.Path(__file__).parents[1] / "letters"


def validate_path(path: Optional[Union[str, pathlib.Path]]) -> pathlib.Path:
    """Validate the specified path."""

    if isinstance(path, str):
        return pathlib.Path(path)
    elif isinstance(path, pathlib.Path):
        return path
    else:
        raise TypeError(f"{path} must be str or pathlib.Path")


def letters(path: Optional[Union[str, pathlib.Path]] = LETTERS_PATH) -> Tuple[str]:
    """Return the list of letters in the specified folder.

    Parameters
    ----------
    path : str | pathlib.Path (Optional)
        Path to letters.

    Returns
    -------
    tuple :
        List of all letters in the specified folder.
    """

    path = validate_path(path)
    files = [file for file in os.listdir(path) if file.endswith(".txt")]

    return tuple(files)


def read_letter(
    filename: str, path: Optional[Union[str, pathlib.Path]] = LETTERS_PATH
) -> str:
    """Return the text in the letter if this exists

    Parametters
    -----------
    file : str
        filename.
    path : str | pathlib.Path (Optional)
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


if __name__ == "__main__":
    some_files = letters()
    one_file = some_files[0]
    print(read_letter(one_file))
