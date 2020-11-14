from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, SelectField
from wtforms.validators import DataRequired

class StartForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()], render_kw={"placeholder": "Username"}) 
    submit = SubmitField('Start')

class CreateDeviceForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()], render_kw={"placeholder": "Name (i.e. fridge)"})
    # device_type = SelectField('Type', choices=[
    #     ("fridge", "fridge"),
    #     ("oven", "oven"),
    #     ("car", "car"),
    #     ("phone", "phone"),
    #     ("solar panels", "solar panels"),
    #     ("heater", )
    # ])
    submit = SubmitField('Create')