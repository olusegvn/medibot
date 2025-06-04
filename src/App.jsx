"use client"

import { useState } from "react"
import "./App.css"

function App() {
  const [selectedSymptoms, setSelectedSymptoms] = useState([])
  const [diagnosis, setDiagnosis] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  const symptoms = [
    "Muscle pain",
    "Dizziness",
    "Fever",
    "Shortness of breath",
    "Runny nose",
    "Loss of appetite",
    "Cough",
    "Headache",
    "Nausea",
    "Vomiting",
    "Diarrhea",
    "Chest pain",
    "Fatigue",
    "Sore throat",
    "Abdominal pain",
    "Shivering",
    "Rashes",
  ]

  const toggleSymptom = (symptom) => {
    if (selectedSymptoms.includes(symptom)) {
      setSelectedSymptoms(selectedSymptoms.filter((s) => s !== symptom))
    } else {
      setSelectedSymptoms([...selectedSymptoms, symptom])
    }
  }


  const submitSymptoms = async () => {
    if (selectedSymptoms.length === 0) {
      setError("Please select at least one symptom")
      return
    }

    setLoading(true)
    setError(null)
    setDiagnosis(null)

    try {
      const response = await fetch('/api/diagnose', {  // Notice the relative URL
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ symptoms: selectedSymptoms })  // Fixed the payload
      });

      if (!response.ok) {
        throw new Error('Failed to get diagnosis');
      }

      const data = await response.json();
      setDiagnosis(data);
    } catch (err) {
      setError(err.message || 'An error occurred while getting diagnosis');
      console.error(err);
    } finally {
      setLoading(false);
    }
  }

  return (
      <div className="app">
        <div className="chat-container">
          <div className="status-bar">
            <div className="time">9:41</div>
            <div className="status-icons">
              <div className="signal"></div>
              <div className="wifi"></div>
              <div className="battery"></div>
            </div>
          </div>

          <div className="chat-messages">
            <div className="bot-icon-container">
              <div className="bot-icon">
                <BotIcon />
              </div>
            </div>

            <div className="message bot-message">Hey there!</div>
            <div className="message bot-message">I'm Medibot</div>
            <div className="message bot-message">
              I'm here to help you pre-diagnose common illnesses you might be feeling.
            </div>
            <div className="message bot-message">How do you feel?</div>

            {loading && (
              <div className="message bot-message">Analyzing your symptoms...</div>
            )}

            {error && (
              <div className="message bot-message" style={{ backgroundColor: "#ffdddd" }}>
                Error: {error}
              </div>
            )}

            {diagnosis && (
              <>
                <div className="message bot-message">
                  <strong>Diagnosis: {diagnosis.diagnosis}</strong>
                </div>
                <div className="message bot-message">
                  Confidence: {diagnosis.confidence}% ({diagnosis.confidence_level})
                </div>
                <div className="message bot-message">
                  {diagnosis.message}
                </div>
              </>
            )}
          </div>

          <div className="selection-area">
            <div className="selection-counter">
              <span>{selectedSymptoms.length} selected</span>
              <button
                className="up-arrow"
                onClick={submitSymptoms}
                disabled={loading}
              >
                {loading ? "..." : "↑"}
              </button>
            </div>

            <div className="symptoms-grid">
              {symptoms.map((symptom, index) => (
                  <button
                      key={index}
                      className={`symptom-button ${selectedSymptoms.includes(symptom) ? "selected" : ""}`}
                      onClick={() => toggleSymptom(symptom)}
                  >
                    {symptom}
                  </button>
              ))}
            </div>
          </div>
        </div>
      </div>
  )
}

// Simple Bot Icon Component
function BotIcon() {
  return (
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
        <circle cx="12" cy="12" r="11" stroke="black" strokeWidth="2" fill="white" />
        <circle cx="8" cy="10" r="2" fill="black" />
        <circle cx="16" cy="10" r="2" fill="black" />
        <path d="M7 15C8.5 17 15.5 17 17 15" stroke="black" strokeWidth="2" strokeLinecap="round" />
      </svg>
  )
}

export default App
