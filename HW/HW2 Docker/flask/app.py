from flask import Flask, request, make_response
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
            'body': user_input,
            'status': 200
        }
    )
    return response


if __name__ == '__main__':
    # By default flask is only accessible from localhost.
    # Set this to '0.0.0.0' to make it accessible from any IP address
    # on your network (not recommended for production use)
    app.run(host='0.0.0.0', port=PORT, debug=True)
