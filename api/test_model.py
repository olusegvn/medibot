import sys
import os

# Add the current directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from diagnose import analyze_symptoms

def test_model():
    """
    Test the model with different sets of symptoms and print the results.
    """
    test_cases = [
        ["Fever", "Cough", "Sore throat", "Runny nose"],  # Common Cold
        ["Fever", "Headache", "Muscle pain", "Fatigue"],  # Flu
        ["Nausea", "Vomiting", "Diarrhea", "Abdominal pain"],  # Food Poisoning
        ["Headache", "Nausea", "Dizziness"],  # Migraine
        ["Rashes", "Shortness of breath", "Runny nose"],  # Allergic Reaction
        ["Fever", "Cough", "Shortness of breath", "Loss of appetite"],  # COVID-19
        ["Nausea", "Vomiting", "Diarrhea", "Fever", "Abdominal pain"],  # Stomach Virus
    ]
    
    print("Testing the illness prediction model...")
    print("-" * 50)
    
    for i, symptoms in enumerate(test_cases):
        print(f"Test case {i+1}: {', '.join(symptoms)}")
        result = analyze_symptoms(symptoms)
        print(f"Diagnosis: {result['diagnosis']}")
        print(f"Confidence: {result['confidence']}% ({result['confidence_level']})")
        print(f"Message: {result['message']}")
        print("Top matches:")
        for illness, data in result['matches'].items():
            print(f"  - {illness}: {data['percentage']}%")
        print("-" * 50)
    
    print("Testing complete!")

if __name__ == "__main__":
    test_model()