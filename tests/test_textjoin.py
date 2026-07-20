from __future__ import annotations
#if __name__ == "__main__":

from pathlib import Path
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from typing import Any


import pytest

from libreexceltoolkit.text.join import (
    textjoin,
    rowjoin,
    columnjoin,
)
# ---------------------------------------------------------
# TEXTJOIN
# ---------------------------------------------------------

def test_textjoin_basic():
    result = textjoin(", ", True, "A", "B", "C")
    print(f"\n -> test_textjoin_basic: {result!r}")
    assert result == "A, B, C"


def test_textjoin_empty_delimiter():
    result = textjoin("", True, "A", "B", "C")
    print(f"\n -> test_textjoin_empty_delimiter: {result!r}")
    assert result == "ABC"


def test_textjoin_ignore_empty():
    result = textjoin(",", True, "A", "", "C")
    print(f"\n -> test_textjoin_ignore_empty: {result!r}")
    assert result == "A,C"


def test_textjoin_keep_empty():
    result = textjoin(",", False, "A", "", "C")
    print(f"\n -> test_textjoin_keep_empty: {result!r}")
    assert result == "A,,C"


def test_textjoin_single_value():
    result = textjoin(",", True, "Libre")
    print(f"\n -> test_textjoin_single_value: {result!r}")
    assert result == "Libre"


def test_textjoin_no_values():
    result = textjoin(",", True)
    print(f"\n -> test_textjoin_no_values: {result!r}")
    assert result == ""


def test_textjoin_numbers():
    result = textjoin("-", True, 1, 2, 3)
    print(f"\n -> test_textjoin_numbers: {result!r}")
    assert result == "1-2-3"


def test_textjoin_none_ignored():
    result = textjoin(",", True, "A", None, "C")
    print(f"\n -> test_textjoin_none_ignored: {result!r}")
    assert result == "A,C"


def test_textjoin_none_kept():
    result = textjoin(",", False, "A", None, "C")
    print(f"\n -> test_textjoin_none_kept: {result!r}")
    assert result == "A,,C"


# ---------------------------------------------------------
# ROWJOIN
# ---------------------------------------------------------

def test_rowjoin_basic():
    data = [
        ["A", "B", "C"],
        ["D", "E", "F"],
    ]
    result = rowjoin(",", True, data)
    print(f"\n -> test_rowjoin_basic: {result!r}")
    assert result == [
        "A,B,C",
        "D,E,F",
    ]


def test_rowjoin_ignore_empty():
    data = [
        ["A", "", "C"],
        ["D", "", "F"],
    ]
    result = rowjoin(",", True, data)
    print(f"\n -> test_rowjoin_ignore_empty: {result!r}")
    assert result == [
        "A,C",
        "D,F",
    ]


def test_rowjoin_keep_empty():
    data = [
        ["A", "", "C"],
        [ "", "D", "F"],  ]
    result = rowjoin(",", False, data)
    print(f"\n -> test_rowjoin_keep_empty: {result!r}")
    assert result == [
        "A,,C",
        ",D,F",
    ]


def test_rowjoin_empty():
    result = rowjoin(",", True, [])
    print(f"\n -> test_rowjoin_empty: {result!r}")
    assert result == []


# ---------------------------------------------------------
# COLUMNJOIN
# ---------------------------------------------------------

def test_columnjoin_basic():
    data = [
        ["A", "B", "C"],
        ["D", "E", "F"],
    ]
    result = columnjoin(",", True, data)
    print(f"\n -> test_columnjoin_basic: {result!r}")
    assert result == [
        "A,D",
        "B,E",
        "C,F",
    ]


def test_columnjoin_ignore_empty():
    data = [
        ["A", "B", "C"],
        ["D", "", "F"],
    ]
    result = columnjoin(",", True, data)
    print(f"\n -> test_columnjoin_ignore_empty: {result!r}")
    assert result == [
        "A,D",
        "B",
        "C,F",
    ]


def test_columnjoin_keep_empty():
    data = [
        ["A", "", "C"],
        ["D", "", "F"],
    ]
    result = columnjoin(",", False, data)
    print(f"\n -> test_columnjoin_keep_empty: {result!r}")
    assert result == [
        "A,D",
        ",",
        "C,F",
    ]


def test_columnjoin_empty():
    result = columnjoin(",", True, [])
    print(f"\n -> test_columnjoin_empty: {result!r}")
    assert result == []


# ---------------------------------------------------------
# Validation
# ---------------------------------------------------------

def test_invalid_delimiter():
    with pytest.raises(TypeError):
        textjoin(123, True, "A")  # type: ignore
    print("\n -> test_invalid_delimiter: Successfully caught TypeError!")


def test_invalid_ignore_empty():
    with pytest.raises(TypeError):
        textjoin(",", "yes", "A")  # type: ignore
    print("\n -> test_invalid_ignore_empty: Successfully caught TypeError!")


if __name__ == "__main__":
    # The "-s" flag ensures all our print statements above show up in your terminal
    pytest.main([__file__, "-v", "-s"])