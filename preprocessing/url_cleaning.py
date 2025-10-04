import pandas as pd
import os
import re

os.makedirs("data/processed", exist_ok=True)

input_path = "data/raw/url.csv"
output_path = "data/processed/urls_clean.csv"

# Step 1: Read the file safely, ignoring bad encodings
with open(input_path, "rb") as f:
    raw_bytes = f.read()

text = raw_bytes.decode("utf-8", errors="ignore")

# Step 2: Split into rough "records"
lines = [line.strip() for line in text.splitlines() if line.strip()]

# Step 3: Extract URLs and domains
url_pattern = re.compile(r"https?://[^\s'\"<>]+")
domain_pattern = re.compile(r"https?://([^/\s]+)")

urls, domains = [], []

for line in lines:
    found_urls = url_pattern.findall(line)
    found_domains = domain_pattern.findall(line)

    urls.append(", ".join(found_urls) if found_urls else None)
    domains.append(", ".join(found_domains) if found_domains else None)

# Step 4: Build DataFrame
df = pd.DataFrame({
    "raw_line": lines,
    "urls_found": urls,
    "domains_found": domains
})

# Step 5: Clean it up
df.drop_duplicates(inplace=True)
df.dropna(how="all", inplace=True)

# Step 6: Save
df.to_csv(output_path, index=False)
print(f"✅ URL data extracted and saved to {output_path}")

