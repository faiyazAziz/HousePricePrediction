from flask import Flask,request,jsonify
import pickle
import numpy as np

model = pickle.load(open('priceModel.pkl','rb'))
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World"

@app.route('/predict',methods = ['POST'])
def predict():

    area = request.form.get('area')
    noOfBedroom = request.form.get('noOfBedroom')
    noOfBathroom = request.form.get('noOfBathroom')
    noOfStories = request.form.get('noOfStories')
    mainRoad = request.form.get('mainRoad')
    guestRoom = request.form.get('guestRoom')
    basement = request.form.get('basement')
    hotWaterHeating = request.form.get('hotWaterHeating')
    airConditioning = request.form.get('airConditioning')
    parking = request.form.get('parking')
    prefarea = request.form.get('prefarea')
    furnishingstatus = request.form.get('furnishingstatus')

    input_data = np.array([[ area, noOfBedroom, noOfBathroom,
                            noOfStories, mainRoad,guestRoom, basement,
                            hotWaterHeating, airConditioning,parking,
                            prefarea, furnishingstatus]])
    result = model.predict(input_data)[0]

    return jsonify({'price':str(result)})


if __name__ == '__main__':
    app.run(debug=True)
