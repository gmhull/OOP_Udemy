from fpdf import FPDF

pdf = FPDF(orientation='P', unit='pt', format='A4')
pdf.add_page()

pdf.set_font(family='Times', size=24, style='B')
pdf.cell(w=100, h=80, txt="Flatmates Bill", border=1, align='C')
pdf.cell(w=50, h=40, txt="Period", border=1, align='')

pdf.output("bill.pdf")
