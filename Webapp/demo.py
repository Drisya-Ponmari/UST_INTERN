from flask import Flask,jsonify,make_response

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


@app.route('/todo/<int:task_id>',methods=['GET'])
def get_tasks(task_id):
	task = [task for task in tasks if task['id'] == task_id]
	if len(task) ==0:
		abort(404)
	return jsonify({'task':task[0]})

@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error':'Not found'}),404)

@app.route('/')
def index():
	return "Hi"

if __name__ == "__main__":
	app.run()
