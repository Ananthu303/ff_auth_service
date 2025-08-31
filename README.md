# Auth Service

A Django-based authentication microservice with JWT authentication, containerized using Docker.  
Built with **Django REST Framework**, **drf-spectacular**, and **PostgreSQL**.

---

## 🚀 Features
- User signup & login with **JWT tokens**
- Secure authentication (`access` & `refresh` tokens)
- Authenticated user profile endpoint (`/users/me/`)
- PostgreSQL integration
- Dockerized for easy deployment
- API documentation with **Swagger / OpenAPI**

---

## 📦 Requirements
- Python **3.10+**
- Docker & Docker Compose
- PostgreSQL (if running outside Docker)

---

## ⚙️ Environment Variables

Create a `.env` file in the project root refering using env_sample:


## Run with Docker

docker-compose up --build

Access the app at : http://localhost:8000

## API Endpoints
## Method  	Endpoint	  Description

POST	/users/signup/	Register a new user

POST	/users/login/	Login & get JWT tokens

GET	/users/me/	Get current user profile


## API Documentation

Once running, API docs are available at:

Swagger UI: http://localhost:8000/api/docs/

Raw schema: http://localhost:8000/api/schema/
