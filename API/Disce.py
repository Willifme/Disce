from flask import Flask, jsonify, abort, make_response, request

app = Flask(__name__)

tasks = [

    {
        'id': 1,
        'title': u'Buy food',
        'description': u'Milk, Cheese, Pizza, Fruit',
        'done' : False
    },
    {
        'id' : 2,
        'title' : 'Learn Python',
        'description' : u'Need to find a good Python tutorial on the web',
        'done' : False
    }

]

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods = ['GET'])
def get_tasks(task_id):

    task = filter(lambda t: t['id'] == task_id, tasks)

    if len(task) == 0:
        abort(404)

    return jsonify( { 'tasks' : task[0] } )

@app.route('/todo/api/v1.0/tasks', methods = ['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify( { 'task': task } ), 201


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error' : 'Not found' } ), 404)

if __name__ == '__main__':
    app.run(debug = True)