from flask import Flask, request, jsonify
from flask_cors import CORS
from web_agent import WebAgent
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Initialize the web agent
web_agent = WebAgent()

@app.route('/')
def home():
    return jsonify({
        "message": "Manus Replica API Server",
        "version": "1.0.0",
        "status": "running"
    })

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        if not data or 'message' not in data:
            return jsonify({
                "success": False,
                "error": "Missing 'message' field in request"
            }), 400
        
        user_message = data['message']
        result = web_agent.process_message(user_message)
        
        return jsonify(result)
    
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route('/api/status', methods=['GET'])
def status():
    try:
        status_info = web_agent.get_status()
        return jsonify({
            "success": True,
            "data": status_info
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route('/api/tools', methods=['GET'])
def get_tools():
    try:
        tools = []
        for name, tool_info in web_agent.tool_registry.tools.items():
            tools.append({
                "name": name,
                "description": tool_info["description"]
            })
        
        return jsonify({
            "success": True,
            "tools": tools
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

