# A utility script to wriie the metrorail.csv fare table file for use with
# the OTP DC fare calculator. Requires access to WMATA Developer API; specify
# API key in config.py
#
# Run script in directory containing the config.py and stops_codes.csv files;
# script # will write output to stops_codes.csv

import config
import urllib.request, json, csv

print("key=" + config.api_key)

stops = []

stops_codes = csv.DictReader(open("stops_codes.csv"))
for stop in stops_codes:
    stops.append(stop)


with open('metrorail.csv', 'w') as outfile:
    field_names = ["from_stop_id", "to_stop_id", "peak_fare", "low_fare", "senior_fare"]
    writer = csv.DictWriter(outfile, field_names)
    writer.writeheader()
    for stop1 in stops:
        for stop2 in stops:
            stop1_code = stop1["stop_code"]
            stop2_code = stop2["stop_code"]
            if(stop1_code == stop2_code):
                continue
            url = "http://api.wmata.com/rail.svc/json/JSrcStationToDstStationInfo?FromStationCode=" + stop1_code +"&ToStationCode=" + stop2_code+ "&api_key=" + config.api_key
            success = False
            while not success:
                try:
                    response = urllib.request.urlopen(url)
                    content = response.read()
                    success = True
                except Exception as ex:
                    print(ex)
                    print("retrying...")
            data = json.loads(content.decode('utf8'))
            fares = data['StationToStationInfos'][0]["RailFare"]
            row = {
                "from_stop_id" : stop1["stop_id"],
                "to_stop_id" : stop2["stop_id"],
                "peak_fare" : fares["PeakTime"],
                "low_fare" : fares["OffPeakTime"],
                "senior_fare" : fares["SeniorDisabled"],
            }
            print(stop1["stop_name"] + " -> " + stop2["stop_name"] + " : " + str(fares["PeakTime"]) + " / " + str(fares["OffPeakTime"]) + " / " + str(fares["SeniorDisabled"]))

            writer.writerow(row)
