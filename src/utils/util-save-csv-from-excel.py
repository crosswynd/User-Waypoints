"""Save one worksheet from an .xlsx workbook as a CSV file."""

import argparse
from pathlib import Path

import pandas as pd


def save_sheet_as_csv(source_file: str, output_file: str, sheet_name: str) -> None:
	"""Write *sheet_name* from *source_file* to *output_file*."""
	with pd.ExcelFile(source_file) as workbook:
		if sheet_name not in workbook.sheet_names:
			available = ", ".join(workbook.sheet_names)
			raise ValueError(f"Sheet {sheet_name!r} not found. Available sheets: {available}")

		worksheet = pd.read_excel(workbook, sheet_name=sheet_name, header=None)
		Path(output_file).parent.mkdir(parents=True, exist_ok=True)
		worksheet.to_csv(
			output_file,
			index=False,
			header=False,
			encoding="utf-8-sig",
			na_rep="",
		)


def main() -> None:
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument("source_file", help="Input .xlsx file")
	parser.add_argument("output_file", help="Output .csv file")
	parser.add_argument("sheet_name", help="Worksheet name to export")
	args = parser.parse_args()
	save_sheet_as_csv(args.source_file, args.output_file, args.sheet_name)


if __name__ == "__main__":
	main()
