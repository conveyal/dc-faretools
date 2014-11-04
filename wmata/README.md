A script to create the WMATA Metrorail FareTable file for use with OTP's DCFareCalculator

*Instructions*

Register for a WMATA API key at http://developer.wmata.com/API_Get_Started. Update config.py to include your key.

Check that the stops.csv contains an up-to-date collection of GTFS stop entries for the Metro stations. If needed, the find_metro_stops.py utility can be used to extract likely Metro stops from the stops.txt file of the WMATA GTFS feed.

Run the append_stop_codes script to link the API stop codes to the GTFS stop entries.

        python3 append_stop_codes.py

Once stop_codes.csv has been successfully created, run the write_wmata_table script to create the FareTable file:

        python3 write_wmata_table.py

Copy the resulting metrorail.csv file to the profiler fare resources directory in your OTP repo (src/main/resources/org/opentripplanner/profile/fares)
