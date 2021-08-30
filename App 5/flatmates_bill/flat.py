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
