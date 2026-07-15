if __name__ == "__main__":

    from pathlib import Path
    import sys

    PROJECT_ROOT = Path(__file__).resolve().parents[1]
    sys.path.insert(0, str(PROJECT_ROOT / "src"))

from libreexceltoolkit.text.before_after import textbefore, textafter

print(textbefore("A-B-C", "-"))
print(textafter("A-B-C", "-"))
