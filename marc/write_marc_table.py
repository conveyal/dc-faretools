# Generates the marc.csv file used in the OTP DC fare calculator
#
# Run in directory containing the three required input files:
# 1. penn_fares.csv - the station-to-station fare table for the Penn line
# 2. brunswickcamden_fares.csv - the station-to-station fare table for the
#      Brunswick & Camden lines
# 3. stops.csv - a file mapping station names to GTFS stop IDs. Individual
#      stations may correspond to multiple GTFS stops

import csv

# create a mapping of station names to GTFS stop IDs

stop_ids = {} # maps station name string to array of stop IDs
stops = csv.DictReader(open("stops.csv"))
for stop in stops:
    name = stop["name"]
    if(name in stop_ids):
        stop_ids[name].append(stop["stop_id"])
    else:
        stop_ids[name] = [stop["stop_id"]]


# A function to write a single station-to-station fare. Will produce
# multiple rows in the output file if either station has multiple GTFS stops

def writerow(writer, from_name, to_name, fare):
    print("writing fare " + from_name + " to " + to_name + " : " + fare)

    if(from_name not in stop_ids):
        print("Warning: could not find " + from_name + " in stops.csv")
        return

    if(to_name not in stop_ids):
        print("Warning: could not find " + to_name + " in stops.csv")
        return

    if fare == "":
        return

    from_gtfs_ids = stop_ids[from_name]
    to_gtfs_ids = stop_ids[to_name]

    # write a row for each pairing of "from" and "to" GTFS stops
    for from_id in from_gtfs_ids:
        for to_id in to_gtfs_ids:
            row = { "from_stop_id" : from_id, "to_stop_id" : to_id }
            row["peak_fare"] = row["low_fare"] = row["senior_fare"] = fare
            writer.writerow(row)


# A function to process a single fare input table

def process_fare_table(filename, writer):
    fares = csv.DictReader(open(filename))

    for fare_row in fares:
        origin_name = fare_row["ORIGIN"]
        for dest_name in fare_row:
            if(dest_name != "ORIGIN" and dest_name != origin_name):
                writerow(writer, origin_name, dest_name, fare_row[dest_name])


# Open the output file and process the two input tables

with open('marc.csv', 'w') as outfile:
    field_names = ["from_stop_id", "to_stop_id", "peak_fare", "low_fare", "senior_fare"]
    writer = csv.DictWriter(outfile, field_names)
    writer.writeheader()

    process_fare_table("penn_fares.csv", writer)
    process_fare_table("brunswickcamden_fares.csv", writer)