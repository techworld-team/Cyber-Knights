import pandas as pd
import os
import re

os.makedirs("data/processed", exist_ok=True)

input_path = "data/raw/Email.csv"
output_path = "data/processed/emails_clean.csv"

# Step 1: Read the whole file safely, ignoring encoding issues
with open(input_path, "rb") as f:
    raw_bytes = f.read()

text = raw_bytes.decode("utf-8", errors="ignore")

# Step 2: Split into rough "records"
lines = [line.strip() for line in text.splitlines() if line.strip()]

# Step 3: Try to extract any fields that look like emails or domains
emails, subjects, urls = [], [], []

email_pattern = re.compile(r"[\w\.-]+@[\w\.-]+\.\w+")
url_pattern = re.compile(r"https?://[^\s]+")

for line in lines:
    found_emails = email_pattern.findall(line)
    found_urls = url_pattern.findall(line)

    emails.append(", ".join(found_emails) if found_emails else None)
    urls.append(", ".join(found_urls) if found_urls else None)

# Step 4: Build DataFrame
df = pd.DataFrame({
    "raw_line": lines,
    "emails_found": emails,
    "urls_found": urls
})

# Step 5: Clean it up
df.drop_duplicates(inplace=True)
df.dropna(how="all", inplace=True)

# Step 6: Save
df.to_csv(output_path, index=False)
print(f"✅ Extracted structured data and saved to {output_path}")

