from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request
from flatmates_bill import flat

app = Flask(__name__)

class HomePage(MethodView):

    def get(self):
        return render_template('index.html')

class BillFormPage(MethodView):
    def get(self):
        bill_form = BillForm()
        return render_template('bill_form_page.html', billform=bill_form)

    def post(self):
        billform = BillForm(request.form)

        the_bill = flat.Bill(int(billform.amount.data), billform.period.data)
        flatmate1 = flat.Flatmate(billform.name1.data, int(billform.days_in_house1.data))
        flatmate2 = flat.Flatmate(billform.name2.data, int(billform.days_in_house2.data))

        return render_template('bill_form_page.html',
                               result=True,
                               billform=billform,
                               name1=flatmate1.name,
                               amount1="{:.2f}".format(flatmate1.pay(the_bill, flatmate2)),
                               name2=flatmate2.name,
                               amount2="{:.2f}".format(flatmate2.pay(the_bill, flatmate1)))


class BillForm(Form):
    amount = StringField("Bill Amount: ", default="100")
    period = StringField("Bill Period: ", default="December 2020")

    name1 = StringField("Name: ", default="Gerry")
    days_in_house1 = StringField("Days in House: ", default="13")
    name2 = StringField("Name: ", default="Rosana")
    days_in_house2 = StringField("Days in House: ", default="23")

    button = SubmitField("Calculate")


app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/bill', view_func=BillFormPage.as_view('bill_form_page'))

app.run(debug=True)
