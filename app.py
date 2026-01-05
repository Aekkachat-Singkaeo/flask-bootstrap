from flask import Flask, render_template, request,redirect,url_for

app = Flask(__name__)

care=[
    {'id':1,'brand' :'Toyota','model':'Yaris Ativ','year':1945,'price':559000},
    {'id':2,'brand' :'Honda','model':'City Hatcback','year':1945,'price':689000},
    {'id':3,'brand' :'Nissan','model':'Amera','year':2005,'price':799000},
]

@app.route("/")
def index():
    return render_template("index.html", title="HOME PAGE")

@app.route('/cars')
def call_cars():
    return render_template('cars/cars.html', title='Show All Cars Page', cars=care)

@app.route('/cars/new', methods=['GET', 'POST'])
def new_car():
    if request.method == 'POST':
        brand = request.form['brand']
        model = request.form['model']
        year = (request.form['year'])
        price = (request.form['price'])
    length = len(care)
    id = length + 1

    car = {'id': id, 'brand': brand, 'model': model, 'year': year, 'price': price}

    care.append(car)

    return redirect(url_for('call_cars'))

 return render_template('cars/new_cars.html', title='New Car Page')