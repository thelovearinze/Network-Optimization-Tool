# Network Optimization Tool

A **Network Optimization Tool** that automates the analysis of **Azure NSG (Network Security Group) flow logs**, detects potential threats via **VirusTotal**, and provides visual insights to strengthen **network security and efficiency**.

## Project Overview
This system automates:
1. **Fetching** Azure NSG Flow Logs from Azure Storage  
2. **Parsing** logs into a structured format  
3. **Detecting** malicious & suspicious IPs  
4. **Querying** threat intelligence (VirusTotal)  
5. **Visualizing** results with Python’s Matplotlib  

Ultimately, it highlights **network bottlenecks**, **threat sources**, and fosters an **intelligent, automated** approach to network optimization.

## Features
- **Automated NSG Flow Log Retrieval**
- **Threat Intelligence Integration** (VirusTotal)
- **Data Analysis & Visualization** (pandas & matplotlib)
- **End-to-End Pipeline** with scripts for each stage
- **Security-Focused**: Identifies malicious IPs and suspicious traffic

## Prerequisites
- **Azure CLI** installed and logged in
- **Azure Storage Account** storing NSG flow logs
- **VirusTotal API Key** (or another threat intelligence provider)
- **Python 3.x** on your local machine
- **Git** for version control

## Technical Architecture


## Technologies Used
- **Azure**
  - NSG Flow Logs
  - Azure Blob Storage
- **Python 3.x**
  - `pandas`, `requests`, `matplotlib`
- **Threat Intelligence**
  - VirusTotal API
- **Git/GitHub** for collaboration

## Project Structure
```
Network-Optimization-Tool/
├── venv/                          # Python Virtual Env (gitignored)
├── parse_flow_logs.py            # Converts flowlog.json to CSV
├── analyze_flow_logs.py          # Summarizes & extracts top blocked IPs
├── query_threat_intelligence.py  # Checks IPs against VirusTotal
├── save_threat_results.py        # Saves final threat data to CSV
├── visualize_threat_data.py      # Graphs malicious/suspicious traffic
├── update_threat_database.py     # Orchestrates the entire pipeline
├── flowlog.json                  # Fetched raw NSG logs
├── flowlog.csv                   # Parsed logs in CSV format
├── threat_intelligence_results.txt # VirusTotal raw output
├── threat_intelligence_results.csv # Final consolidated threat data
├── analysis_results.txt          # Output from local analysis
└── README.md                     # This documentation
```

## Setup Guide

### 1. Clone the Repository
```bash
git clone https://github.com/<YourUsername>/Network-Optimization-Tool.git
cd Network-Optimization-Tool
```

### 2. Create & Activate Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
```

### 3. Install Dependencies
```bash
pip install pandas requests matplotlib emoji
# If using a requirements file:
pip install -r requirements.txt
```

### 4. Configure Azure CLI & Log In
```bash
az login
az account set --subscription "<YourSubscriptionID>"
```

### 5. Set Your VirusTotal API Key
Open `query_threat_intelligence.py` and replace the placeholder:
```python
API_KEY = "your-api-key-here"
```

### 6. Run the Full Pipeline
```bash
python3 update_threat_database.py
```
This will:
- Fetch the latest blob name from Azure Storage
- Download logs as `flowlog.json`
- Parse them into `flowlog.csv`
- Analyze traffic & produce `analysis_results.txt`
- Query threat intelligence & produce `threat_intelligence_results.txt`
- Save results to `threat_intelligence_results.csv`
- Generate visual reports (`top_malicious_ips.png`, `threat_by_country.png`)

### 7. View the Visualizations
```bash
open top_malicious_ips.png\open top_suspicious_ips.png
open threat_by_country.png
```
(For Windows, use an image viewer.)

## Potential Errors & Solutions
- **BlobNotFound**: Logs may not be generated yet.
  - _Fix_: Ensure the correct resource path or wait for logs.
- **ModuleNotFoundError (pandas, requests, etc.)**: Missing dependencies.
  - _Fix_: Activate virtual environment and reinstall packages.
- **Authentication Error (VirusTotal)**: Invalid API key.
  - _Fix_: Update `query_threat_intelligence.py` with a valid API key.
- **Glyph Missing Warnings (Matplotlib)**: Missing emoji fonts.
  - _Fix_: Install an emoji-compatible font or remove emojis.

## What We Learned
- How to parse **Azure NSG Flow Logs** for network insights
- Integrating **Python** with **Azure CLI**
- Using **VirusTotal** for real-time threat analysis
- **Automating network security optimization**
- **Data Visualization** for quick insights

## Future Enhancements
- **Automated Remediation**: Dynamically block malicious IPs in NSG.
- **Machine Learning**: Predict anomalies in network traffic.
- **Scheduled Runs**: Automate with cron jobs or Azure Automation.
- **Web Dashboard**: A user-friendly interface for monitoring threats.





