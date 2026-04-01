import streamlit as st
import pandas as pd

st.set_page_config(page_title="Excel Automation Tool", layout="wide")

st.title("🚀 Excel Automation Tool")
st.write("Upload Excel bestanden en krijg direct een clean rapport")

uploaded_files = st.file_uploader(
    "Upload Excel bestanden",
    accept_multiple_files=True,
    type=["xlsx"]
)

if uploaded_files:

    if st.button("Verwerken"):

        df_list = []

        for file in uploaded_files:
            try:
                data = pd.read_excel(file, header=None)

                data = data.dropna(axis=1, how="all")
                data = data.dropna(how="all")

                # header zoeken
                header_row = None
                for i, row in data.iterrows():
                    row_str = row.astype(str).str.lower()
                    if row_str.str.contains("naam").any():
                        header_row = i
                        break

                if header_row is None:
                    st.warning(f"Geen header gevonden in {file.name}")
                    continue

                data.columns = data.iloc[header_row]
                data = data[header_row + 1:]

                data.columns = data.columns.astype(str).str.strip().str.lower()

                cols = list(data.columns)

                # betere detectie
                naam_col = next((c for c in cols if "naam" in c or "name" in c), None)
                uren_col = next((c for c in cols if "uur" in c or "hour" in c), None)
                bedrag_col = next((c for c in cols if "bedrag" in c or "salaris" in c or "amount" in c), None)

                if not naam_col or not bedrag_col:
                    st.warning(f"Kolommen niet herkend in {file.name}")
                    continue

                data = data.rename(columns={
                    naam_col: "naam",
                    bedrag_col: "bedrag"
                })

                # 🔥 FIX: uren fallback slimmer
                if uren_col:
                    data = data.rename(columns={uren_col: "uren"})
                else:
                    # probeer automatisch kolom te vinden met kleine getallen
                    mogelijke_uren = data.select_dtypes(include=["number"]).columns.tolist()

                    if len(mogelijke_uren) > 0:
                        data = data.rename(columns={mogelijke_uren[0]: "uren"})
                    else:
                        data["uren"] = 0

                data = data[["naam", "uren", "bedrag"]]

                data["uren"] = pd.to_numeric(data["uren"], errors="coerce")
                data["bedrag"] = pd.to_numeric(data["bedrag"], errors="coerce")

                data = data.dropna()

                df_list.append(data)

            except Exception as e:
                st.error(f"Fout bij bestand: {file.name}")
                st.write(e)

        if df_list:
            combined_df = pd.concat(df_list, ignore_index=True)

            st.success("Klaar!")
            st.dataframe(combined_df, use_container_width=True)

            st.download_button(
                "Download resultaat",
                combined_df.to_csv(index=False).encode("utf-8"),
                "result.csv"
            )
        else:
            st.error("Geen geldige bestanden gevonden")