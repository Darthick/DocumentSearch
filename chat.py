from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Replace these with your actual values
ENDPOINT_URL = 'https://aml-documentsearch-dev-5.eastus2.inference.ml.azure.com/score'
API_KEY = 'n4GyWpwW20sACxL76bOv6GJKACCzaaQd'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form.get('user_input', '')
    
    if not user_input:
        return jsonify({'bot_response': 'Error: Empty user input'})

    try:
        # Prepare headers and data for the API request
        headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {API_KEY}'}
        data = {'question': user_input, 'chat_history': []}

        # Make the API request
        response = requests.post(ENDPOINT_URL, json=data, headers=headers)
        response.raise_for_status()  # Raise an error for unsuccessful HTTP responses

        # Extract bot response from the JSON response
        bot_response = response.json().get('output', 'Error in getting response')
        print("Bot Response:", bot_response)

        return jsonify({'bot_response': bot_response})

    except requests.RequestException as e:
        # Handle request-related errors
        error_message = f"Error in getting response: {str(e)}"
        print(error_message)
        return jsonify({'bot_response': error_message})

    except Exception as e:
        # Handle other unexpected errors
        error_message = f"Unexpected error: {str(e)}"
        print(error_message)
        return jsonify({'bot_response': error_message})

#if __name__ == '__main__':
 #   app.run(port=5000, debug=True)
