if __name__ == "__main__":

    from pathlib import Path
    import sys

    PROJECT_ROOT = Path(__file__).resolve().parents[1]
    sys.path.insert(0, str(PROJECT_ROOT / "src"))

    from libreexceltoolkit.text.before_after import (
        textbefore,
        textafter,
    )

    tests = [
        ("abc-def-ghi", "-", 1),
        ("abc-def-ghi", "-", 2),
        ("abc-def-ghi", "-", -1),
        ("abc-def-ghi", "-", -2),
        ("abcdef", "-", 1),
        ("abcdef", "-", -1),
        ("abc-def-ghi", "d", 1),
        ("abc-def-ghi", "d", -1),
        ("Hello!, harshit", "hello", 1),
    ]

    print("=" * 80)
    print("TEXTBEFORE TESTS")
    print("=" * 80)

    for text, delimiter, instance in tests:
        try:
            result = textbefore(
                text=text,
                delimiter=delimiter,
                instance_num=instance,
            )
        except Exception as e:
            result = repr(e)

        print(
            f"{text!r}, delimiter={delimiter!r}, instance={instance:>2}"
            f" -> {result!r}"
        )

    print()
    print("=" * 80)
    print("TEXTAFTER TESTS")
    print("=" * 80)

    for text, delimiter, instance in tests:
        try:
            result = textafter(
                text=text,
                delimiter=delimiter,
                instance_num=instance,
            )
        except Exception as e:
            result = repr(e)

        print(
            f"{text!r}, delimiter={delimiter!r}, instance={instance:>2}"
            f" -> {result!r}"
        )