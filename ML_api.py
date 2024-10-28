from fastapi import FastAPI
from pydantic import BaseModel
import pickle


app = FastAPI()

class ModelInput(BaseModel):
    Pregnancies : int
    Glucose :int
    BloodPressure :int
    SkinThickness :int
    Insulin : int
    BMI : float
    DiabetesPedigreeFunction : float
    Age : int


#loading he saved model

diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))



@app.post('/diabetes_prediction')
def diabetes_pred(data : ModelInput):

    data = data.model_dump()

    Pregnancies =data['Pregnancies']
    Glucose =data['Glucose']
    BloodPressure =data['BloodPressure']
    SkinThickness =data['SkinThickness']
    Insulin =data['Insulin']
    BMI =data['BMI']
    DiabetesPedigreeFunction =data['DiabetesPedigreeFunction']
    Age =data['Age']



    input_list= [Pregnancies , Glucose , BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
    prediction = diabetes_model.predict([input_list])

    if prediction[0] == 0:
        return {"prediction": "Hurrah! The person is not diabetic."}
    else:
        return {"prediction": "Alas! The person is diabetic."}
    
