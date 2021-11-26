from flask import Flask,jsonify,request,render_template
import utils
app = Flask(__name__)

@app.route('/')  # base API
def welcome():
    print("We are learning Flask")
    return jsonify({'Message': "Welcome API Successful"})


@app.route('/predict',methods = ['POST'])
def prediction():
    print("Testing prediction API")
    data = request.form
    if request.method == 'POST':
        print('Input data is ',data)
        x1 = float(data['Age'])
        x2 = float(data['Sex'])
        x3 = float(data['ChestPainType'])
        x4 = float(data['Cholesterol'])
        x5 = float(data['FastingBS'])
        x6 = float(data['MaxHR'])
        x7 = float(data['ExerciseAngina'])
        x8 = float(data['Oldpeak'])
        x9 = float(data['ST_Slope'])


        prediction = utils.predict_class(x1,x2,x3,x4,x5,x6,x7,x8,x9)        
        return jsonify({"Message": f'predicted class is :{prediction}'})
    
    else:
        return jsonify({"Message":'Unsuccessful'})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8085,debug=False)


