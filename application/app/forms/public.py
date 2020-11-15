from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, SelectField
from wtforms.validators import DataRequired
from wtforms.fields.core import IntegerField

class StartForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()], render_kw={"placeholder": "Username"}) 
    submit = SubmitField('Start')

class CreateDeviceForm(FlaskForm):
    # name = StringField('Name', validators=[DataRequired()], render_kw={"placeholder": "Name (i.e. fridge)"})
    # device_type = SelectField('Type', choices=[
    #     ("fridge", "fridge"),
    #     ("oven", "oven"),
    #     ("car", "car"),
    #     ("phone", "phone"),
    #     ("solar panels", "solar panels"),
    #     ("heater", )
    # ])
    submit = SubmitField('Add')

class AggregationForm(FlaskForm):
    smartmeter1 = IntegerField('Smartmeter reading', validators=[DataRequired()], render_kw={"placeholder": "Smartmeter reading"}) 
    smartmeter2 = IntegerField('Smartmeter reading', validators=[DataRequired()], render_kw={"placeholder": "Smartmeter reading"}) 
    smartmeter3 = IntegerField('Smartmeter reading', validators=[DataRequired()], render_kw={"placeholder": "Smartmeter reading"}) 
    smartmeter4 = IntegerField('Smartmeter reading', validators=[DataRequired()], render_kw={"placeholder": "Smartmeter reading"}) 
    smartmeter5 = IntegerField('Smartmeter reading', validators=[DataRequired()], render_kw={"placeholder": "Smartmeter reading"}) 
    submit = SubmitField('Start')