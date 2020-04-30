from flask import Flask, render_template, request

app = Flask(__name__)

ButtonPressed = 0      

@app.route('/')
def index():
    return render_template('button.html', ButtonPressed = ButtonPressed)  

@app.route('/button', methods=["GET", "POST"])
def button():
    if request.method == "POST":
        global ButtonPressed
        ButtonPressed = ButtonPressed + 1
        return render_template("button.html", ButtonPressed = ButtonPressed)

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
