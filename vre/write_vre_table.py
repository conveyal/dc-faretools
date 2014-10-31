import csv

# maps zone id to an array of stops
zone_stops = {}

stops = csv.DictReader(open("stops.csv"))

for stop in stops:
    zone_id = stop["zone_id"]
    if(stop["zone_id"] in zone_stops):
        zone_stops[zone_id].append(stop)
    else:
        zone_stops[zone_id] = [stop]


# function to write a single row to the output file given the from/to stops and fare
def writerow(writer, from_stop, to_stop, fare):
    row = { "from_stop_id" : from_stop["gtfs_id"], "to_stop_id" : to_stop["gtfs_id"] }
    print(from_stop["stop_name"] + " -> " + to_stop["stop_name"] + " : " + fare)
    row["peak_fare"] = row["low_fare"] = row["senior_fare"] = fare
    writer.writerow(row)


with open('vre.csv', 'w') as outfile:
    field_names = ["from_stop_id", "to_stop_id", "peak_fare", "low_fare", "senior_fare"]
    writer = csv.DictWriter(outfile, field_names)
    writer.writeheader()

    # read each zone-to-zone fare
    zone_fares = csv.DictReader(open("zone_fares.csv"))
    for zone_fare in zone_fares:

        zone1 = zone_fare["zone1"]
        zone2 = zone_fare["zone2"]

        if zone1 not in zone_stops or zone2 not in zone_stops:
            continue

        # get the lists of stops belonging to each of the two zones
        stops1 = zone_stops[zone1]
        stops2 = zone_stops[zone2]

        # write each unique pairing of a zone1 stop and zone2 ztop
        for stop1 in stops1:
            for stop2 in stops2:
                if stop1 == stop2:
                    continue
                writerow(writer, stop1, stop2, zone_fare["fare"])
                if zone1 != zone2:
                    writerow(writer, stop2, stop1, zone_fare["fare"])

