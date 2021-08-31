import requests
from selectorlib import Extractor

class Temperature(object):
    """Represents the users local temperature from the website
    timeanddate.com/weather
    """
    def __init__(self, country, city):
        self.country = country.replace(" ", "-")
        self.city = city.replace(" ", "-")

    def get_temp(self):
        # Get the html data from the website
        base_url = "http://timeanddate.com/weather"
        url = "{}/{}/{}".format(base_url, self.country, self.city)
        req = requests.get(url)
        self.content = req.text

        return self.extract_result()

    def extract_result(self):
        # Get the temp element from the web data
        extractor = Extractor.from_yaml_file('files/temperature.yaml')
        raw_result = extractor.extract(self.content)
        result = float(raw_result['temp'].replace('\xa0°F', ''))
        return result


if __name__ =="__main__":
    r = Temperature("USA", "Chicago")
    r.get_temp()
