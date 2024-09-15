from fpdf import FPDF
import pandas as pd
import glob
from pathlib import Path

filepaths = glob.glob("app4-excel_to_pdf/invoices/*.xlsx")

# Main loop to iterate over each file
for filepath in filepaths:
    
    filename = Path(filepath).stem
    invoice_nr, date = filename.split("-")
    
    # Invoice number and Date
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=20)
    pdf.cell(w=50, h=8, txt=f"Invoice nr.{invoice_nr}", ln=1)
    pdf.cell(w=50, h=8, txt=f"Date: {date}", ln=1)

    # Headers
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    columns = df.columns
    columns = [i.replace("_", " ").title() for i in columns]
    pdf.set_font(family="Times", style="B", size=10)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt=columns[0], border=1)
    pdf.cell(w=65, h=8, txt=columns[1], border=1)
    pdf.cell(w=35, h=8, txt=columns[2], border=1)
    pdf.cell(w=30, h=8, txt=columns[3], border=1)
    pdf.cell(w=30, h=8, txt=columns[4], border=1, ln=1)

    # Content under headers
    for index, row in df.iterrows():
        pdf.set_font(family="Times", size=10)
        pdf.set_text_color(80, 80, 80)
        pdf.cell(w=30, h=8, txt=str(row['product_id']), border=1)
        pdf.cell(w=65, h=8, txt=str(row['product_name']), border=1)
        pdf.cell(w=35, h=8, txt=str(row['amount_purchased']), border=1)
        pdf.cell(w=30, h=8, txt=str(row['price_per_unit']), border=1)
        pdf.cell(w=30, h=8, txt=str(row['total_price']), border=1, ln=1)
    
    # Total price row
    total_sum = df['total_price'].sum()    
    pdf.set_font(family="Times", size=10)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt='', border=1)
    pdf.cell(w=65, h=8, txt='', border=1)
    pdf.cell(w=35, h=8, txt='', border=1)
    pdf.cell(w=30, h=8, txt='', border=1)
    pdf.cell(w=30, h=8, txt=str(total_sum), border=1, ln=1)
    
    # Total price sentence
    pdf.set_font(family="Times", style="B", size=10)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt=f"The total price is {total_sum}", ln=1)
    
    # Company name and logo
    pdf.set_font(family="Times", style="B", size=14)
    pdf.cell(w=25, h=8, txt="PythonHow")
    pdf.image("app4-excel_to_pdf/pythonhow.png", w=10)
    
    pdf.output(f"app4-excel_to_pdf/PDFs/{filename}.pdf")