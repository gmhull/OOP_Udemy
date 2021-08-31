from . import temperature

class Calorie:
    """Represents required calorie intake based on the formula:
    BMR = 10*weight + 6.25*height - 5*age - 10*temperature
    """
    def __init__(self, weight, height, age, temperature, metric=True):
        self.weight = weight
        self.height = height
        self.age = age
        self.temperature = temperature
        self.metric = metric

    def calculate(self):
        if self.metric == False:
            self.convert_to_metric()
        BMR = 10*self.weight + 6.25*self.height - 5*self.age - 10*self.temperature
        return BMR

    def convert_to_metric(self):
        self.weight = self.weight/2.2
        self.height = self.height
        self.temperature = temperature * (5/9) - 32


if __name__ =="__main__":
    temp = temperature.Temperature("USA", "Merrimack").get_temp()
    calorie = Calorie(weight=84, height=197, age=24, temperature=temp)
    print(calorie.calculate())
