"""
Title: Flatmates bill
Description: An app that gets an input of bill amount and periods of times that
the flatmates were at the house during the period.  It returns how much each
flatmate will have to pay.  It will generate a PDF report stating the names, period,
and how much they have to pay.
Objects: Bill, Flatmate,
"""
from fpdf import FPDF

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
        pdf = FPDF(orientation='P', unit='pt', format='A4')



if __name__ == "__main__":
    bill = Bill(amount=120, period="March 2021")
    garth = Flatmate(name="Garth", days_in_house=20)
    jerry = Flatmate(name="Jerry", days_in_house=25)

    print("Garth pays: ", garth.pay(bill=bill, flatmate=jerry))
    print("Jerry pays: ", jerry.pay(bill=bill, flatmate=garth))


# float(input("Howdy, enter the bill amount: "))
# print("What is your name? ")
# float(input("How many days did you stay in the house during the bill period?"))
# print("What is your name? ")
# float(input("How many days did you stay in the house during the bill period?"))
