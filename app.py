from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def calculate_income_tax(income):
    # Tax calculation logic
    tax_slabs = [
        (250000, 0),
        (500000, 0.05),
        (1000000, 0.2),
        (float('inf'), 0.3)
    ]
    tax = 0
    previous_limit = 0
    for limit, rate in tax_slabs:
        if income > limit:
            tax += (limit - previous_limit) * rate
            previous_limit = limit
        else:
            tax += (income - previous_limit) * rate
            break
    return tax

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        income = float(request.form['income'])
        if income < 0:
            return jsonify({"error": "Income cannot be negative"})
        tax = calculate_income_tax(income)
        return jsonify({"income": income, "tax": tax})
    except ValueError:
        return jsonify({"error": "Invalid input. Please enter a numeric value."})

if __name__ == '__main__':
    app.run(port=3000, debug=True)

# commit "income_tax"