import pandas as pd

data = pd.read_excel("data.xlsx")

data = data.dropna()

data = data.sort_values(by=data.columns[0])

data.to_excel("clean_data.xlsx", index=False)

print("Excel opgeschoond!")

import pandas as pd
df = pd.read_excel("clean_data.xlsx")
print(df)