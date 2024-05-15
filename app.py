from flask import Flask, request, render_template, jsonify
import os
import json
from datetime import datetime

app = Flask(__name__)
LOG_DIR = './logs/'

def load_logs():
    logs = []
    for filename in os.listdir(LOG_DIR):
        if filename.endswith('.log'):
            with open(os.path.join(LOG_DIR, filename), 'r') as f:
                for line in f:
                    try:
                        log_entry = json.loads(line.strip())
                        logs.append(log_entry)
                    except json.JSONDecodeError:
                        continue
    return logs

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search_logs():
    level = request.args.get('level')
    log_string = request.args.get('log_string')
    start_time = request.args.get('start_time')
    end_time = request.args.get('end_time')
    source = request.args.get('source')

    logs = load_logs()
    results = []

    for log in logs:
        if level and log['level'] != level:
            continue
        if log_string and log_string not in log['log_string']:
            continue
        if source and log['metadata']['source'] != source:
            continue
        log_time = datetime.fromisoformat(log['timestamp'].replace('Z', '+00:00'))
        if start_time and log_time < datetime.fromisoformat(start_time):
            continue
        if end_time and log_time > datetime.fromisoformat(end_time):
            continue
        results.append(log)

    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
