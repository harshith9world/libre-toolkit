if __name__ == "__main__":

    from pathlib import Path
    import sys

    PROJECT_ROOT = Path(__file__).resolve().parents[1]
    sys.path.insert(0, str(PROJECT_ROOT / "src"))

    from libreexceltoolkit.text.engine import find_delimiter
    
    tests = [
        ("Hello!, harshit", "hello", 1),
        ("abc-def-ghi", "-", 1),
        ("abc-def-ghi", "-", 2),
        ("abc-def-ghi", "-", -1),
        ("abc-def-ghi", "-", -2),
        ("abcdef", "-", 1),
        ("abcdef", "-", -1),
        ("abc-def-ghi", "x", 1),
        ("abc-def-ghi", "x", -1),
        ("abc-def-ghi", "d", 1),
        ("abc-def-ghi", "d", -1),
        ]      
    
    for text, delimiter, instance in tests:
        result = find_delimiter(
            text=text,
            delimiter=delimiter,
            instance=instance,
        )
    
        print(f"{text!r}, instance={instance} -> {result} -> {delimiter!r}")