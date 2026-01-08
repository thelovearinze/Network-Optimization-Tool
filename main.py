import argparse
import os
import sys
from log_parser import parse_nsg_flow_logs
from threat_detection import detect_threats
from report_generator import generate_csv_report
from query_threat_intelligence import batch_query_virustotal

def main():
    parser = argparse.ArgumentParser(description="NSG Flow Log Threat Detection Tool")
    parser.add_argument("--input", "-i", type=str, default="flowlog.json", help="Path to input logs")
    parser.add_argument("--output", "-o", type=str, default="threats_report.csv", help="Path to save CSV report")
    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"Error: Input file '{args.input}' not found.")
        sys.exit(1)

    try:
        # 1. Parse
        print(f"[*] Reading logs from '{args.input}'...")
        flows = parse_nsg_flow_logs(args.input)
        print(f" -> Success: {len(flows)} flow records parsed.")

        if not flows:
            return

        # 2. Detect
        print("[*] Analyzing traffic patterns...")
        threats = detect_threats(flows)
        print(f" -> Detection Complete: {len(threats)} potential threats found.")

        # 3. Threat Intel (The New Step!)
        if threats:
            # Get unique IPs from the threats
            attacker_ips = list(set([t['src_ip'] for t in threats]))
            print(f"\n[*] Found {len(attacker_ips)} unique suspicious IPs.")
            
            # Limit to top 3 for the demo to save time
            ips_to_scan = attacker_ips[:3] 
            print(f"[*] Sending top {len(ips_to_scan)} IPs to VirusTotal for analysis...")
            
            vt_results = batch_query_virustotal(ips_to_scan)
            
            # Save the Intel Report
            with open("threat_intelligence_results.txt", "w") as f:
                for res in vt_results:
                    f.write(str(res) + "\n")
            print(" -> Intelligence saved to 'threat_intelligence_results.txt'")

        # 4. CSV Report
        print(f"\n[*] Generating final CSV report...")
        generate_csv_report(threats, output_file=args.output)
        print(f" -> Report saved to: {args.output}")

    except Exception as e:
        print(f"\n[!] Critical Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
