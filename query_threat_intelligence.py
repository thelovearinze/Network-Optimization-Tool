import os
import time
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_KEY = os.getenv("API_KEY")
VIRUSTOTAL_URL = "https://www.virustotal.com/api/v3/ip_addresses/"

# TODO: In the future, read this list from 'analysis_results.txt' automatically.
# For now, this is a placeholder list for demonstration.
blocked_ips = [
    "147.185.132.172", "89.248.163.14", "194.50.16.198",
    "162.216.149.140", "35.203.210.38", "57.129.64.219",
    "107.173.58.11", "109.236.61.85", "35.203.210.55",
    "80.82.77.33"
]

def check_ip(ip):
    headers = {"x-apikey": API_KEY}
    try:
        response = requests.get(f"{VIRUSTOTAL_URL}{ip}", headers=headers)
        if response.status_code == 200:
            data = response.json()
            attributes = data["data"]["attributes"]
            stats = attributes["last_analysis_stats"]
            return {
                "IP": ip,
                "Malicious": stats["malicious"],
                "Suspicious": stats["suspicious"],
                "Harmless": stats["harmless"],
                "Country": attributes.get("country", "Unknown"),
                "ASN": attributes.get("asn", "Unknown")
            }
        elif response.status_code == 429:
            return {"IP": ip, "Error": "Rate Limit Exceeded"}
        else:
            return {"IP": ip, "Error": f"Status {response.status_code}"}
    except Exception as e:
        return {"IP": ip, "Error": str(e)}

if __name__ == "__main__":
    if not API_KEY:
        print("Error: API_KEY not found in .env file.")
        exit(1)

    print(f"Starting Threat Intelligence Scan for {len(blocked_ips)} IPs...")
    results = []

    for ip in blocked_ips:
        print(f"Scanning {ip}...", end=" ", flush=True)
        result = check_ip(ip)
        results.append(result)
        print("Done.")
        
        # SLEEP to respect VirusTotal free tier (4 requests/minute)
        # We wait 15 seconds to be safe.
        time.sleep(15)

    # Save results
    with open("threat_intelligence_results.txt", "w") as file:
        for result in results:
            file.write(str(result) + "\n")

    print("\nScan Completed. Results saved to 'threat_intelligence_results.txt'")
