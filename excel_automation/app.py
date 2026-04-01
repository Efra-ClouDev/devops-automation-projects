import streamlit as st
import pandas as pd

st.set_page_config(page_title="Excel Automation Tool", layout="wide")

st.title("🚀 Excel Automation Tool")
st.write("Upload Excel bestanden → opschonen + samenvoegen zonder dataverlies")

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

                # lege rijen/kolommen verwijderen
                data = data.dropna(axis=1, how="all")
                data = data.dropna(how="all")

                # header zoeken (eerste rij met tekst)
                header_row = None
                for i, row in data.iterrows():
                    if row.astype(str).str.contains("[a-zA-Z]").any():
                        header_row = i
                        break

                if header_row is None:
                    st.warning(f"Geen header gevonden in {file.name}")
                    continue

                # header instellen
                data.columns = data.iloc[header_row]
                data = data[header_row + 1:]

                # kolomnamen opschonen
                data.columns = (
                    data.columns
                    .map(lambda x: str(x).strip().lower())
                    .str.replace(" ", "_")
                )

                # alleen lege rijen verwijderen
                data = data.dropna(how="all")

                # voeg bronbestand toe
                data["bronbestand"] = file.name

                df_list.append(data)

            except Exception as e:
                st.error(f"Fout bij bestand: {file.name}")
                st.write(e)

        if df_list:
            # 🔥 BELANGRIJK: kolommen samenvoegen (union)
            combined_df = pd.concat(df_list, ignore_index=True, sort=False)

            st.success("Klaar! Alle kolommen behouden ✅")
            st.dataframe(combined_df, use_container_width=True)

            st.download_button(
                "Download resultaat",
                combined_df.to_csv(index=False).encode("utf-8"),
                "result.csv"
            )
        else:
            st.error("Geen geldige bestanden gevonden")