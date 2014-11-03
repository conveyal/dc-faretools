A script to create the Maryland MARC FareTable file for use with OTP's DCFareCalculator

*Instructions*

Check that the stop-to-stop input data in penn_fares.csv and brunswickcamden_fares.csv is up to date. Refer to http://mta.maryland.gov/marc-fares for zone/fare tables.

Check that the GTFS ID mappings in stops.csv are up to date. The values for the 'name' column in stops.csv should match the row/column headers in the two fare input files above. The find_marc_stops.py script can be used to identify likely MARC stops in the stops.txt file of the MTA GTFS feed.

Once penn_fares.csv, brunswickcamden_fares.csv, and stops.csv are up to date, run the script to create the FareTable file

        python3 write_marc_table.py

Copy the resulting marc.csv file to the profiler fare resources directory in your OTP repo (src/main/resources/org/opentripplanner/profile/fares)
