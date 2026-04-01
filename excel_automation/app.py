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
                # lees bestand
                data = pd.read_excel(file, header=None)

                # verwijder lege rijen/kolommen
                data = data.dropna(axis=1, how="all")
                data = data.dropna(how="all")

                # zoek header rij (waar 'naam' voorkomt)
                header_row = None
                for i, row in data.iterrows():
                    row_str = row.astype(str).str.lower()
                    if row_str.str.contains("naam").any():
                        header_row = i
                        break

                if header_row is None:
                    st.warning(f"Geen header gevonden in {file.name}")
                    continue

                # zet header
                data.columns = data.iloc[header_row]
                data = data[header_row + 1:]

                # clean kolomnamen
                data.columns = data.columns.astype(str).str.strip().str.lower()

                # FLEXIBELE kolom detectie
                cols = list(data.columns)

                naam_col = next((c for c in cols if "naam" in c), None)
                uren_col = next((c for c in cols if "uur" in c), None)
                bedrag_col = next((c for c in cols if "bedrag" in c or "salaris" in c or "amount" in c), None)

                if not naam_col or not bedrag_col:
                    st.warning(f"Kolommen niet herkend in {file.name}")
                    continue

                # hernoem kolommen
                data = data.rename(columns={
                    naam_col: "naam",
                    bedrag_col: "bedrag"
                })

                if uren_col:
                    data = data.rename(columns={uren_col: "uren"})
                else:
                    data["uren"] = 0

                # selecteer kolommen
                data = data[["naam", "uren", "bedrag"]]

                # convert types
                data["uren"] = pd.to_numeric(data["uren"], errors="coerce")
                data["bedrag"] = pd.to_numeric(data["bedrag"], errors="coerce")

                # drop lege rijen
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