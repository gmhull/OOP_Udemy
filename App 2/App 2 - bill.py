"""
Title: Flatmates bill
Description: An app that gets an input of bill amount and periods of times that
the flatmates were at the house during the period.  It returns how much each
flatmate will have to pay.  It will generate a PDF report stating the names, period,
and how much they have to pay.
Objects: Bill, Flatmate,
"""
from fpdf import FPDF
import webbrowser, os

class Bill:
    """
    Object that contains data about a bill.  Total amount and period of bill.
    """
    def __init__(self, amount, period):
        self.amount = amount
        self.period = period

class Flatmate:
    """
    Object that holds the data specific to each flatmate.  Name and days living
    in the house.
    """
    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pay(self, bill, flatmate):
        weight = self.days_in_house / (self.days_in_house + flatmate.days_in_house)
        return bill.amount * weight

class PDFReport:
    """
    Object that creates a PDF report to present the flatmates, bill amount, and
    period in a PDF report.
    """
    def __init__(self, filename):
        self.filename = filename

    def generate_PDF(self, flatmate1, flatmate2, bill):
        flatmate_1_payment = str(round(flatmate1.pay(bill, flatmate2),2))
        flatmate_2_payment = str(round(flatmate2.pay(bill, flatmate1),2))

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Add image icon
        pdf.image("files/Patty.jpg", w=40, h=40)

        # Insert Title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, align='C', ln=1)

        # Add Period
        pdf.set_font(family='Times', size=14, style="B")
        pdf.cell(w=100, h=40, txt="Period:", border=0)
        pdf.cell(w=200, h=40, txt=bill.period, border=0, ln=1)

        # Add Flatmate 1
        pdf.set_font(family='Times', size=12)
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=100, h=25, txt=flatmate_1_payment, border=0, ln=1)

        # Add Flatmate 2
        pdf.cell(w=100, h=25, txt=flatmate2.name, border=0)
        pdf.cell(w=100, h=25, txt=flatmate_2_payment, border=0, ln=1)

        # Change directory, save pdf, and open the pdf
        os.chdir("files")
        pdf.output(self.filename)
        webbrowser.open(self.filename)

if __name__ == "__main__":
    amount = float(input("Enter the bill amount: "))
    period = input("Enter the period of the bill? E.g. August, 2021: ")

    name_1 = input("What is your name? ")
    days_in_house_1 = int(input("How many days did %s stay in the house during the build period? " % name_1))

    name_2 = input("What is your flatmate's name? ")
    days_in_house_2 = int(input("How many days did %s stay in the house during the build period? " % name_2))

    bill = Bill(amount, period)
    flatmate1 = Flatmate(name_1, days_in_house_1)
    flatmate2 = Flatmate(name_2, days_in_house_2)

    print("%s pays: " % name_1, flatmate1.pay(bill, flatmate2))
    print("%s pays: " % name_2, flatmate2.pay(bill, flatmate1))

    pdf_report = PDFReport(filename="%s.pdf" % bill.period)
    pdf_report.generate_PDF(flatmate1, flatmate2, bill)
