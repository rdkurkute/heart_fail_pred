import pickle
import numpy as np
import os
import config
model_folder_path = config.MODEL_FOLDER_PATH

def predict_class(Age, Sex, ChestPainType, Cholesterol, FastingBS, MaxHR, ExerciseAngina, Oldpeak, ST_Slope):
    
    xgb_model = pickle.load(open(f'{model_folder_path}/pickel_file.pkl','rb'))
    
    data_ = np.array([[Age, Sex, ChestPainType, Cholesterol, FastingBS,MaxHR, ExerciseAngina, Oldpeak, ST_Slope]])
    prediction = xgb_model.predict(data_)
    # collection_analysis.insert_one()
    print("Predicted class is :",prediction[0])
    pred = prediction[0]
    
    return pred

# predict_class(59,0,3,0,0,132,1,1.5,3)
