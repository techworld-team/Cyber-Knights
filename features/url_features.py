import pandas as pd
import os
import re

# --- Step 1: File paths ---
input_path = "data/processed/urls_clean.csv"
output_path = "data/features/url_features.csv"

# --- Step 2: Verify file existence ---
if not os.path.exists(input_path):
    raise FileNotFoundError(f"❌ File not found: {input_path}")

print(f"📥 Loading cleaned URL dataset from: {input_path}")

# --- Step 3: Load data safely ---
df = pd.read_csv(input_path, encoding="latin1", on_bad_lines="skip")
print(f"✅ Loaded {len(df)} rows")

# --- Step 4: Use correct URL column (based on your file) ---
if "urls_found" in df.columns:
    url_col = "urls_found"
elif "domains_found" in df.columns:
    url_col = "domains_found"
else:
    raise ValueError(f"❌ No valid URL column found. Columns in file: {df.columns.tolist()}")

print(f"✅ Using column: {url_col}")

# --- Step 5: Create new features ---
df["url_text"] = df[url_col].astype(str).str.lower()
df["url_length"] = df["url_text"].apply(len)
df["num_dots"] = df["url_text"].apply(lambda x: x.count('.'))
df["num_digits"] = df["url_text"].apply(lambda x: sum(ch.isdigit() for ch in x))
df["has_https"] = df["url_text"].apply(lambda x: 1 if "https" in x else 0)
df["has_ip"] = df["url_text"].apply(lambda x: 1 if re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', x) else 0)
df["has_hyphen"] = df["url_text"].apply(lambda x: 1 if "-" in x else 0)
df["num_slashes"] = df["url_text"].apply(lambda x: x.count("/"))
df["ends_with_php"] = df["url_text"].apply(lambda x: 1 if x.endswith(".php") else 0)

# --- Step 6: Save features file ---
os.makedirs(os.path.dirname(output_path), exist_ok=True)
df.to_csv(output_path, index=False, encoding="utf-8")

print(f"✅ URL features successfully created and saved to {output_path}")
print(df.head())

