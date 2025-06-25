# Medibot AI Diagnosis System

This folder contains the backend API for the Medibot application, including a machine learning model for diagnosing illnesses based on symptoms.

## Files

- `app.py`: Flask API server that handles diagnosis requests
- `diagnose.py`: Contains the `analyze_symptoms` function that uses the machine learning model
- `model.py`: Implements the machine learning model for illness prediction
- `dataset.csv`: Training dataset with symptoms and illness labels
- `test_model.py`: Script to test the model with different symptom combinations

## Dataset

The dataset (`dataset.csv`) contains:
- 17 symptom columns (boolean values: 0 or 1)
- 1 illness column (label)
- 28 samples covering 7 common illnesses

## Machine Learning Model

The system uses a Random Forest classifier to predict illnesses based on symptoms. The model:
- Is trained on the dataset of symptoms and illnesses
- Achieves approximately 67% accuracy on the test set
- Returns predictions with confidence levels (high, medium, low)
- Provides the top 3 matching illnesses with their confidence percentages

## How to Use

1. The model is automatically trained when the API starts
2. Send a POST request to `/api/diagnose` with a JSON payload containing a list of symptoms
3. The API will return a diagnosis with confidence level and additional information

Example request:
```json
{
  "symptoms": ["Fever", "Cough", "Fatigue"]
}
```

Example response:
```json
{
  "diagnosis": "Flu",
  "confidence": 80,
  "confidence_level": "high",
  "message": "You may have Flu. Please consult with a healthcare professional.",
  "matches": {
    "Flu": {"percentage": 80},
    "COVID-19": {"percentage": 15},
    "Common Cold": {"percentage": 5}
  }
}
```

## Testing

Run the test script to verify the model's predictions:

```
python test_model.py
```

This will test the model with different symptom combinations and print the results.

## Disclaimer

This is a simplified diagnostic tool for educational purposes only. It should not be used as a substitute for professional medical advice, diagnosis, or treatment.