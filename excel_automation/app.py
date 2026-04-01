import streamlit as st
import pandas as pd

st.set_page_config(page_title="Excel Automation Tool", layout="wide")

st.title("🚀 Excel Automation Tool")
st.write("Upload Excel bestanden en krijg een clean samengevoegd rapport")

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

                # verwijder lege rijen/kolommen
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

                # header instellen
                data.columns = data.iloc[header_row]
                data = data[header_row + 1:]

                # kolomnamen clean
                data.columns = data.columns.map(lambda x: str(x).strip().lower())

                cols = list(data.columns)

                # kolommen zoeken (zonder data te veranderen)
                naam_col = next((c for c in cols if "naam" in str(c) or "name" in str(c)), None)
                uren_col = next((c for c in cols if "uur" in str(c) or "hour" in str(c)), None)
                bedrag_col = next((c for c in cols if "bedrag" in str(c) or "salaris" in str(c) or "amount" in str(c)), None)

                if not naam_col or not bedrag_col:
                    st.warning(f"Kolommen niet herkend in {file.name}")
                    continue

                # rename zonder data te veranderen
                rename_dict = {
                    naam_col: "naam",
                    bedrag_col: "bedrag"
                }

                if uren_col:
                    rename_dict[uren_col] = "uren"

                data = data.rename(columns=rename_dict)

                # alleen bestaande kolommen selecteren
                final_cols = ["naam", "bedrag"]
                if "uren" in data.columns:
                    final_cols.insert(1, "uren")

                data = data[final_cols]

                # alleen lege rijen weg
                data = data.dropna(subset=["naam", "bedrag"])

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