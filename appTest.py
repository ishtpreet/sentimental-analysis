from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def tryHTML():
    return render_template('try.html')

@app.route('/get_text', methods=['GET', 'POST'])
def get_text():
	# if request.method == 'POST':
	# 	text = request.get_json()
		
	# else:
	# 	print('Some ERROR occured')
	if request.method == "POST":
		textFromSpeech = request.form["textFromSpeech"]

	return render_template('result.html', textFromSpeech = textFromSpeech) 

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
