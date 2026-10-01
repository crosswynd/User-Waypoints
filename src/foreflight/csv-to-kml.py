#!/usr/bin/env python3
"""Convert waypoint data in a CSV file to KML."""

import argparse
import csv
import sys
import xml.etree.ElementTree as ET


KML_NS = "http://www.opengis.net/kml/2.2"
ET.register_namespace("", KML_NS)


def kml_tag(name):
	return f"{{{KML_NS}}}{name}"


def convert(source_filename, output_filename):
	required = ("Waypoint Name", "Description", "Lat", "Lon")
	root = ET.Element(kml_tag("kml"))
	document = ET.SubElement(root, kml_tag("Document"))

	with open(source_filename, encoding="utf-8-sig", newline="") as source:
		reader = csv.DictReader(source)
		if reader.fieldnames is None:
			raise ValueError("CSV file has no header row")
		missing = [column for column in required if column not in reader.fieldnames]
		if missing:
			raise ValueError("Missing CSV columns: " + ", ".join(missing))

		for row_number, row in enumerate(reader, start=2):
			try:
				latitude = float(row["Lat"])
				longitude = float(row["Lon"])
			except (TypeError, ValueError) as exc:
				raise ValueError(f"Invalid coordinates on CSV row {row_number}") from exc
			if not -90 <= latitude <= 90 or not -180 <= longitude <= 180:
				raise ValueError(f"Coordinates out of range on CSV row {row_number}")

			placemark = ET.SubElement(document, kml_tag("Placemark"))
			ET.SubElement(placemark, kml_tag("name")).text = row["Waypoint Name"] or ""
			ET.SubElement(placemark, kml_tag("description")).text = row["Description"] or ""
			point = ET.SubElement(placemark, kml_tag("Point"))
			ET.SubElement(point, kml_tag("coordinates")).text = (
				f"{longitude:.15g},{latitude:.15g},0"
			)
			ET.SubElement(point, kml_tag("altitudeMode")).text = "absolute"
	
	ET.indent(root, space="  ")
	ET.ElementTree(root).write(output_filename, encoding="utf-8", xml_declaration=True)


def main():
	parser = argparse.ArgumentParser(description="Convert a waypoint CSV file to KML.")
	parser.add_argument("source_file", help="Input CSV filename")
	parser.add_argument("output_file", help="Output KML filename")
	args = parser.parse_args()
	try:
		convert(args.source_file, args.output_file)
	except (OSError, csv.Error, ValueError) as exc:
		print(f"Error: {exc}", file=sys.stderr)
		return 1
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
