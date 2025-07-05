

from flask import Flask, render_template, request, jsonify
from calculator import Calculator, CalculatorError

app = Flask(__name__)
calc = Calculator()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/calc', methods=['POST'])
def api_calc():
    data = request.get_json() or {}
    expr = data.get('expression', '')
    try:
        result = calc.calculate(expr)
        return jsonify({'result': result})
    except CalculatorError as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)