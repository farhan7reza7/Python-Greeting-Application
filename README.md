Task Manager API Documentation
Introduction
This repository contains the source code for a simple Task Manager API built using Express.js. The API allows users to manage tasks by performing operations such as retrieving all tasks, getting a specific task by ID, creating a new task, updating a task, and deleting a task.

Getting Started
Prerequisites
Ensure you have the following installed on your machine:

Node.js
npm (Node Package Manager)
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/task-manager-api.git
Navigate to the project directory:

bash
Copy code
cd task-manager-api
Install dependencies:

bash
Copy code
npm install
Run the server:

bash
Copy code
npm start
The server will be running at http://localhost:3000.

API Endpoints
1. Get All Tasks
Endpoint: /api/tasks
Method: GET
Description: Retrieves a list of all tasks.
Example Response:
json
Copy code
[
  { "id": 1, "title": "Complete homework", "completed": false },
  { "id": 2, "title": "Prepare for meeting", "completed": true }
]
2. Get a Specific Task
Endpoint: /api/tasks/:id
Method: GET
Description: Retrieves a specific task by ID.
Example Response:
json
Copy code
{ "id": 1, "title": "Complete homework", "completed": false }
3. Create a New Task
Endpoint: /api/tasks
Method: POST
Description: Creates a new task.
Request Body:
json
Copy code
{ "title": "New task", "completed": false }
Example Response:
json
Copy code
{ "id": 3, "title": "New task", "completed": false }
4. Update a Task
Endpoint: /api/tasks/:id
Method: PUT
Description: Updates a task by ID.
Request Body:
json
Copy code
{ "title": "Updated task", "completed": true }
Example Response:
json
Copy code
{ "id": 3, "title": "Updated task", "completed": true }
5. Delete a Task
Endpoint: /api/tasks/:id
Method: DELETE
Description: Deletes a task by ID.
Example Response: 204 No Content
Conclusion
This Task Manager API provides a basic foundation for managing tasks.
