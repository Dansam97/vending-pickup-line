"""Entry for make.fun bounty u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee.

Writes one pickup line, spoken by a vending machine to a passing human,
to entry.txt in the output directory.
"""

import os

TEXT = (
    "My coils only spin for you - press B7 and I'll drop the last "
    "chocolate bar, no exact change required."
)


MAX_CHARS = 200


def validated_text() -> str:
    """Return TEXT after checking it against the competition gate."""
    encoded = TEXT.encode("utf-8")  # raises if not encodable as UTF-8
    if not TEXT.strip():
        raise ValueError("entry text must not be only whitespace")
    if "\n" in TEXT or "\r" in TEXT:
        raise ValueError("entry text must be a single line")
    if not 1 <= len(TEXT) <= MAX_CHARS:
        raise ValueError(
            f"entry text must be 1..{MAX_CHARS} characters, got {len(TEXT)}"
        )
    if len(encoded.decode("utf-8")) != len(TEXT):
        raise ValueError("entry text does not round-trip as UTF-8")
    return TEXT


def main() -> None:
    text = validated_text()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    payload = (text + "\n").encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(payload)
    # Read back and prove the bytes on disk are exactly what we intended.
    with open(path, "rb") as fh:
        if fh.read() != payload:
            raise IOError("entry.txt bytes differ after write")


if __name__ == "__main__":
    main()
