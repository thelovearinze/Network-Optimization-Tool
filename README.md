Network Optimization Tool
A Network Optimization Tool that automates the analysis of Azure NSG (Network Security Group) flow logs, detects potential threats, integrates with VirusTotal for threat intelligence, and provides visual insights to improve network security and efficiency.

Project Overview
This project demonstrates a cloud-based approach to monitoring and optimizing network traffic in Azure. The system automates:

Fetching Azure NSG Flow Logs from Azure Storage
Parsing logs into a structured format
Analyzing traffic to detect malicious/suspicious IPs
Querying Threat Intelligence (VirusTotal) for real-time risk assessment
Visualizing results with Python (Matplotlib)
Together, these steps highlight network bottlenecks, potential security threats, and provide the foundation for an intelligent, automated network optimization strategy.

Features
Automated NSG Flow Log Analysis
Threat Intelligence Integration (VirusTotal)
Automated Scripting for a complete pipeline:
Log retrieval
Log parsing
Threat analysis
Visualization
Dashboards & Graphs to show top malicious IPs, suspicious IPs, and threat-by-country
Prerequisites
Azure CLI installed and logged in
Azure Storage Account that stores NSG Flow Logs
VirusTotal API Key (or any threat intelligence provider’s key)
Python 3.x on your local machine
Git for version control
Technical Architecture
lua
Copy
Edit

Technologies
Azure
NSG Flow Logs
Blob Storage
Python 3.x
pandas, requests, matplotlib, json
VirusTotal (Threat Intelligence API)
Git / GitHub for version control
Project Structure
graphql
Copy
Edit
Network-Optimization-Tool/
├── venv/                          # Python Virtual Env (gitignored)
├── parse_flow_logs.py            # Parses raw flowlog.json into CSV
├── analyze_flow_logs.py          # Summarizes top blocked IPs, etc.
├── query_threat_intelligence.py  # Checks IPs against VirusTotal
├── save_threat_results.py        # Saves threat intelligence to CSV
├── visualize_threat_data.py      # Creates bar charts & other visuals
├── update_threat_database.py     # Orchestrates the entire pipeline
├── flowlog.json                  # Fetched raw NSG Flow Logs
├── flowlog.csv                   # Parsed CSV from logs
├── threat_intelligence_results.csv # Merged threat intelligence CSV
├── threat_intelligence_results.txt # Raw text for threat analysis
├── analysis_results.txt          # Summary from local analysis
└── README.md                     # This documentation
Setup Instructions
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/<YourUsername>/Network-Optimization-Tool.git
cd Network-Optimization-Tool
2. Create & Activate Virtual Environment
bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt  # If you created a requirements file
# Or manually:
pip install pandas requests matplotlib emoji
4. Configure Azure CLI & Log In
bash
Copy
Edit
az login
az account set --subscription "<YourSubscriptionID>"
5. Set Up VirusTotal API Key
Sign up at https://virustotal.com/
Copy your API Key
Open query_threat_intelligence.py and replace the placeholder with your key:
python
Copy
Edit
API_KEY = "your_api_key_here"
6. Run the Full Pipeline
bash
Copy
Edit
python3 update_threat_database.py
This script will:

Fetch the latest blob name from Azure Storage
Download the logs as flowlog.json
Parse them into flowlog.csv
Analyze traffic & produce analysis_results.txt
Query threat intelligence & produce threat_intelligence_results.txt
Save results to threat_intelligence_results.csv
Visualize data (top_malicious_ips.png, top_suspicious_ips.png, threat_by_country.png)
7. View the Visualizations
Open the .png files generated:

bash
Copy
Edit
open top_malicious_ips.png
open top_suspicious_ips.png
open threat_by_country.png
Potential Errors & Solutions
BlobNotFound

Occurs when the blob path is incorrect or logs are not generated yet.
Solution: Ensure the full resource path is used, or wait for logs to appear.
ModuleNotFoundError (pandas, requests, etc.)

Means packages are missing in your virtual environment.
Solution: Activate venv & run pip install again.
Authentication failed (VirusTotal)

Invalid or missing API key.
Solution: Update query_threat_intelligence.py with a valid API key.
Glyph Missing (Emoji warnings in Matplotlib)

Harmless font warnings about missing emojis.
Solution: Install an emoji-compatible font or remove emojis.
What We Learned
Azure NSG Flow Logs for network insights
Dynamic threat intelligence queries using VirusTotal
Data Parsing & Analysis with Python (pandas)
Automated Pipeline integration using scripts
Visualizations for immediate, actionable insights
Future Enhancements
Automated Remediation: Dynamically block malicious IPs in NSG rules.
Machine Learning: Predict anomalies or spikes in network traffic.
CI/CD Pipeline: Integrate with GitHub Actions to run tests & checks.
Scheduled (cron) runs or Azure Automation for hands-free updates.
