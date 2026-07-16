from __future__ import annotations
from typing import Any
from .engine import DelimiterMatch, find_delimiter


def _validate(
    text: str,
    col_delimiter: str,
    row_delimiter: str | None,
    ignore_empty: bool,
    match_mode: int,
) -> None:
    """
    Internal helper that validates Excel-compatible arguments and
    delegates delimiter searching to the shared search engine.
    """
    if not isinstance(text, str):
        raise TypeError("Selected text must be a string")

    if not isinstance(col_delimiter, str):
        raise TypeError("Column delimiter must be a string")

    if row_delimiter is not None and not isinstance(row_delimiter, str):
        raise TypeError("Row delimiter must be a string or None")

    if row_delimiter == "":
        raise ValueError("Row delimiter cannot be an empty string")

    if not isinstance(ignore_empty, bool):
        raise TypeError("Ignore_empty must be a boolean")

    if match_mode not in (0, 1):
        raise ValueError("Match mode must be 0 (case-sensitive) or 1 (case-insensitive)")


def _split_all(
    text: str,
    delimiter: str,
    *,
    ignore_empty: bool,
    case_sensitive: bool,
) -> list[str]:
    """
    Internal helper that splits the text at all occurrences of the delimiter.
    """
    result: list[str] = []
    remaining = text

    while True:
        match = find_delimiter(
            text=remaining,
            delimiter=delimiter,
            case_sensitive=case_sensitive,
        )

        if not match.found:
            if remaining or not ignore_empty:
                result.append(remaining)
            break

        token = remaining[:match.start]

        if token or not ignore_empty:
            result.append(token)

        remaining = remaining[match.end:]
        
    return result


def _split_rows(
    text: str,
    row_delimiter: str | None,
    *,
    ignore_empty: bool,
    case_sensitive: bool,
) -> list[str]:
    if row_delimiter is None:
        return [text]

    return _split_all(
        text,
        row_delimiter,
        ignore_empty=ignore_empty,
        case_sensitive=case_sensitive,
    )


def _pad_rows(
    rows: list[list[str]],
    pad_with: Any,
) -> None:
    """Modifies the rows list in-place so all rows have equal length."""
    if pad_with is None or not rows:
        return

    max_columns = max(len(row) for row in rows)

    for row in rows:
        while len(row) < max_columns:
            row.append(pad_with)


def TEXTSPLIT(
    text: str,
    col_delimiter: str,
    row_delimiter: str | None = None,
    ignore_empty: bool = False,
    match_mode: int = 0,
    pad_with: Any = None,
) -> list[list[str]]:
    """Excel-compatible TEXTSPLIT() function."""
    _validate(
        text,
        col_delimiter,
        row_delimiter,
        ignore_empty,
        match_mode,
    )

    case_sensitive = match_mode == 0

    rows = _split_rows(
        text,
        row_delimiter,
        ignore_empty=ignore_empty,
        case_sensitive=case_sensitive,
    )

    result: list[list[str]] = []

    for row in rows:
        result.append(
            _split_all(
                row,
                col_delimiter,
                ignore_empty=ignore_empty,
                case_sensitive=case_sensitive,
            )
        )

    # Apply padding in-place if rows have uneven columns
    _pad_rows(result, pad_with)

    return result