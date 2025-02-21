import json
import pandas as pd

# Read the text file with threat intelligence results
with open("threat_intelligence_results.txt", "r") as file:
    data = [json.loads(line.replace("'", '"')) for line in file.readlines()]

# Convert to a Pandas DataFrame
df = pd.DataFrame(data)

# Save results as CSV
df.to_csv("threat_intelligence_results.csv", index=False)

print("✅ Threat Intelligence Results saved as 'threat_intelligence_results.csv'")
