import sys
from pathlib import Path

from lifegraph.extraction.receipt import extract_receipt


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit(
            "Usage: python scripts/extract_receipt.py path/to/receipt.txt"
        )

    receipt_path = Path(sys.argv[1])
    receipt_text = receipt_path.read_text(encoding="utf-8")

    receipt = extract_receipt(receipt_text)
    print(receipt.model_dump_json(indent=2))


if __name__ == "__main__":
    main()
