from flask import request, jsonify
from app import app
from app.utils.gpt_integration import get_gpt_response

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['message']
    # Handle technology-based logic
    if 'AWS' in user_message:
        return jsonify({"response": "How can I assist you with AWS?"})
    # Use AI for general responses
    else:
        response = get_gpt_response(user_message)
        return jsonify({"response": response})
