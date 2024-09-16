from flask import Flask, request, jsonify
import pickle
import numpy as np
from tensorflow.keras.models import load_model

app = Flask(__name__)

with open('rf_model.pkl', 'rb') as f:
    rf_model = pickle.load(f)

ann_model = load_model('ann_model.h5')

def get_recommendations(prediction):
    if prediction == 1: 
        return {
            'Diet': 'Follow a balanced diet low in sugar and carbohydrates.',
            'Exercise': 'Engage in regular physical activity, such as walking or swimming.',
            'Medical': 'Consult a healthcare provider for a comprehensive treatment plan.',
            'Monitoring': 'Regularly monitor blood sugar levels and follow up with your healthcare provider.'
        }
    else:
        return {
            'General': 'Maintain a healthy lifestyle to prevent diabetes, including regular exercise and a balanced diet.'
        }

@app.route('/predict_rf', methods=['POST'])
def predict_rf():
    data = request.json['features']
    data = np.array(data).reshape(1, -1) 
    prediction = rf_model.predict(data)[0]
    recommendations = get_recommendations(int(prediction))
    return jsonify({
        'prediction': int(prediction),
        'recommendations': recommendations
    })

@app.route('/predict_ann', methods=['POST'])
def predict_ann():
    data = request.json['features']
    data = np.array(data).reshape(1, -1)
    prediction_prob = ann_model.predict(data)[0][0]  
    prediction = int(prediction_prob > 0.5)  
    
    recommendations = get_recommendations(prediction)
    
    return jsonify({
        'prediction': prediction,
        'probability': float(prediction_prob),
        'recommendations': recommendations
    })

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
