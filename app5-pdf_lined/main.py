from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("app5-pdf_lined/topics.csv")

#TOPIC PAGES
for index, row in df.iterrows():
    pdf.add_page()
    
    pdf.set_text_color(100, 100, 100)
    pdf.set_font(family="Times", style="B", size=24)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", 
             ln=1)
    
    #add lines
    for y in range(20, 290, 10):
        pdf.line(10, y, 200, y)
    
    #add lines alter
    # pdf.set_text_color(100, 100, 100)
    # y=31
    # for i in range(26):
    #     pdf.line(10, y, 200, y)
    #     y+=10
    
    #break line and set footer
    pdf.ln(260)
    
    pdf.set_text_color(180, 180, 180)
    pdf.set_font(family="Times", style="I", size=12)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="R", 
             ln=1)
    
    #EXTRA PAGES
    for i in range(row["Pages"] - 1):
        pdf.add_page()
        
        #add lines
        for y in range(20, 290, 10):
            pdf.line(10, y, 200, y)
        
        #add lines alter
        # pdf.set_text_color(100, 100, 100)
        # y=15
        # for i in range(28):
        #     pdf.line(10, y, 200, y)
        #     y+=10
        
        #break line and set footer
        pdf.ln(273.25)
        
        pdf.set_text_color(180, 180, 180)
        pdf.set_font(family="Times", style="I", size=12)
        pdf.cell(w=0, h=12, txt=row["Topic"], align="R", 
                 ln=1)
        
pdf.output("app5-pdf_lined/output.pdf")