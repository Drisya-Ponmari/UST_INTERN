from flask import Flask,jsonify

app = Flask(__name__)


tasks =[
	{
		'id':1,
		'title':u'Sing',
		'done':False
	},
	{
		'id':2,
		'title':u'Dance',
		'done':False
	}
]


@app.route('/todo',methods=['GET'])
def get_tasks():
	return jsonify({'tasks':tasks})

@app.route('/')
def index():
	return "Hi"

if __name__ == "__main__":
	app.run()
