from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = [
    {"id": 1, "title": "Task 1", "done": False},
    {"id": 2, "title": "Task 2", "done": False},
]

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

if __name__ == '__main__':
    app.run(debug=True)
