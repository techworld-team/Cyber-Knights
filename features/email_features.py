import pandas as pd
import os
import re

os.makedirs("data/features", exist_ok=True)

df = pd.read_csv("data/processed/emails_clean.csv")

# Basic features
df["num_characters"] = df["raw_line"].astype(str).apply(len)
df["num_words"] = df["raw_line"].astype(str).apply(lambda x: len(x.split()))
df["has_link"] = df["raw_line"].astype(str).apply(lambda x: 1 if "http" in x else 0)
df["has_number"] = df["raw_line"].astype(str).apply(lambda x: 1 if re.search(r"\d", x) else 0)

df.to_csv("data/features/email_features.csv", index=False)
print("✅ Email features extracted → data/features/email_features.csv")
