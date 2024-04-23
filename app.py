from flask import Flask, render_template, request
import pickle as pk

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("form.html")

@app.route("/predict", methods=["POST"])
def submit():
    form_data = request.json
    keys_for_array = ['mathSex','mathAge', 'mathAddress', 'mathFamSize', 'mathPStatus', 'mathMedu', 'mathFedu','motherJob', 'fatherJob', 'reasonMap', 'guardianMap', 
    'travelTime', 'studyTime', 'pastFailures', 'eduSupport', 'famSupport',
    'paidClasses', 'extraCurricular', 'nurserySchool', 'higherEdu',
    'internetAccess', 'romanticRelationship', 'familyRelationship',
    'freeTime', 'goingOut', 'workdayAlcohol', 'weekendAlcohol',
    'healthStatus', 'schoolAbsences', 'firstPeriodGrade', 'secondPeriodGrade',
    'portravelTime', 'porstudyTime', 'porpastFailures', 'poreduSupport',
    'porfamSupport', 'porpaidClasses', 'porextraCurricular', 'pornurserySchool',
    'porhigherEdu', 'porinternetAccess', 'porromanticRelationship',
    'porfamilyRelationship', 'porfreeTime', 'porgoingOut', 'porworkdayAlcohol',
    'porweekendAlcohol', 'porhealthStatus', 'porschoolAbsences', 'porfirstPeriodGrade',
    'porsecondPeriodGrade'
    ]
    numeric_values = [int(form_data[key]) for key in keys_for_array]
    print(numeric_values)
    with open('catboost.pkl', 'rb') as file:
        loaded_model = pk.load(file)
    prediction = loaded_model.predict([numeric_values])
    print (prediction)
    return {"grade1": prediction[0], "grade2": prediction[0]}
    

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
