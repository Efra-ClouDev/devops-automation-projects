import pandas as pd
import glob

def clean_excel(file):
    df = pd.read_excel(file, header=None)

    df = df.dropna(axis=1, how="all")
    df = df.dropna(how="all")

    df = df.iloc[:, -2:]

    df = df[df.iloc[:,0].notna()]
    df = df[df.iloc[:,0] != "Naam"]

    df.columns = ["Naam", "Bedrag"]

    return df


files = glob.glob("sales*.xlsx")

df_list = []

for file in files:
    print(f"Processing {file}")
    clean_df = clean_excel(file)
    df_list.append(clean_df)

merged = pd.concat(df_list)

merged.to_excel("merged_report.xlsx", index=False)

print("✅ Alle bestanden cleaned en gemerged!")