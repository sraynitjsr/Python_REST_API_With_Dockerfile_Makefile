from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Configure MySQL database connection
db = mysql.connector.connect(
    host="localhost",
    user="sraynitjsr",
    password="Tufan2020",
    database="task_database"
)
cursor = db.cursor()

@app.route('/tasks', methods=['GET'])
def get_tasks():
    cursor.execute("SELECT * FROM task")
    tasks = cursor.fetchall()
    task_list = [{"id": task[0], "title": task[1], "done": task[2]} for task in tasks]
    return jsonify({'tasks': task_list})

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    cursor.execute("SELECT * FROM task WHERE task_id = %s", (task_id,))
    task = cursor.fetchone()
    if task is None:
        return jsonify({'error': 'Task not found'}), 404
    return jsonify({'task': {'id': task[0], 'title': task[1], 'done': task[2]}})

@app.route('/tasks', methods=['POST'])
def create_task():
    if not request.json or 'title' not in request.json:
        return jsonify({'error': 'Invalid request'}), 400
    title = request.json['title']
    cursor.execute("INSERT INTO task (title, done) VALUES (%s, %s)", (title, False))
    db.commit()
    new_task_id = cursor.lastrowid
    return jsonify({'task': {'id': new_task_id, 'title': title, 'done': False}}), 201

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    cursor.execute("SELECT * FROM task WHERE task_id = %s", (task_id,))
    task = cursor.fetchone()
    if task is None:
        return jsonify({'error': 'Task not found'}), 404
    if not request.json:
        return jsonify({'error': 'Invalid request'}), 400
    title = request.json.get('title', task[1])
    done = request.json.get('done', task[2])
    cursor.execute("UPDATE task SET title = %s, done = %s WHERE task_id = %s", (title, done, task_id))
    db.commit()
    return jsonify({'task': {'id': task_id, 'title': title, 'done': done}})

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    cursor.execute("SELECT * FROM task WHERE task_id = %s", (task_id,))
    task = cursor.fetchone()
    if task is None:
        return jsonify({'error': 'Task not found'}), 404
    cursor.execute("DELETE FROM task WHERE task_id = %s", (task_id,))
    db.commit()
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True)
