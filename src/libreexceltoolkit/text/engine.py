"""
Core text processing engine.

This module contains reusable text algorithms that are independent of
Excel, LibreOffice, or UNO. It provides low-level operations that are
used by higher-level Excel-compatible functions.
"""
from __future__ import annotations
from dataclasses import dataclass

@dataclass(frozen=True)
class DelimiterMatch:
    """Represents a result of a delimiter search.

    Attributes:
        found (bool): Whether a delimiter was found.
        start (int): The starting index of the match.
        end (int): The ending index of the match.
        "delimiter (str): The matched delimiter string."
    """
    found: bool
    start: int
    end: int
    #delimiter: str

def find_delimiter(
        *,
        text: str,
        delimiter: str,
        instance: int = 1,
        case_sensitive: bool = True,
) -> DelimiterMatch:
    
    """Finds the specified instance of a delimiter in the given text.

    Args/parameters:

       1) text (str): Source Text - where to find.
       2) delimiter (str): Delimiter type - What to find?
       3) instance (int, default = 1): 
            positive value = start from begining
            negative value = start from end
       4) case_sensitive (bool, default = True):
            Whether the search should be case-sensitive. Defaults to True.

    Returns:
        DelimiterMatch: An object containing information about the match.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    if not isinstance(delimiter, str):
        raise TypeError("delimiter must be a string")
    
    if delimiter == "":
        raise ValueError("delimiter cannot be an empty string")
    
    if instance == 0:
        raise ValueError("Instance must be a non-zero integer can be positive [from the beginning] or negative [from the end]")
    
    search_text = text if case_sensitive else text.casefold()
    search_delimiter = delimiter if case_sensitive else delimiter.casefold()
    delimiter_length = len(search_delimiter)
    #---------------------------------------------------------
    # Froward search for positive instance values
    #---------------------------------------------------------

    if instance > 0:
        position = -1
        start = 0

        for _ in range(instance):
            position = search_text.find(search_delimiter, start)
            
            if position == -1:
                return DelimiterMatch(
                    found=False,
                    start=-1,
                    end=-1
                )
            
            start = position + delimiter_length
        
        return DelimiterMatch(
            found=True,
            start=position,
            end=position + delimiter_length,
        )

    #---------------------------------------------------------
    # Reverse search for negative instance values
    #---------------------------------------------------------
    

    occurrence = abs(instance)
    position = len(search_text)

    for _ in range(occurrence):
        position = search_text.rfind(
            search_delimiter,
            0,
            position,
        )
        
        if position == -1:
            return DelimiterMatch(
                found=False,
                start=-1,
                end=-1
            )
            
    return DelimiterMatch(
        found=True,
        start=position,
        end=position + delimiter_length,
    )
    
