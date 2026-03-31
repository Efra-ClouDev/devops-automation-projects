import pandas as pd
import glob

files = glob.glob("input/*.xlsx")

df_list = []

for file in files:
    print(f"Processing {file}")

    data = pd.read_excel(file)

    print("Kolommen:", data.columns.tolist())

    # kolomnamen opschonen (belangrijk!)
    data.columns = data.columns.str.strip()

    # check of kolommen bestaan
    required = ["Naam", "Uren", "Bedrag"]
    if not all(col in data.columns for col in required):
        print(f"❌ Bestand overgeslagen: {file}")
        continue

    # alleen juiste kolommen pakken
    data = data[required]

    # lege rijen weg
    data = data.dropna(how="all")

    # alleen geldige rijen
    data = data[data["Naam"].notna()]

    # cijfers opschonen
    data["Uren"] = pd.to_numeric(data["Uren"], errors="coerce")
    data["Bedrag"] = pd.to_numeric(data["Bedrag"], errors="coerce")

    data = data.dropna()

    df_list.append(data)

# alles samenvoegen
merged = pd.concat(df_list)

merged.to_excel("output/result.xlsx", index=False)

print("✅ Alles netjes verwerkt!")
