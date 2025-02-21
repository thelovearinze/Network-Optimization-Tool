import os
import subprocess
import json

# Step 1: Get the latest blob name dynamically
print("🔍 Fetching the latest NSG flow log...")
result = subprocess.run([
    "az", "storage", "blob", "list",
    "--account-name", "lanetoptstorage5547",
    "--container-name", "insights-logs-networksecuritygroupflowevent",
    "--query", "[].{Name:name}",
    "--output", "json",
    "--auth-mode", "login"
], capture_output=True, text=True)

# Parse the output and get the latest available log file
blob_list = json.loads(result.stdout)
if not blob_list:
    print("🚨 No NSG flow logs found in the storage container!")
    exit(1)  # Stop execution

latest_blob = blob_list[-1]["Name"]  # Get the last blob in the list
print(f"📂 Latest available blob: {latest_blob}")

# Step 2: Download the latest flow log using the FULL path
print("🚀 Downloading latest NSG flow logs...")
subprocess.run([
    "az", "storage", "blob", "download",
    "--account-name", "lanetoptstorage5547",
    "--container-name", "insights-logs-networksecuritygroupflowevent",
    "--name", latest_blob,  # Use FULL path
    "--file", "flowlog.json",
    "--auth-mode", "login"
])

# Step 3: Parse the new logs
print("📊 Parsing flow logs...")
subprocess.run(["python3", "parse_flow_logs.py"])

# Step 4: Analyze new logs
print("🔎 Running threat analysis...")
subprocess.run(["python3", "analyze_flow_logs.py"])

# Step 5: Query updated threat intelligence
print("🌍 Querying threat intelligence database...")
subprocess.run(["python3", "query_threat_intelligence.py"])

# Step 6: Save the results to CSV
print("📁 Saving threat results...")
subprocess.run(["python3", "save_threat_results.py"])

# Step 7: Generate updated visualizations
print("📈 Updating visualizations...")
subprocess.run(["python3", "visualize_threat_data.py"])

print("✅ Automated threat database update completed successfully!")
