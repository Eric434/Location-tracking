from flask import Flask, render_template, request, jsonify
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/log_location', methods=['POST'])
def log_location():
    data = request.get_json()
    lat = data.get('latitude')
    lon = data.get('longitude')
    timestamp = datetime.datetime.now().isoformat()
    with open('locations.log', 'a') as f:
        f.write(f"{timestamp}: {lat}, {lon}\n")
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
