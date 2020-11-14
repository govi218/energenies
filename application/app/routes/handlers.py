from app import app
from app.data.models import User, Device
from app.forms.public import StartForm, CreateDeviceForm
from flask import redirect, render_template, url_for

from app.Aggregator.Aggregation import Customer, Aggregator


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


@app.route('/init_aggr', methods=['GET'])
def init_aggr():

    # Initialize users
    customer_number = 5

    aggregator = Aggregator()
    customers = []
    for i in range(customer_number):
        customers.append(Customer(aggregator))
    
    for i in range(len(customers)):
        enc_shares = customers[i].encrypt_shares()
        customers[i].send_enc_shares(enc_shares)

    aggragation_result = aggregator.aggregate_data()
    
    total_Paillier = 0
    for uuid in aggragation_result:
        for customer in customers:
            if uuid is customer.name:
                aggr_ptxt = customer.private_key.decrypt(aggragation_result[uuid])
                aggr_ptxt += customer.retained_share
                total_Paillier += aggr_ptxt
                print("Sum of shares for user {}: {}".format(uuid, aggr_ptxt))

    print("ptxt sum: ", Customer.smartmeter_reading_sum)
    print("ctxt sum: ", total_Paillier)