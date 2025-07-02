# Network Optimization Tool

> Automated Azure NSG Log Analysis + Threat Detection

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Build](https://img.shields.io/badge/build-passing-brightgreen)
![CLI Tool](https://img.shields.io/badge/Interface-CLI-orange)

## Project Overview

A smart and automated tool designed to optimize network security by analyzing Azure NSG (Network Security Group) flow logs, detecting potential threats via VirusTotal, and providing clear visual insights. This helps you strengthen security and improve efficiency without the hassle of manual analysis.

![demo](screenshots/demo.gif)

## Features

* **Automated NSG Flow Log Retrieval** – No more manual downloads
* **Built-in Threat Intelligence** (VirusTotal integration)
* **Easy Data Analysis & Visualization** using pandas & Matplotlib
* **End-to-End Pipeline** – Everything runs in a structured flow
* **Security-Focused** – Flags and logs malicious traffic in real-time
* **CLI Support** – Run the tool with flexible input/output arguments

## Prerequisites

Before getting started, make sure you have:

* **Azure CLI** installed and logged in
* **An Azure Storage Account** where NSG logs are stored
* **A VirusTotal API Key** (or another threat intelligence provider)
* **Python 3.x** installed on your local machine
* **Git** for version control

## Technical Architecture

### Technologies Used

* **Azure Services:**

  * NSG Flow Logs
  * Azure Blob Storage
* **Python 3.x** (with the following libraries):

  * `pandas` (data analysis)
  * `requests` (API calls)
  * `matplotlib` (visualization)
  * `python-dotenv` (environment management)
* **Threat Intelligence:**

  * VirusTotal API
* **Git/GitHub** for collaboration and version control.

## Project Structure

```
Network-Optimization-Tool/
├── venv/                          # Python Virtual Environment (gitignored)
├── main.py                        # CLI entry point
├── parse_flow_logs.py             # Converts raw flow logs to structured format
├── threat_detection.py            # Flags suspicious traffic patterns
├── report_generator.py            # Saves results to CSV (default: threats_report.csv)
├── flowlog.json                   # Sample raw NSG logs
├── threats_report.csv             # Default threat report
├── requirements.txt               # Python dependencies
├── .env                           # API key & config (gitignored)
└── README.md                      # This documentation
```

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/thelovearinze/Network-Optimization-Tool.git
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

Ensure `requirements.txt` includes:

```
pandas
requests
matplotlib
python-dotenv
```

### 4. Set Up Environment Variables

```bash
touch .env
```

Add to `.env`:

```
API_KEY=your-virustotal-api-key
```

### 5. Run the Tool

#### Default usage:

```bash
python3 main.py
```

#### Custom input/output:

```bash
python3 main.py --input flowlog.json --output my_custom_report.csv
```

The tool will:

* Parse the NSG logs
* Detect suspicious traffic
* Log and save findings to a report

## Viewing the Report

Open `threats_report.csv` or your custom report in Excel or VS Code to review flagged entries.

## Running Tests (if test suite is added)

```bash
pytest tests/
```

## Troubleshooting

### `ModuleNotFoundError`

* Make sure you're in the virtual environment
* Run `pip install -r requirements.txt` again

### Invalid VirusTotal Key

* Double-check `.env` file for the correct API key

### CLI Usage Help

```bash
python3 main.py --help
```

## Known Limitations

* IPv6 traffic is currently not parsed
* VirusTotal API has daily request limits
* Only JSON-formatted NSG logs are supported

## Contributing

Contributions are welcome!

To get started:

* Fork the repository
* Create a new branch
* Make your changes
* Submit a pull request

Please include tests or run the tool before pushing any major change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Future Enhancements

* **Auto-Blocking**: Integrate with Azure NSG rules to block threats
* **Machine Learning**: Anomaly-based traffic detection
* **Web Dashboard**: For real-time visualization
* **Scheduled Jobs**: Automate runs with cron or Azure Functions

---

**Built by [Love Arinze](https://github.com/thelovearinze) for security teams, developers, and network engineers who want clarity, speed, and actionable insight.**
