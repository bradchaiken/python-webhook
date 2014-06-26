from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def real_time_api():
	if request.method == 'POST':
		print request.data
		return ""

if __name__ == '__main__':
    app.run()