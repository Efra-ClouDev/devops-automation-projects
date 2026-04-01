import streamlit as st
import pandas as pd

st.title("🚀 Excel Automation Tool")

uploaded_files = st.file_uploader(
    "Upload Excel bestanden",
    accept_multiple_files=True
)

if uploaded_files:
    df_list = []

    for file in uploaded_files:
        try:
            data = pd.read_excel(file, header=None)

            data = data.dropna(axis=1, how="all")
            data = data.dropna(how="all")

            data = data.iloc[:, -3:]
            data.columns = ["naam", "uren", "bedrag"]

            df_list.append(data)

        except:
            st.error(f"Fout bij bestand: {file.name}")

    if st.button("Verwerken"):
        if df_list:
            merged = pd.concat(df_list)

            st.success("Klaar!")
            st.dataframe(merged)

            st.download_button(
                "Download resultaat",
                merged.to_csv(index=False).encode("utf-8"),
                "result.csv"
            )
        else:
            st.error("Geen geldige bestanden")