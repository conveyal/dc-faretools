# A helper utility to extract likely MARC stops from the stops.txt file of the
# MTA GTFS feed. Run in the directory containing stops.txt; the script will
# create a file marc_stops.csv that contains only the rows where the stop name
# or description contained "MARC". The script will also attempt to match the
# name against the standardized station names used in the fare table files, and
# will include the matched name in the 'name' column where applicable.


import csv

names = ["Balto/Penn Station","Aberdeen","Baltimore","Barnesville","Bowie State","Boyds","Brunswick","BWI Airport","College Park","Dickerson","Dorsey","Duffields","Edgewood","Frederick","Gaithersburg","Garrett Park","Germantown","Greenbelt","Halethorpe","Harpers Ferry","Jessup","Kensington","Laurel","Laurel Park","Martin State Airport","Martinsburg","Metropolitan Grove","Monocacy","Muirkirk","New Carrollton","Odenten","Perryville","Point of Rocks","Riverdale","Rockville","Savage","Seabrook","Silver Spring","St. Denis","Washington DC","Washington Grove","West Baltimore"]

with open('marc_stops.csv', 'w') as outfile:

    stops = csv.DictReader(open("stops.txt"))

    field_names = stops.fieldnames
    field_names.append("name")
    writer = csv.DictWriter(outfile, stops.fieldnames)
    writer.writeheader()

    for stop in stops:
        stop_name = stop["stop_name"].lower()
        stop_desc = stop["stop_desc"].lower()
        if("marc" in stop_name or "marc" in stop_desc):
            stop["name"] = ""
            for name in names:
                if(name.lower() in stop_name):
                    stop["name"] = name
            writer.writerow(stop)

