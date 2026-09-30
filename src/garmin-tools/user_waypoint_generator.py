"""Convert a CSV file into XML using its headers and cell values."""

import argparse
import csv
import xml.etree.ElementTree as ET
from pathlib import Path


def csv_to_xml(csv_path, xml_path, root_name="", row_name="waypoint"):
	"""Write CSV records as XML elements, using headers as field names."""
	with open(csv_path, "r", newline="", encoding="utf-8-sig") as csv_file:
		reader = csv.DictReader(csv_file)
		if not reader.fieldnames:
			raise ValueError("The CSV file must contain a header row.")

		root = ET.Element(root_name)
		for record in reader:
			row = ET.SubElement(root, row_name)
			for header, value in record.items():
				# Empty or duplicate CSV headers cannot be XML tag names.
				tag = (header or "column").strip() or "column"
				field = ET.SubElement(row, tag)
				field.text = value or ""

	ET.indent(root, space="  ")
	ET.ElementTree(root).write(xml_path, encoding="utf-8", xml_declaration=True, short_empty_elements=False)

def main():
	parser = argparse.ArgumentParser(description="Generate XML from a CSV file.")
	parser.add_argument("csv_file", type=Path, help="Input CSV file")
	parser.add_argument(
		"xml_file", type=Path, nargs="?", help="Output XML file (defaults to the input name with .xml)"
	)
	parser.add_argument("--root", default="rows", help="Name of the XML root element")
	parser.add_argument("--row", default="waypoint", help="Name of each record element")
	args = parser.parse_args()

	output = args.xml_file or args.csv_file.with_suffix(".xml")
	csv_to_xml(args.csv_file, output, args.root, args.row)

if __name__ == "__main__":
	main()
