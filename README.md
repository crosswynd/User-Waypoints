# Malaysia VFR Data for Foreflight
## Introduction
This project is intended to prepare Malaysia VFR data for ForeFlight. 

## Source of Data
Waypoints are created from coordinates listed in WM-ENR-3.5, CAAM AIP published on 05 Nov 2020 (latest as of 29 Sep 2026). A few waypoints around the Langkawi and Ipoh areas do not have published coordinates and are placed manually based on map locations.  

Currently include waypoints:
<img width="2189" height="1049" alt="image" src="https://github.com/user-attachments/assets/704070b6-7c7e-4051-923e-e280b715c93d" />

### Data Manipulation
The following steps were taken:
1. Manual data manipulation
    1. Manual copy of waypoint names, descriptions, and coordinates from publication into Excel file.
    2. Minor manual data cleansing (e.g. special characters, updating descriptions with waypoint names if not provided, etc).
2. Excel formulas
    1. Convert names into upper case with underscore (Foreflight compatible format).
    2. Apply standard abbreviations e.g. Bukit -> BT, Kampung -> Kg, etc.
    3. Convert coordinates to decimal degrees with 5 decimal place accuracy.
3. Building KML/KMZ
    1. Export to CSV
    2. Convert CSV to KML with name, description, and coordinates. For KMZ format, add a style for icon and the icon PNG.

## Map Layer for Importing as Custom Waypoints
VFR waypoints data for importing as Custom Waypoints are available as a KML file. 

Due to ForeFlight constraints, waypoint style (icon and icon color) cannot be specified. If you don't like the default display, you can specify it yourself in the custom waypoint editor. But you will have to do it one waypoint at a time. 

## VFR Waypoints in a Content Pack 
VFR waypoints are also available as a content pack. Note that when a layer is displayed from a Content Pack, the icons do not declutter on zooming out. 

Waypoint photos will be added over time - crowdsourcing required! Please contact me to contribute photos. Photos will appear as such:
<img width="1050" height="956" alt="WaypointAdditionalInfo" src="https://github.com/user-attachments/assets/d70def6c-6015-4f57-8bf1-fbdc972d7eaa" />

## Installation Instructions
Download the KML file or the Content Pack (zip file) from Releases (on the right side of the page). Open the respective file with Foreflight and load it as Custom Waypoints or Content Pack. 

If you already have custom waypoints, you may want to consider whether to load the 180+ additional waypoints. If you want to keep it separate, consider using the Content Pack as you can delete it easily. 

## Future Content Ideas
Some ideas for Content Pack:

1. VFR lane overlays - Initial assessment is that the diagrams published in the WM-ENR are not accurate enough to be georeferenced. Content Pack line drawings are unfortunately not labelled. 

## Disclaimer
The information and data provided by this service are for informational purposes only. While every effort is made to ensure quality and relevance, the creator makes no representations or warranties of any kind, express or implied, regarding the accuracy, completeness, reliability, suitability, or availability of any data.

Any reliance you place on such information is strictly at your own risk. The creator shall not be held liable for any loss, damage, or consequence arising directly or indirectly from the use of or reliance on this data. Users are advised to independently verify critical information before taking action based upon it. 
