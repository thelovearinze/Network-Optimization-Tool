import json
import csv

# Load the JSON log file
with open("flowlog.json", "r") as file:
    data = json.load(file)

# Prepare CSV file
csv_filename = "flowlog.csv"
fields = ["time", "source_ip", "destination_ip", "source_port", "destination_port", "protocol", "direction", "action"]

with open(csv_filename, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(fields)

    # Extract relevant fields
    for record in data["records"]:
        time = record["time"]
        flows = record["properties"]["flows"]

        for flow in flows:
            rule = flow["rule"]

            for entry in flow["flows"]:
                mac = entry["mac"]
                
                for tuple_data in entry["flowTuples"]:
                    tuple_values = tuple_data.split(",")
                    timestamp, src_ip, dest_ip, src_port, dest_port, protocol, direction, action = tuple_values

                    writer.writerow([time, src_ip, dest_ip, src_port, dest_port, protocol, direction, action])

print(f" Flow log data has been successfully saved to {csv_filename}")
