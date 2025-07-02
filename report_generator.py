import csv
import logging

# Set up logging
logger = logging.getLogger(__name__)
if not logger.hasHandlers():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s — %(levelname)s — %(message)s",
        handlers=[
            logging.FileHandler("logs/report_generator.log", mode='a'),
            logging.StreamHandler()
        ]
    )

def generate_csv_report(threats, output_file="threats_report.csv"):
    """Exports a list of threat records to a CSV file."""
    if not threats:
        logger.warning("No threats to report. Skipping CSV generation.")
        return

    # Define CSV column headers
    headers = ["timestamp", "src_ip", "dest_ip", "src_port", "dest_port", "protocol", "rule"]

    try:
        with open(output_file, mode='w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            writer.writerows(threats)

        logger.info(f"Threat report saved to {output_file}")

    except Exception as e:
        logger.error(f"Failed to write CSV report: {e}", exc_info=True)
