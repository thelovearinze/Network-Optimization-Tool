import argparse
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

    # Step 1: Parse logs
    flows = parse_nsg_flow_logs(args.input)
    print(f"{len(flows)} flow records parsed.")

    # Step 2: Detect threats
    threats = detect_threats(flows)
    print(f"{len(threats)} threats detected.")

    # Step 3: Export to CSV
    generate_csv_report(threats, output_file=args.output)
    print(f"Threat report written to {args.output}")

    # Show a sample
    if threats:
        print("Sample threat:", threats[0])

if __name__ == "__main__":
    main()
