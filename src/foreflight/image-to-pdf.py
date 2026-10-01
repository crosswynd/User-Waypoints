#!/usr/bin/env python3
"""Convert photos supplied on the command line to PDF files."""

import argparse
from pathlib import Path

from PIL import Image


def convert_image_to_pdf(filename: Path) -> Path:
	"""Convert one image and return the path of the generated PDF."""
	output = filename.with_suffix(".pdf")
	with Image.open(filename) as image:
		# PDF does not support all image modes (notably RGBA and palette images).
		if image.mode != "RGB":
			image = image.convert("RGB")
		image.save(output, "PDF", resolution=100.0)
	return output


def main() -> int:
	parser = argparse.ArgumentParser(description="Convert photos to PDF files.")
	parser.add_argument("photos", nargs="+", type=Path, help="Photo files to convert")
	args = parser.parse_args()

	failed = False
	for photo in args.photos:
		try:
			output = convert_image_to_pdf(photo)
			print(f"{photo} -> {output}")
		except (OSError, ValueError) as error:
			failed = True
			print(f"Could not convert {photo}: {error}")

	return 1 if failed else 0


if __name__ == "__main__":
	raise SystemExit(main())
