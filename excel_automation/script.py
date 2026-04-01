import pandas as pd
import glob

files = glob.glob("input/*.xlsx")

df_list = []

for file in files:
    print(f"Processing {file}")

    data = pd.read_excel(file, header=None)

    # lege kolommen en rijen weg
    data = data.dropna(axis=1, how="all")
    data = data.dropna(how="all")

    # zoek header rij
    header_row = None
    for i, row in data.iterrows():
        if row.astype(str).str.lower().str.contains("naam").any():
            header_row = i
            break

    if header_row is None:
        print(f"❌ Geen header gevonden in {file}")
        continue

    data.columns = data.iloc[header_row]
    data = data[header_row + 1:]

    # kolommen opschonen
    data.columns = data.columns.astype(str).str.strip().str.lower()

    mapping = {
        "naam": "naam",
        "name": "naam",
        "uren": "uren",
        "hours": "uren",
        "bedrag": "bedrag",
        "amount": "bedrag"
    }

    data = data.rename(columns=mapping)

    required = ["naam", "uren", "bedrag"]

    if not all(col in data.columns for col in required):
        print(f"❌ Bestand overgeslagen: {file}")
        print("Kolommen gevonden:", data.columns.tolist())
        continue

    data = data[required]

    # opschonen data
    data["uren"] = pd.to_numeric(data["uren"], errors="coerce")
    data["bedrag"] = pd.to_numeric(data["bedrag"], errors="coerce")
    data = data.dropna()

    df_list.append(data)

if not df_list:
    print("❌ Geen geldige bestanden gevonden")
    exit()

merged = pd.concat(df_list)

merged.to_excel("output/result.xlsx", index=False)

print("✅ Alles netjes verwerkt!")