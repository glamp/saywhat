from flask import Flask, render_template, request, jsonify
import traceback
import json

app = Flask(__name__)

#Accept a Post request
@app.route('/', methods=['POST'])
def parse_request():
	#Is the data sent JSON data
	if request.json:
		#Parse JSON for data
		response=request.json
		x = response.get('x')
		y = response.get('y')
		words = response.get('words')
		date = response.get('date')
		#Write to "database"
		with open('./static/markers.txt', 'a') as f:
			f.write(''+str(x)+" "+str(y)+" "+str(words)+" "+str(date)+"\n")
	return jsonify(request.json)

@app.route('/data/')
def sendData():
	#Send back one string of entire "database" history
	s = ''
	try:
		with open('./static/markers.txt') as f:
			for line in f:
				s+=line
		return s
	except Exception:
		print "Error: "+str(traceback.print_exc())
		return ''		
		#return str(traceback.print_exc())	


@app.route('/')
def index(name = None):
	try:
		#Render template
		return render_template('index.html', name = name)
	except Exception:
		print "There was an error: " + str(traceback.print_exc())


if __name__ == '__main__':
	#Debug mode, public IP, port 80
	app.run(host='0.0.0.0', port=80)
