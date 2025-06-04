import random

def analyze_symptoms(symptoms):
    """
    Analyze the provided symptoms and return a potential diagnosis.
    This is a simplified example - a real medical diagnosis would require more sophisticated logic.
    """
    # Dictionary mapping common illnesses to their symptoms
    illness_symptoms = {
        "Common Cold": ["Runny nose", "Cough", "Sore throat", "Fever"],
        "Flu": ["Fever", "Fatigue", "Muscle pain", "Headache", "Cough"],
        "Food Poisoning": ["Nausea", "Vomiting", "Diarrhea", "Abdominal pain"],
        "Migraine": ["Headache", "Nausea", "Dizziness"],
        "Allergic Reaction": ["Rashes", "Shortness of breath", "Runny nose"],
        "COVID-19": ["Fever", "Cough", "Shortness of breath", "Fatigue", "Loss of appetite"],
        "Stomach Virus": ["Nausea", "Vomiting", "Diarrhea", "Abdominal pain", "Fever"],
    }
    
    # Count matching symptoms for each illness
    matches = {}
    for illness, illness_symp in illness_symptoms.items():
        count = sum(1 for s in symptoms if s in illness_symp)
        if count > 0:
            matches[illness] = {
                "count": count,
                "total": len(illness_symp),
                "percentage": round((count / len(illness_symp)) * 100)
            }
    
    # Sort by percentage match (descending)
    sorted_matches = sorted(matches.items(), key=lambda x: x[1]["percentage"], reverse=True)
    
    if not sorted_matches:
        return {
            "diagnosis": "Unknown",
            "confidence": 0,
            "message": "Unable to determine a diagnosis based on the provided symptoms."
        }
    
    # Get the top match
    top_illness, top_data = sorted_matches[0]
    
    # Generate a response
    if top_data["percentage"] >= 75:
        confidence = "high"
        message = f"You may have {top_illness}. Please consult with a healthcare professional."
    elif top_data["percentage"] >= 50:
        confidence = "medium"
        message = f"You might have {top_illness}, but there could be other possibilities. Consider consulting a doctor."
    else:
        confidence = "low"
        message = f"Your symptoms partially match {top_illness}, but the confidence is low. Please consult a healthcare professional for an accurate diagnosis."
    
    return {
        "diagnosis": top_illness,
        "confidence": top_data["percentage"],
        "confidence_level": confidence,
        "message": message,
        "matches": dict(sorted_matches[:3])  # Return top 3 matches
    }

# Test function
if __name__ == "__main__":
    test_symptoms = ["Fever", "Cough", "Fatigue"]
    result = analyze_symptoms(test_symptoms)
    print(result)