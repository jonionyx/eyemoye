import pandas as pd
import numpy as np


"""Generate data that simulate 'real-world" issues'
such as: missing values, negative prices, etc. so we can catch them.
"""

data = {
    'transaction_id': [101, 102, 103, 104, 105],
    'customer_id': ['C01', 'C02', 'C01', 'C03', 'C02' ],
    'amount': [150.50, -20.00, 300.00, np.nan, 450.25], # Issue: Negative & NaN
    'currency': ['GBP', 'GBP', 'USD', 'GBP', 'GBP'],
    'timestamp':  pd.to_datetime(['2023-10-01', '2023-10-01', '2023-10-02', '2023-10-02', '2023-10-03'])
}
df = pd.DataFrame(data)
df.to_csv("data/financial_data.csv", index=False)
print("financial_data.csv created with intentional errors")
