from flask import Flask,flash, render_template, request, redirect, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = b'secretkey'   

care = [
    {'id': 1, 'brand': 'Toyota', 'model': 'Yaris Ativ', 'year': 1945, 'price': 559000},
    {'id': 2, 'brand': 'Honda', 'model': 'City Hatchback', 'year': 1945, 'price': 689000},
    {'id': 3, 'brand': 'Nissan', 'model': 'Amera', 'year': 2005, 'price': 799000},
]

@app.route("/")
def index():
    return render_template("index.html", title="HOME PAGE")

@app.route('/cars')
def call_cars():
    return render_template(
        'cars/cars.html',
        title='Show All Cars Page',
        cars=care
    )

@app.route('/cars/new', methods=['GET', 'POST'])
def new_car():
    if request.method == 'POST':
        brand = request.form['brand']
        model = request.form['model']
        year = int(request.form['year'])
        price = int(request.form['price'])

        new_id = len(care) + 1

        car = {
            'id': new_id,
            'brand': brand,
            'model': model,
            'year': year,
            'price': price
        }

        care.append(car)
        flash(f'New car {brand} {model} has been added.', 'success')
        return redirect(url_for('call_cars'))

   
    return render_template(
        'cars/new_cars.html',
        title='New Car Page'
    )
@app.route('/cars/<int:id>/delete')
def delete_car(id):
    for car in care:
        if id == car['id']:
            care.remove(car)
            break  
    flash(f'Car with ID {id} has been deleted.', 'success')
    return redirect(url_for('call_cars'))

@app.route('/cars/<int:id>/edit')
def edit_car(id):

    return render_template('cars/edit_cars.html',title='Edit Car Page')