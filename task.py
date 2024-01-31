from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = [
    {"id": 1, "title": "Task 1", "description": "Description for Task 1", "status": "In Progress"},
    {"id": 2, "title": "Task 2", "description": "Description for Task 2", "status": "To Do"},
]

# Get all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({"tasks": tasks})

# Get a specific task by ID
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({"error": "Task not found"}), 404
    return jsonify({"task": task})

# Create a new task
@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    new_task = {
        "id": len(tasks) + 1,
        "title": data["title"],
        "description": data["description"],
        "status": data["status"],
    }
    tasks.append(new_task)
    return jsonify({"task": new_task}), 201

# Update an existing task
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({"error": "Task not found"}), 404

    data = request.get_json()
    task.update({
        "title": data["title"],
        "description": data["description"],
        "status": data["status"],
    })
    return jsonify({"task": task})

# Delete a task
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return jsonify({"result": "Task deleted"})


if __name__ == '__main__':
    app.run(debug=True)
