from dotenv import load_dotenv
import os

load_dotenv()  # This loads the variables from your .env file

API_KEY = os.getenv("API_KEY")  # Now API_KEY comes from the .env file

import requests

# List of blocked IPs from analysis_results.txt
blocked_ips = [
    "147.185.132.172", "89.248.163.14", "194.50.16.198",
    "162.216.149.140", "35.203.210.38", "57.129.64.219",
    "107.173.58.11", "109.236.61.85", "35.203.210.55",
    "80.82.77.33"
]

# Removed the hardcoded API_KEY assignment here:
# API_KEY = "6edd29e5e707c784ada1d6a6286e967e870bbad09347e4b6cf879d6aa615f1e4"

VIRUSTOTAL_URL = "https://www.virustotal.com/api/v3/ip_addresses/"

# Function to query threat intelligence
def check_ip(ip):
    headers = {
        "x-apikey": API_KEY
    }
    response = requests.get(VIRUSTOTAL_URL + ip, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return {
            "IP": ip,
            "Malicious Votes": data["data"]["attributes"]["last_analysis_stats"]["malicious"],
            "Suspicious Votes": data["data"]["attributes"]["last_analysis_stats"]["suspicious"],
            "Harmless Votes": data["data"]["attributes"]["last_analysis_stats"]["harmless"],
            "ASN": data["data"]["attributes"].get("asn", "Unknown"),
            "Country": data["data"]["attributes"].get("country", "Unknown"),
        }
    else:
        return {"IP": ip, "Error": response.text}

# Check each blocked IP
results = [check_ip(ip) for ip in blocked_ips]

# Save results
with open("threat_intelligence_results.txt", "w") as file:
    for result in results:
        file.write(str(result) + "\n")

print("Threat Intelligence Analysis Completed! Results saved in 'threat_intelligence_results.txt'")
