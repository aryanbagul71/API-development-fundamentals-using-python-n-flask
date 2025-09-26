# API-development-fundamentals-using-python-n-flask
This project is a simple REST API built with Python and Flask to manage user data. It supports all standard CRUD operations (GET, POST, PUT, DELETE) and uses a basic in-memory list as a temporary database. This serves as a foundational example for understanding core API development concepts.
Simple User Management REST API with Flask
This project is a simple REST API built with Python and Flask to manage user data. It supports all standard CRUD (Create, Read, Update, Delete) operations and uses a basic in-memory list as a temporary database. This serves as a foundational example for understanding core API development concepts.

Features
List All Users: Retrieve a complete list of all users.

Get Single User: Fetch a single user by their unique ID.

Create User: Add a new user to the list.

Update User: Modify the details of an existing user.

Delete User: Remove a user from the list.

Technologies Used
Python 3.x

Flask: A lightweight web framework for Python.

Postman: An API platform for testing the endpoints.

Setup and Installation
Follow these steps to get the project running on your local machine. This guide is tailored for Windows users.

1. Clone the repository (or download the code):

git clone [https://github.com/your-username/your-repository-name.git](https://github.com/your-username/your-repository-name.git)
cd your-repository-name

2. Create and activate a virtual environment:

# Create a virtual environment named 'venv'
python -m venv venv

# Activate the virtual environment
.\venv\Scripts\activate

(You should see (venv) at the beginning of your terminal prompt after activation.)

3. Install the required dependencies:

pip install Flask

4. Run the application:

python app.py

The server will start and be accessible at http://127.0.0.1:5000.

API Endpoints Guide
The base URL for all endpoints is http://127.0.0.1:5000.

Method

Endpoint

Description

Request Body (JSON)

Success Response (200 OK)

GET

/users

Get a list of all users.

None

[{"id": 1, "name": "Alice", ...}, {"id": 2, ...}]

GET

/users/<int:id>

Get a single user by ID.

None

{"id": 1, "name": "Alice", "email": "alice@example.com"}

POST

/users

Create a new user.

{"name": "Charlie", "email": "charlie@example.com"}

(201 Created) {"id": 3, "name": "Charlie", ...}

PUT

/users/<int:id>

Update an existing user.

{"name": "Alice Smith"} (or other fields)

{"id": 1, "name": "Alice Smith", "email": "alice@example.com"}

DELETE

/users/<int:id>

Delete a user by ID.

None

{"message": "User with ID 1 deleted successfully"}

How to Test with Postman
Start the Flask server by running python app.py.

Open Postman and create a new request.

Select the HTTP method (e.g., POST) and enter the endpoint URL (e.g., http://127.0.0.1:5000/users).

For POST or PUT requests, go to the Body tab, select raw, and choose JSON from the dropdown. Enter the required data.

Click Send to see the API response.
