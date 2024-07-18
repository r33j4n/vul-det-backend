from flask import Flask, jsonify, request
from flask_cors import CORS
from rag_service_query import chat,ret_result



app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})  # Enable CORS for all routes from http://localhost:3000


@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000, timeout=10000)


@app.route('/getPrompt', methods=['POST'])
def query_chat():
    data = request.json
    code = data.get('content')
    language = data.get('language')
    print(code)
    print(language)

    if not code:
        return jsonify({"error": "Content need to Provided"}), 400
    try:
        result = chat(code, language)
        return jsonify({"result": result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/view_summary',methods=['GET'])
def return_results():
    try:
        result=ret_result("code","language")
        return jsonify({"result": result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500




