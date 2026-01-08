import argparse
import os
import sys
from log_parser import parse_nsg_flow_logs
from threat_detection import detect_threats
from report_generator import generate_csv_report

def main():
    # Set up CLI parser
    parser = argparse.ArgumentParser(description="NSG Flow Log Threat Detection Tool")
    parser.add_argument(
        "--input", "-i", 
        type=str, 
        default="flowlog.json", 
        help="Path to the input NSG flow log JSON file"
    )
    parser.add_argument(
        "--output", "-o", 
        type=str, 
        default="threats_report.csv", 
        help="Path to save the threat report CSV"
    )
    args = parser.parse_args()

    # VALIDATION 1: Check if input file actually exists
    if not os.path.exists(args.input):
        print(f"Error: Input file '{args.input}' not found.")
        print("Tip: Make sure the file is in this folder or provide the full path.")
        sys.exit(1)

    try:
        # Step 1: Parse logs
        print(f"[*] Reading logs from '{args.input}'...")
        flows = parse_nsg_flow_logs(args.input)
        print(f" -> Success: {len(flows)} flow records parsed.")

        if not flows:
            print("Warning: No flow records found in the log file.")
            return

        # Step 2: Detect threats
        print("[*] Analyzing traffic patterns...")
        threats = detect_threats(flows)
        print(f" -> Detection Complete: {len(threats)} potential threats found.")

        # Step 3: Export to CSV
        print(f"[*] Generating report...")
        generate_csv_report(threats, output_file=args.output)
        print(f" -> Report saved to: {args.output}")

    except Exception as e:
        print(f"\n[!] Critical Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
