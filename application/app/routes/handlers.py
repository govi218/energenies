from app import app
from app.data.models import User, Device
from app.forms.public import StartForm, CreateDeviceForm, AggregationForm
from flask import redirect, render_template, url_for

from app.Aggregator.Aggregation import Customer, Aggregator

from flask import request, redirect, render_template, url_for, jsonify
from uuid import uuid4

title = "Energenies"
device_types=["fridge", "oven", "car", "solar panels", "heater"]

### in memory database
global user
global devices
global level
global points

points_to_next_level = 100


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

@app.route('/aggregate', methods=['POST'])
def aggregate():
    print(request.form)
    # ImmutableMultiDict([('csrf_token', 'IjlmMWEzYWZlMjU0NzRmNmM3YzA4MzliODIxNjdlNDFhYjQ3YjBjNWMi.X7EXFg.gWzmoRvOlbnP2eLKZowjVjPKxb8'), ('smartmeter1', '1234123'), ('smartmeter2', '1234123'), ('smartmeter3', '1234123'), ('smartmeter4', '1324114'), ('smartmeter5', '12341'), ('submit', 'Start')])

    customer_number = 5

    original_meter_redings = {}
    aggregator = Aggregator()
    customers = []
    for i in range(customer_number):
        customers.append(Customer(aggregator, int(request.form["smartmeter{}".format(i+1)])))
        original_meter_redings[customers[i].name] = int(request.form["smartmeter{}".format(i+1)])

    for i in range(len(customers)):
        enc_shares = customers[i].encrypt_shares()
        customers[i].send_enc_shares(enc_shares)

    aggragation_result = aggregator.aggregate_data()

    print("origi: {}", original_meter_redings)

    total_Paillier = 0
    list_aggr_ptxt = {}
    for uuid in aggragation_result:
        for customer in customers:
            if uuid is customer.name:
                aggr_ptxt = customer.private_key.decrypt(aggragation_result[uuid])
                aggr_ptxt += customer.retained_share
                total_Paillier += aggr_ptxt
                list_aggr_ptxt[uuid] = aggr_ptxt
                print("Sum of shares for user {}: {}".format(uuid, aggr_ptxt))

    print("ptxt sum: ", Customer.smartmeter_reading_sum)
    print("ctxt sum: ", total_Paillier)

    return jsonify({"success": True, "Orinal meter readings":original_meter_redings, "intermediate_results":list_aggr_ptxt, "ptxt sum":Customer.smartmeter_reading_sum, "ctxt sum: ":total_Paillier})

@app.route('/init_aggr', methods=['GET'])
def init_aggr():

    start_form = AggregationForm()

    return render_template('aggregation.html', title=title, start_form=start_form)

@app.route('/signal_processing', methods=['GET'])
def signal_processing():
    return app.send_static_file('html/signal-processing.html')
