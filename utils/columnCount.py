import pandas as pd
url = "https://raw.githubusercontent.com/greatexpectationslabs/tutorial-gx-in-the-data-pipeline/refs/heads/main/cookbooks/data/raw/products.csv"
df = pd.read_csv(url, index_col="ProductKey")
print(df.head(10))

# count = (df['passenger_count'] == 1).sum()
# print("Number of occurrences of '1' in 'passenger_count':"), count