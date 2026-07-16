if __name__ == "__main__":

    from pathlib import Path
    import sys

    PROJECT_ROOT = Path(__file__).resolve().parents[1]
    sys.path.insert(0, str(PROJECT_ROOT / "src"))

#import pytest

from libreexceltoolkit.text.split import TEXTSPLIT


# ----------------------------------------------------------------------
# Basic Splitting
# ----------------------------------------------------------------------

def test_column_split():
    assert TEXTSPLIT("A,B,C", ",") == [
        ["A", "B", "C"]
    ]


def test_row_split():
    assert TEXTSPLIT(
        "A,B\nC,D",
        ",",
        "\n",
    ) == [
        ["A", "B"],
        ["C", "D"],
    ]


def test_multi_character_delimiter():
    assert TEXTSPLIT(
        "A<>B<>C",
        "<>",
    ) == [
        ["A", "B", "C"]
    ]


# ----------------------------------------------------------------------
# Ignore Empty
# ----------------------------------------------------------------------

def test_ignore_empty_false():
    assert TEXTSPLIT(
        "A,,C",
        ",",
    ) == [
        ["A", "", "C"]
    ]


def test_ignore_empty_true():
    assert TEXTSPLIT(
        "A,,C",
        ",",
        ignore_empty=True,
    ) == [
        ["A", "C"]
    ]


# ----------------------------------------------------------------------
# Match Mode
# ----------------------------------------------------------------------

def test_case_insensitive():
    assert TEXTSPLIT(
        "AxxBxxC",
        "XX",
        match_mode=1,
    ) == [
        ["A", "B", "C"]
    ]


# ----------------------------------------------------------------------
# Padding
# ----------------------------------------------------------------------

def test_padding():
    assert TEXTSPLIT(
        "A,B\nC",
        ",",
        "\n",
        pad_with="",
    ) == [
        ["A", "B"],
        ["C", ""],
    ]


def test_no_padding():
    assert TEXTSPLIT(
        "A,B\nC",
        ",",
        "\n",
    ) == [
        ["A", "B"],
        ["C"],
    ]


# ----------------------------------------------------------------------
# Edge Cases
# ----------------------------------------------------------------------

def test_leading_delimiter():
    assert TEXTSPLIT(",A,B", ",") == [
        ["", "A", "B"]
    ]


def test_trailing_delimiter():
    assert TEXTSPLIT("A,B,", ",") == [
        ["A", "B", ""]
    ]


def test_only_delimiters():
    assert TEXTSPLIT(",,,", ",") == [
        ["", "", "", ""]
    ]


def test_empty_string():
    assert TEXTSPLIT("", ",") == [
        [""]
    ]


def test_only_one_value():
    assert TEXTSPLIT("Hello", ",") == [
        ["Hello"]
    ]


# ----------------------------------------------------------------------
# Validation
# ----------------------------------------------------------------------

def test_empty_column_delimiter():
    with pytest.raises(ValueError):
        TEXTSPLIT("A,B,C", "")


def test_empty_row_delimiter():
    with pytest.raises(ValueError):
        TEXTSPLIT("A,B,C", ",", "")


def test_invalid_match_mode():
    with pytest.raises(ValueError):
        TEXTSPLIT("A,B,C", ",", match_mode=2)


def test_invalid_text_type():
    with pytest.raises(TypeError):
        TEXTSPLIT(123, ",")


def test_invalid_column_delimiter_type():
    with pytest.raises(TypeError):
        TEXTSPLIT("A,B,C", 5)


def test_invalid_row_delimiter_type():
    with pytest.raises(TypeError):
        TEXTSPLIT("A,B,C", ",", 5)


def test_invalid_ignore_empty():
    with pytest.raises(TypeError):
        TEXTSPLIT("A,B,C", ",", ignore_empty="True")



if __name__ == "__main__":
    test_column_split()
    test_row_split()
    test_multi_character_delimiter()
    test_ignore_empty_false()
    test_ignore_empty_true()
    test_case_insensitive()
    test_padding()
    test_no_padding()

    print("All tests passed.")

assert TEXTSPLIT(",A", ",") == [["", "A"]]
assert TEXTSPLIT("A,", ",") == [["A", ""]]
assert TEXTSPLIT(",,", ",") == [["", "", ""]]
assert TEXTSPLIT("", ",") == [[""]]
assert TEXTSPLIT("ABC", ",") == [["ABC"]]
assert TEXTSPLIT("A<>B<>C", "<>") == [["A", "B", "C"]]
assert TEXTSPLIT("A\n\nB", ",", "\n", ignore_empty=True) == [["A"], ["B"]]
