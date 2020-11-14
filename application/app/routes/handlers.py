from app import app
from app.data.models import User, Device
from app.forms.public import StartForm, CreateDeviceForm
from flask import redirect, render_template, url_for


title = "Energysavers"
device_types=["fridge", "oven", "car", "solar panels", "heater"]

### in memory database
global user
global devices

fridge = Device(name="fridge", energy_usage=125, points=15, image="fridge.jpeg")
# microwave = Device(name="microwave", energy_usage=95, points=8)

devices = [fridge]
### end of database



@app.route('/', methods=['GET', 'POST'])
def home():
    create_device_form = CreateDeviceForm()
    if create_device_form.validate_on_submit():
        print("created new device")
    return render_template(
        'home.html',
        title=title,
        devices=devices,
        create_device_form=create_device_form    
        )


# @app.route('/create', methods=['GET', 'POST'])
# def create():
#     """creates a new device"""
#     if request.method == 'POST':
#         print("created new device")






@app.route('/join', methods=['GET', 'POST'])
def join():
    start_form = StartForm()
    if start_form.validate_on_submit():
        user = User(username=start_form.username.data)
        return redirect(url_for('home'))
    
    return render_template(
        'start.html', 
        title=title,
        start_form=start_form
        )


@app.route('/leave', methods=['GET', 'POST'])
def leave():
    return redirect(url_for('join'))