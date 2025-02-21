import pandas as pd

# Load the CSV file
df = pd.read_csv("flowlog.csv")

# Identify top blocked IPs
top_blocked_ips = df[df["action"] == "D"]["source_ip"].value_counts().head(10)

# Identify top allowed IPs
top_allowed_ips = df[df["action"] == "A"]["source_ip"].value_counts().head(10)

# Identify most used ports
top_ports = df["destination_port"].value_counts().head(10)

# Save the analysis results
with open("analysis_results.txt", "w") as f:
    f.write("🚫 Top Blocked IPs:\n")
    f.write(top_blocked_ips.to_string() + "\n\n")

    f.write("✅ Top Allowed IPs:\n")
    f.write(top_allowed_ips.to_string() + "\n\n")

    f.write("🔌 Most Used Destination Ports:\n")
    f.write(top_ports.to_string() + "\n")

print("✅ Analysis completed! Results saved in 'analysis_results.txt'")

