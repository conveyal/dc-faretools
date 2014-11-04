# A utility script to match GTFS stop IDS to the WMATA API station code using
# lat/lon proximity and append the stop codes to the GTFS stop records.
# Requires access to WMATA Developer API; specify # API key in config.py
#
# Run script in directory containing the config.py and stops.csv files; script
# will write output to stops_codes.csv

import config
import urllib.request, json, csv


response = urllib.request.urlopen("http://api.wmata.com/Rail.svc/json/jStations?api_key="+config.api_key)
content = response.read()
data = json.loads(content.decode('utf8'))

stop_codes = {}

for station in data["Stations"]:

    best_delta = 1
    stops = csv.DictReader(open("stops.csv"))
    for stop in stops:
        dlat = abs(float(stop["stop_lat"]) - float(station["Lat"]))
        dlon = abs(float(stop["stop_lon"]) - float(station["Lon"]))
        delta = dlat + dlon
        if(delta < best_delta):
            best_stop = stop
            best_delta = delta

    stop_codes[best_stop["stop_id"]] = station["Code"]

print(stop_codes)


stops = csv.DictReader(open("stops.csv"))
appended_stops = []
for stop in stops:
    stop["stop_code"] = stop_codes[stop["stop_id"]]
    appended_stops.append(stop)

print(appended_stops)

with open('stops_codes.csv', 'w') as outfile:

    field_names = stops.fieldnames
    if("stop_code" not in field_names):
        field_names.append("stop_code")
    print(field_names)
    writer = csv.DictWriter(outfile, stops.fieldnames)
    writer.writeheader()

    for stop in appended_stops:
        writer.writerow(stop)
