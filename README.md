#  Task Management API using FastAPI
-This is a secure and scalable Task Management API built using FastAPI. It provides user authentication via JWT tokens and allows users to create, update, retrieve, and delete tasks.

## 📌 Features
- User Registration & Authentication (JWT-based)

- CRUD Operations for Tasks

- Secure Endpoints with JWT

- SQLite Database Integration

- Proper Error Handling

## 🛠 Tech Stack

- FastAPI

- SQLite (via SQLAlchemy)

- Pydantic

- Passlib (bcrypt for password hashing)

- Python-Jose (JWT authentication)

### 📂 Project Structure
```
project-task-management-api/
│── app/
│   ├── main.py  # Entry point
│   ├── database.py  # DB connection setup
│   ├── models.py  # SQLAlchemy models
│   ├── schemas.py  # Pydantic schemas
│   ├── auth.py  # Authentication Logic (JWT & Password Hashing)
│   ├── env.py  # for importing all the Secrets form .env file 
|   │── .gitignore # Ignore sensitive & unnecessary files
│── tasks.db  # SQLite database
│── requirements.txt
│── README.md
```

## 🔧 Installation & Setup

### 1.Clone the repository
```
git clone https://github.com/Alok5code/task-management-api.git
cd task-management-api
```

### 2.Create and activate a virtual environment
```
python -m venv venv   # Create virtual environment
source venv/bin/activate  # Activate (Linux/Mac)
venv\Scripts\activate  # Activate (Windows)
```
### 3.Set Up the .env File
```
SECRET_KEY=your_secret_key_here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
DATABASE_URL=sqlite:///./tasks.db
```
### 4.Install dependencies
```
pip install -r requirements.txt
```
### 5.Run the FastAPI server
```
uvicorn app.main:app --reload
```
### 6.Access API Documentation

Once the server is running, open the Swagger UI:

#### 🚀 Docs: http://127.0.0.1:8000/docs

#### 📜 Redoc: http://127.0.0.1:8000/redoc



## 🔑 Authentication Endpoints

### 1️⃣ User Registration (POST /auth/register)
- Request Body:

```
{
  "username": "testuser",
  "password": "securepassword"
}
```
- Response:

```
{"message": "User registered successfully"}
```

### 2️⃣ User Login (POST /auth/login)
- Request Body:

```
{
  "username": "testuser",
  "password": "securepassword"
}
```
- Response:

```
{
  "access_token": "jwt_token_here",
  "token_type": "bearer"
}
```
## 📋 Task Management Endpoints (JWT Protected)

| Method   | Endpoint           | Description       |
| -------- | ------------------ | ----------------- |
| `GET`    | `/tasks`           | Get all tasks     |
| `POST`   | `/tasks`           | Create a task     |
| `GET`    | `/tasks/{task_id}` | Get task by ID    |
| `PUT`    | `/tasks/{task_id}` | Update task by ID |
| `DELETE` | `/tasks/{task_id}` | Delete task by ID |

## 🔹 Add the JWT token in the Authorization header for protected endpoints:
```
Authorization: Bearer YOUR_ACCESS_TOKEN
```

### 3️⃣ Create Task (POST /tasks)
- Request Body:

```
{
  "title": "Complete Assignment",
  "description": "Finish the FastAPI project",
  "priority": "high"
}
```
- Response:

```
{
  "id": 1,
  "title": "Complete Assignment",
  "description": "Finish the FastAPI project",
  "status": "todo",
  "priority": "high"
}
```
### 4️⃣ Get All Tasks (GET /tasks)

- Response:
```
[
  {
    "id": 1,
    "title": "Complete Assignment",
    "description": "Finish the FastAPI project",
    "status": "todo",
    "priority": "high"
  }
]
```
### 5️⃣ Update Task (PUT /tasks/{task_id})
- Request Body:

```
{
  "status": "completed"
}
```
- Response:

```
{
  "id": 1,
  "title": "Complete Assignment",
  "description": "Finish the FastAPI project",
  "status": "completed",
  "priority": "high"
}
```
### 6️⃣ Delete Task (DELETE /tasks/{task_id})

- Response:
```
{"message": "Task deleted successfully"}
```

## 🛠 Running Tests
- You can test the API using Postman or curl commands.
Example:
```
curl -X GET http://127.0.0.1:8000/tasks -H "Authorization: Bearer <your-token>"
```
## Credit/Acknowledgment
- Alok Gairola
