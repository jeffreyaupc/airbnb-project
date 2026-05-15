# ============================================================
# WEEK 1 — Toronto Airbnb Data Explorer
# Goal: Load the data, understand its shape, find what's broken
# ============================================================
#
# SETUP — run this once in your terminal before anything else:
#   pip install pandas
#
# DATA — download the Toronto listings CSV from:
#   http://insideairbnb.com/get-the-data/
#   → Find "Toronto" → download "listings.csv.gz"
#   → Put it in the same folder as this script
#   → No need to unzip — pandas reads .gz directly
# ============================================================

import pandas as pd

# ── 1. LOAD ──────────────────────────────────────────────────
# If you unzipped it manually, change the filename to 'listings.csv'
df = pd.read_csv('listings.csv', low_memory=False)

print("=" * 55)
print("STEP 1: Basic shape")
print("=" * 55)
print(f"Rows    : {df.shape[0]:,}")
print(f"Columns : {df.shape[1]}")


# ── 2. COLUMN NAMES ──────────────────────────────────────────
print("\n" + "=" * 55)
print("STEP 2: All column names")
print("=" * 55)
for col in df.columns:
    print(f"  {col}")


# ── 3. DATA TYPES ────────────────────────────────────────────
print("\n" + "=" * 55)
print("STEP 3: Column data types")
print("(Watch for columns that SHOULD be numbers but show 'object')")
print("=" * 55)
print(df.dtypes.to_string())


# ── 4. MISSING VALUES ────────────────────────────────────────
print("\n" + "=" * 55)
print("STEP 4: Missing values — columns with ANY nulls")
print("=" * 55)
missing = df.isnull().sum()
missing = missing[missing > 0].sort_values(ascending=False)

if missing.empty:
    print("  No missing values found.")
else:
    for col, count in missing.items():
        pct = (count / len(df)) * 100
        print(f"  {col:<40} {count:>6,} missing  ({pct:.1f}%)")


# ── 5. PRICE COLUMN PROBLEM ──────────────────────────────────
# The price column comes in as a string like "$150.00"
# This is one of the first things you'll fix in Week 2
print("\n" + "=" * 55)
print("STEP 5: The price column (this is intentionally broken)")
print("=" * 55)
if 'price' in df.columns:
    print(f"  Data type  : {df['price'].dtype}")
    print(f"  Sample values:")
    for val in df['price'].dropna().head(8).values:
        print(f"    {val}")
    print("\n  ⚠ Notice it's a string with '$' and ',' — not a number.")
    print("  You'll fix this in Week 2.")
else:
    print("  'price' column not found — column may be named differently.")
    print("  Check the column list above.")


# ── 6. KEY COLUMNS PREVIEW ───────────────────────────────────
# These are the columns you'll use most throughout the project
key_cols = [
    'id', 'name', 'neighbourhood_cleansed', 'room_type',
    'price', 'minimum_nights', 'number_of_reviews',
    'review_scores_rating', 'availability_365', 'host_id'
]

existing_key_cols = [c for c in key_cols if c in df.columns]

print("\n" + "=" * 55)
print("STEP 6: Preview of key columns (first 5 rows)")
print("=" * 55)
print(df[existing_key_cols].head(5).to_string(index=False))


# ── 7. NEIGHBOURHOODS ────────────────────────────────────────
print("\n" + "=" * 55)
print("STEP 7: Unique neighbourhoods")
print("=" * 55)
if 'neighbourhood_cleansed' in df.columns:
    neighbourhoods = df['neighbourhood_cleansed'].value_counts()
    print(f"  Total unique neighbourhoods: {len(neighbourhoods)}")
    print(f"\n  Top 10 by listing count:")
    for name, count in neighbourhoods.head(10).items():
        print(f"    {name:<35} {count:>5,} listings")
else:
    print("  Column 'neighbourhood_cleansed' not found.")


# ── 8. ROOM TYPES ────────────────────────────────────────────
print("\n" + "=" * 55)
print("STEP 8: Room type breakdown")
print("=" * 55)
if 'room_type' in df.columns:
    room_counts = df['room_type'].value_counts()
    for rtype, count in room_counts.items():
        pct = (count / len(df)) * 100
        print(f"  {rtype:<30} {count:>6,}  ({pct:.1f}%)")


# ── 9. YOUR NOTES ────────────────────────────────────────────
print("\n" + "=" * 55)
print("STEP 9: Your homework")
print("=" * 55)
print("""
  After running this script, write down answers to:

  1. How many listings are in the dataset?
  2. Which neighbourhood has the most listings?
  3. What percentage of listings are 'Entire home/apt'?
  4. Name 3 columns that have significant missing data.
  5. Why can't you do math on the price column right now?

  You'll fix problem #5 in Week 2.
  Keep these notes — your README will use them later.
""")

print("=" * 55)
print("Week 1 complete. You just explored a real dataset.")
print("=" * 55)