import logging

# Set up logging if not already configured
logger = logging.getLogger(__name__)
if not logger.hasHandlers():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s — %(levelname)s — %(message)s",
        handlers=[
            logging.FileHandler("logs/threat_detection.log", mode='a'),
            logging.StreamHandler()
        ]
    )

def detect_threats(flow_records, suspicious_ports=None):
    """Detects threats based on known suspicious ports or IP patterns."""
    if suspicious_ports is None:
        suspicious_ports = {'22', '23', '3389', '8080'}  # SSH, Telnet, RDP, HTTP alternate

    threats = []
    try:
        for record in flow_records:
            try:
                dest_port = record.get('dest_port')
                if dest_port in suspicious_ports:
                    logger.info(f"Suspicious activity detected: {record}")
                    threats.append(record)
            except Exception as inner_err:
                logger.warning(f"Could not process record: {record}, reason: {inner_err}")

        logger.info(f"Threat detection complete: {len(threats)} suspicious flows found")
        return threats

    except Exception as e:
        logger.error(f"Error during threat detection: {e}", exc_info=True)
        return []
