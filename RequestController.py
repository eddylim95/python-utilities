from flask import Flask
from flask import request, jsonify
import sys

app = Flask(__name__)

@app.route('/', methods=['POST'])
def result():
    json = request.get_json()
    print(json, file=sys.stdout)
    #print('Error', file=sys.stderr)
    return jsonify({'success': True})

app.run()