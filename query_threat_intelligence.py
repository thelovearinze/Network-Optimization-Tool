import os
import time
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_KEY = os.getenv("API_KEY")
VIRUSTOTAL_URL = "https://www.virustotal.com/api/v3/ip_addresses/"

def check_single_ip(ip):
    """
    Queries VirusTotal for a single IP address.
    """
    if not API_KEY:
        return {"IP": ip, "Error": "Missing API Key"}

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

def batch_query_virustotal(ip_list):
    """
    Scans a list of IPs, respecting the API rate limit.
    """
    results = []
    unique_ips = list(set(ip_list)) # Remove duplicates to save API calls
    
    print(f"[*] Starting Threat Intelligence Scan for {len(unique_ips)} unique IPs...")
    
    for i, ip in enumerate(unique_ips):
        print(f"    [{i+1}/{len(unique_ips)}] Scanning {ip}...", end=" ", flush=True)
        result = check_single_ip(ip)
        results.append(result)
        print("Done.")
        
        # Sleep 15s between requests to respect free tier (unless it's the last one)
        if i < len(unique_ips) - 1:
            time.sleep(15)

    return results

# This block allows you to still test it by itself if you want
if __name__ == "__main__":
    test_ips = ["8.8.8.8", "1.1.1.1"]
    print(batch_query_virustotal(test_ips))
