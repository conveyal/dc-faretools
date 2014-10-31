A script to create the Virginia Railway Express (VRE) FareTable file for use with OTP's DCFareCalculator

*Instructions*

Check that the input data in stops.csv and zone_fares.csv is up to date. Refer to http://www.vre.org/service/fares.htm for current zone/fare information

Run the script to create the FareTable file

        python3 write_vre_table.py

Copy the resulting vre.csv file to the profiler fare resources directory in your OTP repo (src/main/resources/org/opentripplanner/profile/fares)
