from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load trained model
model = joblib.load('model.pkl')

# Load dataset
career_data = pd.read_csv('ai_career_guidance_dataset.csv')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json

    skills = data['skills']
    education = data['education']
    industry = data['industry']
    experience = data['experience']

    # Combine user input
    user_input = f"{skills} {education} {industry} {experience}"

    # Predict profession
    prediction = model.predict([user_input])[0]

    # Get matching career details
    result = career_data[career_data['Profession'] == prediction].iloc[0]

    response = {
        'profession': prediction,
        'sector': result['Sector'],
        'industry': result['Industry'],
        'salary': result['Salary_Range'],
        'demand': result['Demand_Level'],
        'location': result['Location'],
        'description': result['Job_Description']
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)