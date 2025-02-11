from flask import Flask, request, make_response, jsonify 
import os 

app = Flask(__name__)

PORT = int(os.getenv("PORT", 5000))

@app.route('/')
def hello():
    response = make_response(
        {
            'response': 'Hello, World!',
            'status': 200
        }
    )
    return response

@app.route('/repeat', methods=['GET'])
def repeat():
    user_input = request.args.get("input", "No input provided") 
    response = make_response(
        {
            'body': user_inpu