from flask import Flask

app = Flask(__name__)       #__name__ holds the string of the current module

@app.route('/')
def home():
    return f'<h1>Currency Rate API</h1> <p>Example URL: /api/v1/usd-eur</p>'

@app.route('/api/v1/<input_currency>-<output_currency>')
def api(input_currency, output_currency):
    

app.run()