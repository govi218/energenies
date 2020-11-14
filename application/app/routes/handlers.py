from app import app
from app.data.models import User, Device
from app.forms.public import StartForm, CreateDeviceForm
from flask import request, redirect, render_template, url_for, jsonify
from uuid import uuid4

title = "Energysavers"
device_types=["fridge", "oven", "car", "solar panels", "heater"]

### in memory database
global user
global devices

fridge = Device(id=uuid4().hex[:6], name="fridge", energy_usage=125, points=15, image="fridge.jpeg")
microwave = Device(id=uuid4().hex[:6], name="microwave", energy_usage=95, points=8, image="microwave.jpeg")

devices = [fridge, microwave]
### end of database



@app.route('/', methods=['GET', 'POST'])
def home():
    create_device_form = CreateDeviceForm()
    # if create_device_form.validate_on_submit():
        # new_device = Device(id=uuid4().hex[:6], name="new device", energy_usage=0, points=0, image="")
        # global devices
        # devices.append(new_device)
        # print("created new device")
        # print(devices)
    return render_template(
        'home.html',
        title=title,
        devices=devices,
        create_device_form=create_device_form    
        )


@app.route('/create', methods=['GET', 'POST'])
def create():
    """creates a new device"""
    print("created new device")
    new_device = Device(id=uuid4().hex[:6], name="new device", energy_usage=0, points=0, image="noimage.png")
    global devices
    devices.append(new_device)
    
    if request.method == 'POST':        
        print("created new device")
    
    return redirect(url_for('home'))


@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        for device in devices:
            if device.id == request.form['id']:
                device.name = request.form['name']
                device.energy_usage = request.form['usage'] 
                return jsonify({"success": True})    
    return jsonify({"success": False})


@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        for device in devices:
            if device.id == request.form['id']:
                devices.remove(device)
                return jsonify({"success": True, "redirect": url_for('home')})    
    return jsonify({"success": False})



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