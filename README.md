# React + Vite

This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react) uses [Babel](https://babeljs.io/) for Fast Refresh
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react-swc) uses [SWC](https://swc.rs/) for Fast Refresh

## Expanding the ESLint configuration

If you are developing a production application, we recommend using TypeScript with type-aware lint rules enabled. Check out the [TS template](https://github.com/vitejs/vite/tree/main/packages/create-vite/template-react-ts) for information on how to integrate TypeScript and [`typescript-eslint`](https://typescript-eslint.io) in your project.

# Medibot

A simple medical chatbot that helps pre-diagnose common illnesses based on symptoms.

## Features

- Interactive UI for selecting symptoms
- Python backend for analyzing symptoms and providing diagnoses
- Real-time feedback with confidence levels

## Project Structure

- `/src` - React frontend code
- `/api` - Python Flask backend code

## Setup and Running

### Quick Start (Unix/Linux/Mac)

For convenience, you can use the provided shell script to run both the backend and frontend:

```
chmod +x run_app.sh  # Make the script executable (first time only)
./run_app.sh
```

This script will:
1. Set up the Python virtual environment
2. Install all dependencies
3. Start both the Flask backend and React frontend
4. Properly shut down both when you exit

### Manual Setup

#### Backend (Flask API)

1. Navigate to the API directory:
   ```
   cd api
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run the Flask server:
   ```
   python app.py
   ```

The API will be available at http://localhost:5000

#### Frontend (React)

1. In a new terminal, navigate to the project root directory

2. Install dependencies:
   ```
   npm install
   ```

3. Run the development server:
   ```
   npm run dev
   ```

The React app will be available at http://localhost:5173 (or another port if 5173 is in use)

## How to Use

1. Open the React app in your browser
2. Select the symptoms you're experiencing by clicking on them
3. Click the up arrow button to submit your symptoms
4. View the diagnosis result in the chat area

## Note

This is a demonstration project and should not be used for actual medical diagnosis. Always consult with a healthcare professional for medical advice.
