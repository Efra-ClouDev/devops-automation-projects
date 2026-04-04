import streamlit as st
import pandas as pd
from docx import Document
import io

# Functie voor de conversie
def convert_word_to_excel(word_file):
    doc = Document(word_file)
    all_data = []

    for table in doc.tables:
        for row in table.rows:
            row_data = [cell.text.strip() for cell in row.cells]
            all_data.append(row_data)

    if not all_data:
        return None

    # Eerste rij als header gebruiken
    df = pd.DataFrame(all_data[1:], columns=all_data[0])

    output = io.BytesIO()

    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False)

        worksheet = writer.sheets['Sheet1']

        # Auto column width
        for column_cells in worksheet.columns:
            length = max(len(str(cell.value)) for cell in column_cells if cell.value)
            worksheet.column_dimensions[column_cells[0].column_letter].width = length + 2

    return output.getvalue()


# Streamlit Interface
st.title("📄 Word naar Excel Converter")
st.write("Gemaakt voor mijn DevOps portfolio")

uploaded_file = st.file_uploader("Upload een Word-bestand (.docx)", type="docx")

if uploaded_file:
    excel_data = convert_word_to_excel(uploaded_file)

    if excel_data:
        st.success("Conversie geslaagd!")
        st.download_button(
            label="📥 Download Excel",
            data=excel_data,
            file_name="geconverteerd.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
    else:
        st.warning("Geen tabellen gevonden in dit document.")