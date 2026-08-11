# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API using FastAPI that exposes endpoints for managing a collection of items. Practice defining routes, request and response models, and handling validation and errors in a modern web API.

## 📝 Tasks

### 🛠️ Create a FastAPI Application

#### Description
Create a new FastAPI application in a file named `main.py` and define a simple health-check endpoint.

#### Requirements
Completed program should:

- Import `FastAPI` and create an app instance.
- Add a `GET /health` endpoint that returns `{"status": "ok"}`.
- Start the app locally with `uvicorn main:app --reload`.

### 🛠️ Add a Resource with Pydantic Models

#### Description
Define a resource such as an item and create endpoints to add and retrieve it.

#### Requirements
Completed program should:

- Define a Pydantic model for the resource, including validation rules.
- Add a `POST /items` endpoint that creates a new item and returns it with a `201` status code.
- Add a `GET /items/{item_id}` endpoint that returns a specific item by id.
- Ensure invalid input is rejected with clear validation errors.

### 🛠️ Handle Errors and Query Parameters

#### Description
Make the API more robust by supporting lists and error handling for missing resources.

#### Requirements
Completed program should:

- Add a `GET /items` endpoint that lists all created items.
- Support a query parameter such as `limit` to restrict the number of results.
- Return a `404` response when an item is not found.
- Use response models so the API payloads are consistent.
