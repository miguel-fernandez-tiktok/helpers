import csv
from datetime import datetime

# Input and output file paths
input_file = 'input.csv'
output_file = 'output.csv'

# Read input CSV and prepare output CSV
with open(input_file, 'r', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    fieldnames = reader.fieldnames
    
    with open(output_file, 'w', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        
        # Process each row in the input CSV
        for row in reader:
            timestamp = row['timestamp']
            
            # Convert timestamp to ISO-8601 format
            original_date = datetime.strptime(timestamp, '%m/%d/%Y %H:%M:%S%z')
            iso8601_timestamp = original_date.strftime('%Y-%m-%dT%H:%M:%S%z')
            
            # Update the row with the ISO-8601 timestamp
            row['timestamp'] = iso8601_timestamp
            
            # Write the updated row to the output CSV
            writer.writerow(row)

print("Conversion completed. Output file:", output_file)
