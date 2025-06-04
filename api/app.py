from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from diagnose import analyze_symptoms

app = Flask(__name__)
# Update CORS configuration to be more specific
CORS(app, resources={
    r"/api/*": {
        "origins": ["http://localhost:5173"],  # Your React dev server
        "methods": ["POST", "OPTIONS", "GET"],
        "allow_headers": ["Content-Type"]
    }
})