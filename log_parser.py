import json
import logging

# Set up structured logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s — %(levelname)s — %(message)s",
    handlers=[
        logging.FileHandler("logs/log_parser.log", mode='a'),
        logging.StreamHandler()
    ]
)

def parse_nsg_flow_logs(file_path):
    """Parses a given NSG flow log JSON file and extracts relevant flow records."""
    flow_records = []

    try:
        with open(file_path, 'r') as file:
            data = json.load(file)

        logging.info(f"Loaded NSG flow log from {file_path}")

        records = data.get('records', [])
        for record in records:
            try:
                flows_section = record.get('properties', {}).get('flows', [])
                for flow_group in flows_section:
                    rule = flow_group.get('rule')
                    for flow in flow_group.get('flows', []):
                        for flow_data in flow.get('flowTuples', []):
                            parts = flow_data.split(',')
                            if len(parts) < 6:
                                logging.warning(f"Skipping malformed flow tuple: {flow_data}")
                                continue

                            flow_dict = {
                                'timestamp': parts[0],
                                'src_ip': parts[1],
                                'dest_ip': parts[2],
                                'src_port': parts[3],
                                'dest_port': parts[4],
                                'protocol': parts[5],
                                'rule': rule
                            }
                            flow_records.append(flow_dict)

            except Exception as inner_err:
                logging.error(f"Error parsing a flow record: {inner_err}", exc_info=True)

        logging.info(f"Extracted {len(flow_records)} flow records")
        return flow_records

    except FileNotFoundError:
        logging.error(f"File not found: {file_path}", exc_info=True)
    except json.JSONDecodeError:
        logging.error(f"Invalid JSON in file: {file_path}", exc_info=True)
    except Exception as e:
        logging.error(f"Unexpected error while parsing logs: {e}", exc_info=True)

    return []
