from flask import Flask, redirect, url_for, request, render_template
from processPayment import process_payment
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
   
@app.route('/result', methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        payment_result = process_payment(result)
        return payment_result
        # return result['phone2Recharge']
        # return render_template('result.html', result = result)
    else:
        return 'Method not allowed'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)