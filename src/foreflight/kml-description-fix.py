import re
import sys


# Remove Lat Lon data from the Description field. 
# Set these to the text patterns and replacements required by the KML source. 
SUBSTITUTIONS = (
    (re.compile(r"<!\[CDATA\[Description: "), ""),
    (re.compile(r"<!\[CDATA\["), ""),
    (re.compile(r"<br.*\]>"), ""),
)


def main():
    if len(sys.argv) != 3:
        raise SystemExit(f"Usage: {sys.argv[0]} INPUT_FILE OUTPUT_FILE")

    with open(sys.argv[1], "r", encoding="utf-8", newline="") as source, open(
        sys.argv[2], "w", encoding="utf-8", newline=""
    ) as destination:
        for line in source:
            for pattern, replacement in SUBSTITUTIONS:
                line = pattern.sub(replacement, line)
            destination.write(line)


if __name__ == "__main__":
    main()