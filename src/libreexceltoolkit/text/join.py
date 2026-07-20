from __future__ import annotations
from typing import Iterable, Any

def _join(
        *,
        delimiter: str,
        ignore_empty: bool,
        values: Iterable[Any],
) -> str:
    """Internal Join engine; joins the given values into a single string using the specified delimiter.

    Args/parameters:

       1) delimiter (str): The string to insert between each value.
       2) ignore_empty (bool): Whether to ignore empty values in the input.
       3) values (Iterable[Any]): An iterable of values to join.
     Sahred by:
        TEXTJOIN
        ROWJOIN
        COLUMNJOIN
    """
    if not isinstance(delimiter, str):
        raise TypeError("delimiter must be a string")
    
    if not isinstance(ignore_empty, bool):
        raise TypeError("ignore_empty must be a boolean")
    
    if values is None:
        raise TypeError("values cannot be None")
    
    text_parts: list[str] = []
    for value in values:
        if value is None:
            value_str = ""
        else:
            value_str = str(value)
        
        if ignore_empty and value_str == "":
            continue
        
        text_parts.append(value_str)
    return delimiter.join(text_parts)


def textjoin(
        delimiter : str,
        ignore_empty : bool,
        *values: Any, # type: ignore
) -> str:
    """ 
    Excel like TEXTJOIN function; joins the given values into a single string using the specified delimiter.
    """
    return _join(
        delimiter=delimiter,
        ignore_empty=ignore_empty,
        values=values,
        )


def rowjoin(
        delimiter : str,
        ignore_empty : bool,
        rows : Iterable[Iterable[Any]],
    ) -> str:

    result = []

    for row in rows:
        result.append(
            _join(
                delimiter=delimiter,
                ignore_empty=ignore_empty,
                values=row,
            )
        )

    return result


def columnjoin(
        delimiter : str,
        ignore_empty : bool,
        rows : Iterable[Iterable[Any]],
    ) -> list[str]:
   
    matrix = [list(row) for row in rows]
    
    if not matrix:
        return []
    result: list[str] = []
    column_count = len(matrix[0])

    for col in range(column_count):

        column_values = []

        for row in matrix:
            column_values.append(row[col])

        result.append(
            _join(
                delimiter=delimiter,
                ignore_empty=ignore_empty,
                values=column_values,
            )
        )

    return result
