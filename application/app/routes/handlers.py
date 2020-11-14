from app import app
from app.data.models import User
from app.forms.public import StartForm
from flask import render_template


title = "Energysavers"
global user


@app.route('/join', methods=['GET', 'POST'])
def index():
    start_form = StartForm()
    if start_form.validate_on_submit():
        print("starting session")
        user = User(username=start_form.username.data)
        print(user)
    
    return render_template(
        'start.html', 
        title=title,
        start_form=start_form
        )