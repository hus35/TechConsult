from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

# ملف JSON لتخزين طلبات التواصل
DATA_FILE = 'data.json'

# تحميل البيانات من JSON
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {"requests": []}

# حفظ البيانات إلى JSON
def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        data = load_data()
        new_request = {
            'name': request.form['name'],
            'email': request.form['email'],
            'message': request.form['message']
        }
        data['requests'].append(new_request)
        save_data(data)
        return jsonify({'status': 'success', 'message': 'Request submitted!'})
    return render_template('contact.html')

@app.route('/dashboard')
def dashboard():
    data = load_data()
    return render_template('dashboard.html', requests=data['requests'])

if __name__ == '__main__':
    app.run(debug=True)