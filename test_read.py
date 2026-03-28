import pandas as pd

df = pd.read_excel("sales1.xlsx", header=None)

df = df.dropna(axis=1, how="all")
df = df.dropna(how="all")

df = df.iloc[:, -2:]

# verwijder lege naam rijen
df = df[df.iloc[:,0].notna()]

# verwijder header rij die als data staat
df = df[df.iloc[:,0] != "Naam"]

df = df.reset_index(drop=True)

df.columns = ["Naam", "Bedrag"]

print(df)