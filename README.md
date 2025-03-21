# Network Optimization Tool

A smart and automated tool designed to optimize network security by analyzing Azure NSG (Network Security Group) flow logs, detecting potential threats via VirusTotal, and providing clear visual insights. This helps you strengthen security and improve efficiency without the hassle of manual analysis.

## Project Overview

This tool automates the following steps:
- **Fetching Azure NSG Flow Logs** from Azure Storage
- **Parsing logs** into a structured format
- **Detecting suspicious and malicious IPs**
- **Querying VirusTotal for threat intelligence**
- **Visualizing results** using Python's Matplotlib

By automating these steps, the tool helps pinpoint network bottlenecks, highlights potential threats, and enhances security operations in a smarter way.

## Features

- **Automated NSG Flow Log Retrieval** – No more manual downloads
- **Built-in Threat Intelligence** (VirusTotal integration)
- **Easy Data Analysis & Visualization** using pandas & Matplotlib
- **End-to-End Pipeline** – Everything runs in a structured flow
- **Security-Focused** – Flags and logs malicious traffic in real-time

## Prerequisites

Before getting started, make sure you have:
- **Azure CLI** installed and logged in
- **An Azure Storage Account** where NSG logs are stored
- **A VirusTotal API Key** (or another threat intelligence provider)
- **Python 3.x** installed on your local machine
- **Git** for version control

## Technical Architecture

### Technologies Used

- **Azure Services:**
  - NSG Flow Logs
  - Azure Blob Storage
- **Python 3.x** (with the following libraries):
  - `pandas` (data analysis)
  - `requests` (API calls)
  - `matplotlib` (visualization)
  - `python-dotenv` (environment management)
- **Threat Intelligence:**
  - VirusTotal API
- **Git/GitHub** for collaboration and version control.

## Project Structure

```
Network-Optimization-Tool/
├── venv/                          # Python Virtual Environment (gitignored)
├── parse_flow_logs.py             # Converts raw flow logs to CSV format
├── analyze_flow_logs.py           # Summarizes & extracts key insights
├── query_threat_intelligence.py   # Checks IPs against VirusTotal
├── save_threat_results.py         # Saves threat analysis results
├── visualize_threat_data.py       # Creates visual reports
├── update_threat_database.py      # Orchestrates the entire pipeline
├── flowlog.json                   # Raw NSG logs
├── flowlog.csv                    # Parsed logs in CSV format
├── threat_intelligence_results.txt# Raw VirusTotal output
├── threat_intelligence_results.csv# Final consolidated threat data
├── analysis_results.txt           # Summary of analysis
├── tests/                         # Contains unit tests
│   └── test_query_threat_intelligence.py
└── README.md                      # This documentation
```

## Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/<YourUsername>/Network-Optimization-Tool.git
cd Network-Optimization-Tool
```

### 2. Create & Activate a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate   # On macOS/Linux
# On Windows:
# venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
Make sure `requirements.txt` includes:
```
pandas
requests
matplotlib
python-dotenv
pytest (for testing)
```

### 4. Set Up Environment Variables
Create a `.env` file in the project root:
```bash
touch .env
```
Add your VirusTotal API Key to the `.env` file:
```
API_KEY=your-actual-virustotal-api-key
```
 **Make sure `.env` is in your `.gitignore` file** to avoid accidentally committing sensitive information.

### 5. Configure Azure CLI & Log In
```bash
az login
az account set --subscription "<YourSubscriptionID>"
```

### 6. Load the API Key in Your Code
Your `query_threat_intelligence.py` script will automatically pick up the API key from the `.env` file:
```python
from dotenv import load_dotenv
import os

load_dotenv()  # Loads environment variables from .env file
API_KEY = os.getenv("API_KEY")
```

### 7. Run the Full Pipeline
```bash
python3 update_threat_database.py
```
This script will:
- Retrieve the latest logs from Azure Storage.
- Convert logs into a structured CSV format.
- Analyze traffic and generate a summary report.
- Check suspicious IPs against VirusTotal.
- Save threat analysis results.
- Generate visual reports (`top_malicious_ips.png`, `threat_by_country.png`).

### 8. View Your Visual Reports
```bash
open top_malicious_ips.png
open top_suspicious_ips.png
open threat_by_country.png
```
(For Windows, open the images using an image viewer.)

## Running Tests
Before running tests, make sure your virtual environment is active.
```bash
pytest tests/
```
This will execute all unit tests in the `tests/` directory.

## Troubleshooting & Common Issues

### `BlobNotFound`
- Logs might not have been generated yet.
- **Fix:** Check your resource path or wait for logs to be available.

### `ModuleNotFoundError` (pandas, requests, etc.)
- Some dependencies might be missing.
- **Fix:** Ensure your virtual environment is active and reinstall packages.

### Authentication Error (VirusTotal)
- Your API key might be invalid or missing.
- **Fix:** Update your `.env` file with a valid API key and restart the script.

### Missing Fonts in Matplotlib
- Some platforms may not support emoji-based graphs.
- **Fix:** Install a compatible font or remove emojis from visualizations.

## Key Takeaways
- Automating NSG flow log analysis makes security monitoring much easier.
- VirusTotal API helps in real-time threat detection.
- Python + Azure CLI enables seamless integration with cloud security tools.
- Data visualization helps quickly identify security risks.

## Future Enhancements
- **Automated Remediation:** Block malicious IPs in NSG dynamically.
- **Machine Learning:** Predict anomalies in network traffic.
- **Scheduled Runs:** Automate everything with cron jobs or Azure Automation.
- **Web Dashboard:** A user-friendly dashboard for live monitoring.
