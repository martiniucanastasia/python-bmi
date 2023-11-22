from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    bmi = ''
    if request.method == 'POST':
        weight = float(request.form['weight'])
        height = float(request.form['height']) / 100
        bmi = weight / (height ** 2)
        bmi = f"Your BMI is: {bmi:.2f}"
    return render_template('index.html', bmi=bmi)

if __name__ == '__main__':
    app.run(debug=True)
