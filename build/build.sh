#!/bin/bash

# Create and move into output directory
mkdir temp
cd temp

# Build G1000 navdata file
mkdir navdata
cd navdata
cp ../../data/MY/Waypoints.xlsx ./
python ../../src/utils/util-save-csv-from-excel.py Waypoints.xlsx Waypoints.csv "Garmin Output"
python ../../src/garmin-tools/user-waypoint-generator.py Waypoints.csv waypoints.fpl
rm ./Waypoints.xlsx
rm ./Waypoints.csv
cd ..

# Build MY Custom Waypoints KML file
mkdir custom_waypoints
cd custom_waypoints
cp ../../data/MY/Waypoints.xlsx ./
python ../../src/utils/util-save-csv-from-excel.py Waypoints.xlsx Waypoints.csv "Google My Maps Output"
python ../../src/foreflight/csv-to-kml.py Waypoints.csv "MY VFR Waypoints.kml"
rm ./Waypoints.xlsx
rm ./Waypoints.csv
cd ..

# Build Content Pack
mkdir content_pack
cd content_pack
mkdir images

# Create KMZ file
cp ../../data/icon.png images/
cp ../../data/MY/Waypoints.xlsx ./
python ../../src/utils/util-save-csv-from-excel.py Waypoints.xlsx Waypoints.csv "Google My Maps Output"
python ../../src/foreflight/csv-to-kmz.py Waypoints.csv "MY VFR Waypoints.kml" "Malaysia VFR Waypoints"
rm ./MY\ VFR\ Waypoints.kml
rm -rf images/
rm ./Waypoints.xlsx
rm ./Waypoints.csv

# Create Content Pack structure
mkdir navdata

# Process photos and move KMZ file
mv "MY VFR Waypoints.kmz" navdata/
cd navdata
cp ../../../data/MY/photos/* ./
python ../../../src/foreflight/image-to-pdf.py *.jpeg
rm *.jpeg
cd ..

# Write manifest file and zip the content pack
cat << EOF > manifest.json
{
	"name": "Malaysia VFR Pack",
	"abbreviation": "MY_VFR",
	"version": $GITHUB_REF_NAME,
	"organizationName": "SG FAA"
}
EOF
zip -r "MY VFR Waypoints.zip" manifest.json navdata/

# Copy to output
cd ../../
mkdir dist
cp temp/content_pack/"MY VFR Waypoints.zip" dist/
cp temp/custom_waypoints/"MY VFR Waypoints.kml" dist/
cp temp/navdata/waypoints.fpl dist/
