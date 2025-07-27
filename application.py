from flask import Flask, render_template, request
import joblib
import numpy as np
import os

app = Flask(__name__)

MODEL_PATH = os.path.join('artifacts', 'models', 'model.pkl')
SCALER_PATH = os.path.join('artifacts', 'processed', 'scaler.pkl')
ENCODER_PATH = os.path.join('artifacts', 'processed', 'label_encoders.pkl')

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)
label_encoders = joblib.load(ENCODER_PATH)

FEATURE_ORDER = [
    'Healthcare_Costs', 'Tumor_Size_mm', 'Treatment_Type', 'Diabetes', 'Age',
    'Survival_5_years', 'Mortality_Rate_per_100K', 'Country', 'Physical_Activity',
    'Insurance_Status', 'Alcohol_Consumption', 'Cancer_Stage', 'Urban_or_Rural',
    'Inflammatory_Bowel_Disease', 'Incidence_Rate_per_100K'
]


@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None 

    if request.method == 'POST':
        try:
            input_data = {key: request.form[key] for key in request.form}

            X = []
            for feature in FEATURE_ORDER:
                value = input_data[feature]
                if feature in label_encoders:  
                    le = label_encoders[feature]
                    value = le.transform([value])[0]
                else:
                    value = float(value) 
                X.append(value)

            X = np.array(X).reshape(1, -1)
            X_scaled = scaler.transform(X)

            pred = model.predict(X_scaled)[0]
            prediction = pred

        except Exception as e:
            prediction = f"Error: {e}"

    return render_template('index.html', prediction=prediction)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=6006, debug=True)
