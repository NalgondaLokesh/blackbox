from flask import Flask, request, jsonify
import base64
import random
import hashlib
import re
from datetime import datetime
from math import pi

app = Flask(__name__)


@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({
        "status": "operational",
        "time": datetime.now().strftime("%H:%M:%S"),
        "hint": "All other endpoints use POST"
    })


@app.route('/v1/transform', methods=['POST'])
def transform():
    data = request.get_json()
    if not data or 'input' not in data:
        return jsonify({"error": "Missing 'input'"}), 400
    
    
    rot13 = data['input'].encode('rot13')
    return jsonify({
        "output": base64.b64encode(rot13.encode()).decode(),
        "hint": "Two transformations applied"
    })

@app.route('/v1/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    if not data or 'value' not in data:
        return jsonify({"error": "Requires {'value': number}"}), 400
    
    try:
        x = float(data['value'])
        return jsonify({
            "result": round(x * pi, 3),
            "hint": "Constant involved"
        })
    except:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/v1/timegate', methods=['POST'])
def timegate():
    now = datetime.now()
    return jsonify({
        "weekday": now.strftime("%A"),
        "minute": now.minute,
        "secret": now.second % 3 == 0,
        "hint": "Changes every minute"
    })


@app.route('/v1/quantum', methods=['POST'])
def quantum():
    data = request.get_json() or {}
    responses = []
    
    
    if any(str(k).lower() == "magic" for k in data.keys()):
        responses.append({"phenomenon": random.choice(["entanglement","superposition"])})
    
    if any(str(v) == "42" for v in data.values()):
        responses.append({"answer": "Meaning of life"})
    
    responses.append({
        "state": random.choice(["collapsed","uncertain"]),
        "value": random.randint(1, 100)
    })
    
    return jsonify({"observations": responses})


@app.route('/v1/cipher', methods=['POST'])
def cipher():
    data = request.get_json()
    if not data or 'message' not in data:
        return jsonify({"error": "Requires {'message': str}"}), 400
    
    shift = datetime.now().minute % 10
    result = ""
    for char in data['message']:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    
    return jsonify({
        "encoded": result,
        "hint": f"Shift changes every hour (current: {shift})"
    })


@app.route('/v1/inspect', methods=['POST'])
def inspect():
    data = request.get_json()
    if not data or 'secret' not in data:
        return jsonify({"error": "Requires {'secret': str}"}), 400
    
    s = str(data['secret'])
    return jsonify({
        "length": len(s),
        "has_upper": any(c.isupper() for c in s),
        "has_digit": any(c.isdigit() for c in s),
        "is_palindrome": s == s[::-1]
    })


@app.route('/v1/checkprime', methods=['POST'])
def checkprime():
    data = request.get_json()
    if not data or 'number' not in data:
        return jsonify({"error": "Requires {'number': int}"}), 400
    
    try:
        n = int(data['number'])
        if n < 2:
            return jsonify({"is_prime": False})
        
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return jsonify({"is_prime": False})
        
        return jsonify({
            "is_prime": True,
            "hint": "Only divisible by 1 and itself"
        })
    except:
        return jsonify({"error": "Invalid integer"}), 400

@app.route('/v1/filter', methods=['POST'])
def data_filter():
    data = request.get_json()
    if not data or 'items' not in data:
        return jsonify({"error": "Requires {'items': list}"}), 400
    
    filtered = [x for x in data['items'] 
               if isinstance(x, (int, float)) and x % 1 == 0 and x % 2 == 0]
    
    return jsonify({
        "result": filtered,
        "hint": "Filtered by numeric type and parity"
    })


@app.route('/v1/challenge', methods=['POST'])
def challenge():
    data = request.get_json()
    if not data or 'action' not in data or 'value' not in data:
        return jsonify({"error": "Requires {'action': str, 'value': any}"}), 400
    
    action = data['action'].lower()
    value = data['value']
    
    if action == "encode":
        return jsonify({"result": hashlib.sha256(str(value).encode()).hexdigest()})
    elif action == "reverse":
        return jsonify({"result": str(value)[::-1]})
    elif action == "analyze":
        return jsonify({"length": len(str(value))})
    else:
        return jsonify({"error": "Unknown action"}), 400
@app.route('/_hidden_debug', methods=['GET'])
def debug():
    return jsonify({"active_endpoints": sorted([str(rule) for rule in app.url_map.iter_rules()])})
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5010, debug=False)