import streamlit as st
import pandas as pd

st.title("🚀 Excel Automation Tool")
st.markdown("Upload Excel bestanden en krijg direct een clean rapport")

uploaded_files = st.file_uploader(
    "Upload Excel bestanden",
    accept_multiple_files=True,
    type=["xlsx"]
)

def normalize_columns(columns):
    return [str(col).strip().lower() for col in columns]

def map_columns(columns):
    mapping = {}
    
    for col in columns:
        if any(x in col for x in ["naam", "name", "employee", "persoon"]):
            mapping[col] = "naam"
        elif any(x in col for x in ["bedrag", "amount", "salary", "total"]):
            mapping[col] = "bedrag"
        elif any(x in col for x in ["uren", "hours", "time"]):
            mapping[col] = "uren"
    
    return mapping

if uploaded_files:

    if st.button("Verwerken"):

        df_list = []

        for file in uploaded_files:
            try:
                data = pd.read_excel(file)

                data.columns = normalize_columns(data.columns)
                mapping = map_columns(data.columns)

                data = data.rename(columns=mapping)

                if "naam" not in data.columns or "bedrag" not in data.columns:
                    st.warning(f"⚠️ Kolommen niet herkend in {file.name}")
                    continue

                if "uren" not in data.columns:
                    data["uren"] = 0

                data = data[["naam", "uren", "bedrag"]]

                data["uren"] = pd.to_numeric(data["uren"], errors="coerce")
                data["bedrag"] = pd.to_numeric(data["bedrag"], errors="coerce")

                data = data.dropna()

                df_list.append(data)

            except Exception as e:
                st.error(f"❌ Fout bij bestand: {file.name}")
                st.write(e)

        if df_list:
            combined_df = pd.concat(df_list, ignore_index=True)

            st.success("✅ Klaar!")
            st.dataframe(combined_df)

            st.download_button(
                "Download resultaat",
                combined_df.to_csv(index=False).encode("utf-8"),
                "result.csv"
            )
        else:
            st.error("❌ Geen geldige bestanden gevonden")