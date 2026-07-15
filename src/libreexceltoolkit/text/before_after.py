from __future__ import annotations

from .engine import DelimiterMatch, find_delimiter


def _find(
    text: str,
    delimiter: str,
    instance_num: int,
    match_mode: int,
):
    """
    Internal helper that validates Excel-compatible arguments and
    delegates delimiter searching to the shared search engine.
    """

    if match_mode not in (0, 1):
        raise ValueError(
            "match_mode must be 0 (case-sensitive) or 1 (case-insensitive)"
        )

    return find_delimiter(
        text=text,
        delimiter=delimiter,
        instance=instance_num,
        case_sensitive=(match_mode == 0),
    )


def textbefore(
    text: str,
    delimiter: str,
    instance_num: int = 1,
    match_mode: int = 0,
    match_end: int = 0,
    if_not_found=None,
):
    """
    Returns the text before a specified delimiter.

    Parameters
    ----------
    text : str
        The input text.
    delimiter : str
        The delimiter to search for.
    instance_num : int, default=1
        Delimiter occurrence.
        Positive values search from the beginning.
        Negative values search from the end.
    match_mode : int, default=0
        0 = case-sensitive
        1 = case-insensitive
    match_end : int, default=0
        0 = delimiter must be found.
        1 = treat the end of the text as a delimiter.
    if_not_found :
        Value returned when the delimiter is not found.
        If omitted, a ValueError is raised.
    """

    if match_end not in (0, 1):
        raise ValueError("match_end must be 0 or 1")

    match = _find(
        text=text,
        delimiter=delimiter,
        instance_num=instance_num,
        match_mode=match_mode,
    )

    if match.found:
        return text[:match.start]

    if match_end:
        return text

    if if_not_found is not None:
        return if_not_found

    raise ValueError("Delimiter not found.")


def textafter(
    text: str,
    delimiter: str,
    instance_num: int = 1,
    match_mode: int = 0,
    match_end: int = 0,
    if_not_found=None,
):
    """
    Returns the text after a specified delimiter.

    Parameters
    ----------
    text : str
        The input text.
    delimiter : str
        The delimiter to search for.
    instance_num : int, default=1
        Delimiter occurrence.
        Positive values search from the beginning.
        Negative values search from the end.
    match_mode : int, default=0
        0 = case-sensitive
        1 = case-insensitive
    match_end : int, default=0
        0 = delimiter must be found.
        1 = treat the end of the text as a delimiter.
    if_not_found :
        Value returned when the delimiter is not found.
        If omitted, a ValueError is raised.
    """

    if match_end not in (0, 1):
        raise ValueError("match_end must be 0 or 1")

    match = _find(
        text=text,
        delimiter=delimiter,
        instance_num=instance_num,
        match_mode=match_mode,
    )

    if match.found:
        return text[match.end:]

    if match_end:
        return ""

    if if_not_found is not None:
        return if_not_found

    raise ValueError("Delimiter not found.")