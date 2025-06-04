from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from diagnose import analyze_symptoms

app = Flask(__name__)
CORS(app, supports_credentials=True)


# Ensure CORS headers are added to all responses
@app.route('/api/diagnose', methods=['OPTIONS'])
def handle_options():
    return '', 204

@app.route('/api/diagnose', methods=['POST'])
def diagnose():
    data = request.json
    symptoms = data.get('symptoms', [])

    if not symptoms:
        return jsonify({
            "error": "No symptoms provided",
            "message": "Please select at least one symptom for diagnosis"
        }), 400

    result = analyze_symptoms(symptoms)
    return jsonify(result)

@app.route('/api/diagnose', methods=['GET'])
def get_diagnosis():
    # data = request.json
    # symptoms = data.get('symptoms', [])
    #
    # if not symptoms:
    #     return jsonify({
    #         "error": "No symptoms provided",
    #         "message": "Please select at least one symptom for diagnosis"
    #     }), 400

    # result = analyze_symptoms(symptoms)
    return 'Hello Angie'

@app.after_request
def after_request(response):
    print(response.headers)
    return response

if __name__ == '__main__':
    app.run(debug=False, port=5000)
