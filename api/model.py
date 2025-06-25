import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle
import os

def train_model():
    """
    Train a machine learning model on the symptoms dataset and save it to disk.
    Returns the trained model and a dictionary mapping symptom names to column indices.
    """
    # Load the dataset
    dataset_path = os.path.join(os.path.dirname(__file__), 'dataset.csv')
    data = pd.read_csv(dataset_path)
    
    # Separate features and target
    X = data.drop('illness', axis=1)
    y = data['illness']
    
    # Create a mapping of symptom names to column indices
    symptom_to_index = {col: i for i, col in enumerate(X.columns)}
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train a Random Forest classifier
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Evaluate the model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model accuracy: {accuracy:.2f}")
    
    # Save the model and symptom mapping
    model_path = os.path.join(os.path.dirname(__file__), 'illness_model.pkl')
    with open(model_path, 'wb') as f:
        pickle.dump((model, symptom_to_index), f)
    
    return model, symptom_to_index

def load_model():
    """
    Load the trained model and symptom mapping from disk.
    If the model doesn't exist, train it first.
    """
    model_path = os.path.join(os.path.dirname(__file__), 'illness_model.pkl')
    
    if not os.path.exists(model_path):
        return train_model()
    
    with open(model_path, 'rb') as f:
        model, symptom_to_index = pickle.load(f)
    
    return model, symptom_to_index

def predict_illness(symptoms):
    """
    Predict the illness based on the provided symptoms.
    
    Args:
        symptoms (list): List of symptom strings (e.g., ["Fever", "Cough"])
    
    Returns:
        dict: Prediction results including diagnosis, confidence, etc.
    """
    # Load the model and symptom mapping
    model, symptom_to_index = load_model()
    
    # Create a feature vector with all zeros
    feature_vector = np.zeros(len(symptom_to_index))
    
    # Set the corresponding features to 1 for the provided symptoms
    for symptom in symptoms:
        # Convert symptom name to the format used in the dataset
        symptom_key = f"symptom_{symptom.lower().replace(' ', '_')}"
        if symptom_key in symptom_to_index:
            feature_vector[symptom_to_index[symptom_key]] = 1
    
    # Make a prediction
    prediction = model.predict([feature_vector])[0]
    
    # Get prediction probabilities
    probabilities = model.predict_proba([feature_vector])[0]
    confidence = int(round(np.max(probabilities) * 100))
    
    # Determine confidence level
    if confidence >= 75:
        confidence_level = "high"
        message = f"You may have {prediction}. Please consult with a healthcare professional."
    elif confidence >= 50:
        confidence_level = "medium"
        message = f"You might have {prediction}, but there could be other possibilities. Consider consulting a doctor."
    else:
        confidence_level = "low"
        message = f"Your symptoms partially match {prediction}, but the confidence is low. Please consult a healthcare professional for an accurate diagnosis."
    
    # Get top 3 predictions with their probabilities
    top_indices = np.argsort(probabilities)[::-1][:3]
    top_illnesses = [model.classes_[i] for i in top_indices]
    top_probabilities = [int(round(probabilities[i] * 100)) for i in top_indices]
    
    matches = {}
    for illness, prob in zip(top_illnesses, top_probabilities):
        if prob > 0:
            matches[illness] = {
                "percentage": prob
            }
    
    return {
        "diagnosis": prediction,
        "confidence": confidence,
        "confidence_level": confidence_level,
        "message": message,
        "matches": matches
    }

# Train the model when the module is imported
if __name__ == "__main__":
    train_model()