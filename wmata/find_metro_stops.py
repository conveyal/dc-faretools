# A helper utility to extract likely Metro station stops from the stops.txt file
# of the WMATA GTFS feed. Run in the directory containing stops.txt; the script will
# create a file metro_stops.csv that contains only the rows where the stop name
# contained "Metro".

import csv


stops = csv.DictReader(open("stops.txt"))

metro_stops = []
for stop in stops:
    stop_name = stop["stop_name"].lower()
    if("metro" in stop_name):
        metro_stops.append(stop)

sorted_stops = sorted(metro_stops, key=lambda k: k['stop_name'])

print(sorted_stops)


with open('metro_stops.csv', 'w') as outfile:
    field_names = stops.fieldnames
    writer = csv.DictWriter(outfile, stops.fieldnames)
    writer.writeheader()

    for stop in sorted_stops:
        writer.writerow(stop)