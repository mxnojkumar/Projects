from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("app4-pdf/topics.csv")

for i, row in df.iterrows():
    pdf.add_page()
    
    pdf.set_text_color(100, 100, 100) #(r, g, b)
    pdf.set_font(family="Times", style="B",  size=24)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", 
             ln=1)
    pdf.line(10, 21, 200, 21) #(x1, y1, x2, y2)
    
    pdf.ln(260)
    
    #set footer
    pdf.set_font(family="Times", style="I", size=12)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="R", 
             ln=1)
    
    for i in range(row["Pages"] - 1):
        pdf.add_page()
        
        #set footer
        pdf.ln(273.25)
        pdf.set_font(family="Times", style="I", size=12)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=12, txt=row["Topic"], align="R", 
                 ln=1)

pdf.output("app4-pdf/output.pdf")