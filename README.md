Student Managment Api 

A simple API built with Python, FastAPI, and MongoDB.
Description

This API provides endpoints to perform CRUD operations on a collection of items stored in a MongoDB database. 
It uses FastAPI to define the routes and handle HTTP requests, and MongoDB as the data storage solution.
Features

Create, Read, Update, and Delete operations for students.
MongoDB as the database backend.
FastAPI for defining routes and handling requests.
Swagger UI for interactive API documentation.

Installtion
Clone the repository:
git clone https://github.com/Harsh-rgb394/fastapi

Install dependencies:
pip install -r requirements.txt

Configure environment variables:
Create a .env file in the root directory of the project and add the following variables:
Mongo_url=Your_Url

Run the application:
uvicorn main:app --reload


Access the API documentation:

Open your web browser and navigate to http://localhost:8000/docs to access the Swagger UI for interactive API 
and also access to hosted api with access the Swagger UI for interactive API documentation.

Usage

Use HTTP methods (GET, POST, PUT, DELETE) to interact with the API endpoints.
Refer to the API documentation (/docs endpoint) for detailed information about available endpoints and request/response formats.

Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvement, please open an issue or submit a pull request.

License

This project is licensed under the MIT License - see the LICENSE file for details.

