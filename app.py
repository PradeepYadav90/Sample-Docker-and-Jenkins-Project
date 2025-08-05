from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory task list
todos = []

# Health check / landing route
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Flask To-Do API"}), 200

# Get all todos
@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos), 200

# Add a new todo
@app.route('/todos', methods=['POST'])
def add_todo():
    data = request.get_json()
    task = data.get('task')

    if not task:
        return jsonify({"error": "Task field is required"}), 400

    new_todo = {
        "id": len(todos) + 1,
        "task": task.strip()
    }

    todos.append(new_todo)
    return jsonify(new_todo), 201

# Delete a todo by ID
@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    global todos
    original_len = len(todos)
    todos = [todo for todo in todos if todo["id"] != todo_id]

    if len(todos) == original_len:
        return jsonify({"error": "To-do not found"}), 404

    return jsonify({"message": f"To-do with ID {todo_id} deleted"}), 200

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
