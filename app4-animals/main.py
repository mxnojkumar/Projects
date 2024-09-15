from fpdf import FPDF
import pandas as pd
import glob
from pathlib import Path

pdf = FPDF(orientation="P", unit="mm", format="A4")

filepaths = glob.glob("app4-animals/Text+Files/*.txt")

for filepath in filepaths:
    filename = Path(filepath).stem
        
    with open(filepath, "r") as file:
        para = file.read()
    
    pdf.set_font(family="Times", style="B", size=20)
    pdf.add_page()
    pdf.cell(w=50, h=8, txt=f"{filename}".capitalize(), ln=1)
    
    pdf.set_font(family="Times", size=10)
    pdf.multi_cell(w=0, h=8, txt=para)
    
pdf.output(f"app4-animals/output.pdf")