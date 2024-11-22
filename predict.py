import sys
import pandasgui
import joblib
import pandas as pd
from pandasgui import show
# Load model and binarizer
model = joblib.load('model.pkl')
mlb = joblib.load('mlb.pkl')
df = pd.read_excel('symptom_description_precaution.xlsx')

# Get input symptoms
input_symptoms = sys.argv[1].split(', ')
symptom_vector = mlb.transform([input_symptoms])

# Make prediction
predicted_disease = model.predict(symptom_vector)[0]
disease_row = df[df['Disease'] == predicted_disease].iloc[0]

# Prepare output
description = disease_row['Description']
precautions = [
    disease_row['Precaution_1'],
    disease_row['Precaution_2'],
    disease_row['Precaution_3'],
    disease_row['Precaution_4']
]

# Output results
print(predicted_disease)
print(description)
for precaution in precautions:
    print(precaution)
