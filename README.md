# Azure Network Security & Threat Intelligence Tool

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=flat&logo=python)
![Azure](https://img.shields.io/badge/Azure-NSG_Flow_Logs-0078D4?style=flat&logo=microsoftazure)
![Security](https://img.shields.io/badge/Security-Threat_Intel-red?style=flat&logo=security)

A specialized cybersecurity tool that automates the analysis of **Azure Network Security Group (NSG) Flow Logs**. It detects suspicious traffic patterns (like SSH brute force or RDP exposure) and automatically cross-references attacker IPs with **VirusTotal's Threat Intelligence API**.

## Key Features

* **Automated Log Parsing**: Converts raw, complex Azure NSG JSON logs into structured data.
* **Pattern Recognition**: Identifies potential threats including:
    * SSH Brute Force attempts (Port 22)
    * RDP Exposure (Port 3389)
    * Unauthorized Telnet traffic (Port 23)
* **Automated Threat Intelligence**:
    * Automatically extracts attacker IPs.
    * Queries the **VirusTotal API** in real-time to verify malicious reputation.
    * Includes built-in **Rate Limiting** to respect API quotas.
* **Reporting**: Generates a CSV threat report and a detailed text summary of intelligence findings.

## Installation and Setup

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/thelovearinze/Network-Optimization-Tool.git
    cd Network-Optimization-Tool
    ```

2.  **Create a Virtual Environment** (Recommended)
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure API Key**
    Create a `.env` file in the root directory and add your VirusTotal API key:
    ```text
    API_KEY=your_virustotal_api_key_here
    ```

## Usage

Run the main pipeline:

```bash
python main.py
```

**Execution Flow:**
1.  The tool reads `flowlog.json`.
2.  It detects suspicious traffic patterns.
3.  It **automatically** sends the top suspicious IPs to VirusTotal.
4.  It saves two reports:
    * `threats_report.csv` (All detected anomalies)
    * `threat_intelligence_results.txt` (VirusTotal reputation data)

## Project Structure

* `main.py`: The central engine that orchestrates the pipeline.
* `log_parser.py`: Handles the ingestion of Azure JSON logs.
* `threat_detection.py`: Logic for identifying malicious patterns.
* `query_threat_intelligence.py`: Module for interacting with the VirusTotal API.
* `report_generator.py`: Helper module for CSV export.
* `requirements.txt`: List of python dependencies.

---
*Built by [Love Arinze](https://github.com/thelovearinze).*
