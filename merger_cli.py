import pandas as pd
import glob
import sys

def clean_excel(file):
    df = pd.read_excel(file, header=None)

    df = df.dropna(axis=1, how="all")
    df = df.dropna(how="all")

    df = df.iloc[:, -2:]
    df = df[df.iloc[:,0].notna()]
    df = df[df.iloc[:,0] != "Naam"]

    df.columns = ["Naam", "Bedrag"]

    return df


# CLI argumenten
pattern = sys.argv[1]
output = sys.argv[2]

files = glob.glob(f"{pattern}*.xlsx")

df_list = []

for file in files:
    print(f"Processing {file}")
    df_list.append(clean_excel(file))

merged = pd.concat(df_list)

merged.to_excel(output, index=False)

print(f"✅ Rapport gemaakt: {output}")