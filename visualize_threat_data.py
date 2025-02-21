import pandas as pd
import matplotlib.pyplot as plt

# Load threat intelligence results
df = pd.read_csv("threat_intelligence_results.csv")

# Convert NaN values to 0 (some IPs may have missing votes)
df.fillna(0, inplace=True)

# Plot Top Malicious IPs
top_malicious = df.sort_values(by="Malicious Votes", ascending=False).head(10)

plt.figure(figsize=(10, 5))
plt.bar(top_malicious["IP"], top_malicious["Malicious Votes"], color="red")
plt.xlabel("IP Address")
plt.ylabel("Malicious Votes")
plt.title("🔴 Top 10 Malicious IPs")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("top_malicious_ips.png")  # Save as an image
plt.show()

print("✅ Visualization saved as 'top_malicious_ips.png'")

# Plot Threat Activity by Country
country_counts = df["Country"].value_counts().head(10)

plt.figure(figsize=(10, 5))
plt.bar(country_counts.index, country_counts.values, color="purple")
plt.xlabel("Country")
plt.ylabel("Number of Threats")
plt.title("🌍 Threat Activity by Country")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("threat_by_country.png")  # Save as an image
plt.show()

# Plot Top Suspicious IPs
top_suspicious = df.sort_values(by="Suspicious Votes", ascending=False).head(10)

plt.figure(figsize=(10, 5))
plt.bar(top_suspicious["IP"], top_suspicious["Suspicious Votes"], color="orange")
plt.xlabel("IP Address")
plt.ylabel("Suspicious Votes")
plt.title("🟠 Top 10 Suspicious IPs")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("top_suspicious_ips.png")  # Save as an image
plt.show()

print("✅ Visualization saved as 'top_suspicious_ips.png'")

