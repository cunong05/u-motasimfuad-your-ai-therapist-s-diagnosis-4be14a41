"""Save a short, funny therapist-style diagnosis as a single line of text.

Running this script creates the entry file the bounty expects and prints
how many characters the entry contains, so the result is easy to check.
"""

from pathlib import Path


def main():
    # One playful diagnosis line, kept short enough for the entry limit.
    diagnosis_line = "Diagnosis: chronic main-character syndrome, complicated by 47 open tabs and the emotional range of a loading spinner."
    if not diagnosis_line:
        raise SystemExit("Entry is empty, so nothing was written.")
    if "\n" in diagnosis_line or "\r" in diagnosis_line:
        raise SystemExit("Entry must fit on one line without a line break inside it.")
    entry_length = len(diagnosis_line)
    if entry_length < 1 or entry_length > 200:
        raise SystemExit(f"Entry length is {entry_length}, but it must be between 1 and 200 characters.")

    output_folder = Path("/output")
    output_folder.mkdir(parents=True, exist_ok=True)
    entry_path = output_folder / "entry.txt"
    entry_path.write_text(diagnosis_line, encoding="utf-8")
    print(entry_length)


if __name__ == "__main__":
    main()
