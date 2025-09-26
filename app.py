# app.py

from flask import Flask, jsonify, request

# Initialize the Flask application
app = Flask(__name__)

# In-memory "database" - a list of user dictionaries
users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"}
]
next_user_id = 3 # To auto-increment user IDs

# --- Helper Function ---
def find_user(user_id):
    """Finds a user by their ID."""
    return next((user for user in users if user["id"] == user_id), None)

# --- Routes ---

# GET all users
@app.route('/users', methods=['GET'])
def get_users():
    """Returns a list of all users."""
    return jsonify(users)

# GET a single user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Returns a single user if found, otherwise returns a 404 error."""
    user = find_user(user_id)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

# POST (create) a new user
@app.route('/users', methods=['POST'])
def create_user():
    """Creates a new user."""
    global next_user_id
    if not request.json or not 'name' in request.json or not 'email' in request.json:
        return jsonify({"error": "Missing name or email in request body"}), 400

    new_user = {
        "id": next_user_id,
        "name": request.json['name'],
        "email": request.json['email']
    }
    users.append(new_user)
    next_user_id += 1
    return jsonify(new_user), 201 # 201 Created status code

# PUT (update) an existing user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """Updates an existing user's details."""
    user = find_user(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    if not request.json:
        return jsonify({"error": "Invalid request"}), 400

    user['name'] = request.json.get('name', user['name'])
    user['email'] = request.json.get('email', user['email'])
    return jsonify(user)

# DELETE a user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """Deletes a user."""
    user = find_user(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    users.remove(user)
    return jsonify({"message": f"User with ID {user_id} deleted successfully"}), 200

# --- Run the App ---
if __name__ == '__main__':
    # debug=True enables auto-reloading. Do not use in production.
    app.run(debug=True)