import re
import unicodedata


def clean_filename(filename: str) -> str:
    filename = (
        unicodedata.normalize("NFKD", filename)
        .encode("ascii", "ignore")
        .decode("ascii")
    )
    filename = re.sub(r"[^a-zA-Z0-9_-]", "_", filename)
    filename = re.sub(r"__+", "_", filename).strip("_")

    return filename.lower()
