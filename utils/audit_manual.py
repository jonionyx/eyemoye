import pandas as pd
df = pd.read_csv("data/financial_data.csv")


def run_manual_audit(df):
    print("--- Starting Manaual Data Audit ---")
    # Check for Nulls
    null_count = df.isnull().sum().sum
    print(f"Total Missing Values: {null_count}")



    # Vectorized logic: Check for negative transaction amounts

    negatives = df[df['amount'] < 0]
    if not negatives.empty:
        print(f"Found {len(negatives)} negative transactions")


    # Schema check: Ensure transaction_id is unique
    if not df['transaction_id'].is_unique:
        print(f"Critical: Duplicate Transaction IDs found")


run_manual_audit(df)
