"""
Title: Calorie Calculator App
Description: An app that gets from the user the user's weight, height, age,
city, and country and scrapes the temperature of the users location and
calculates how many calories the user needs.
"""

from flask.views import MethodView
from wtforms import Form, StringField, SubmitField, SelectField, IntegerField
from flask import Flask, render_template, request
from files import calorie, temperature

app = Flask(__name__)

class HomePage(MethodView):

    def get(self):
        return render_template('index.html')

class CalFormPage(MethodView):

    def get(self):
        cal_form = CalForm()
        return render_template('cal_form_page.html', cal_form=cal_form)

    def post(self):
        cal_form = CalForm(request.form)
        temp = temperature.Temperature(cal_form.country.data, cal_form.city.data).get_temp()
        cal = calorie.Calorie(weight=cal_form.weight.data, height=cal_form.height.data,
                          age=cal_form.age.data, temperature=temp)
        calories = cal.calculate()

        return render_template('cal_form_page.html',
                                 result=True,
                                 cal_form=cal_form,
                                 calories=calories)


class CalForm(Form):
    metric = SelectField("Metric? ", choices=[(True, 'True'), (False, 'False')])
    age = IntegerField("Age: ")
    weight = IntegerField("Weight: ")
    height = IntegerField("Height: ")
    city = StringField("City: ")
    country = StringField("Country: ")

    button = SubmitField("Calculate")


app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/cals', view_func=CalFormPage.as_view('cal_form_page'))

if __name__ == "__main__":
    app.run(debug=True)
