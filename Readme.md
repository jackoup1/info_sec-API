# **Project Documentation**

## **Index**
1. [Overview](#overview)
2. [Project Structure](#project-structure)
3. [Functionality and Endpoints Examples](#functionality-and-endpoints-examples)
   - [Authentication](#1-authentication)
   - [User Management](#2-user-management)
   - [Product Management](#3-product-management)
4. [Database Models](#database-models)
   - [User Model](#1-user-model)
   - [Product Model](#2-product-model)
5. [Security](#security)
6. [Configuration](#configuration)
7. [Installation and Setup](#installation-and-setup)
   - [Prerequisites](#1-prerequisites)
   - [Steps to Run the Project](#2-steps-to-run-the-project)
8. [Conclusion](#conclusion)

---

## **Overview**
This project is a Flask-based web application that provides user authentication, user management, and product management functionalities. It uses SQLAlchemy for database interactions and JWT (JSON Web Tokens) for secure authentication. The application is designed to be modular, with separate routes and models for users and products.

[Back to Index](#index)

---

## **Project Structure**
The project is organized into the following files and directories:

1. **`main.py`**: The entry point of the application. It initializes the Flask app, configures the database, and registers the blueprints for different routes.
2. **`config.py`**: Contains configuration settings for the application, such as the secret key and database URI.
3. **`models/`**: Contains the database models.
   - **`user.py`**: Defines the `User` model for user management.
   - **`product.py`**: Defines the `Product` model for product management.
4. **`routes/`**: Contains the route handlers for the application.
   - **`authentication.py`**: Handles user signup and login.
   - **`user_routes.py`**: Handles user-related operations (e.g., updating user details).
   - **`product_routes.py`**: Handles product-related operations (e.g., adding and retrieving products).
5. **`utils/`**: Contains utility functions.
   - **`security.py`**: Provides JWT token generation and verification.
6. **`requirements.txt`**: Lists all the dependencies required to run the project.

[Back to Index](#index)

---

## **Functionality and Endpoints Examples**

### **1. Authentication**
The application provides user authentication using JWT (JSON Web Tokens). Users can sign up and log in to the system.

#### **Endpoints:**
- **Signup**:  
  - **Endpoint**: `/signup`  
  - **Method**: `POST`  
  - **Request Body**:  
    ```json
    {
      "name": "John Doe",
      "username": "johndoe",
      "password": "password123"
    }
    ```
  - **Response**:  
    ```json
    {
      "message": "User registered successfully"
    }
    ```
  - **Description**: Registers a new user in the system.

- **Login**:  
  - **Endpoint**: `/login`  
  - **Method**: `POST`  
  - **Request Body**:  
    ```json
    {
      "username": "johndoe",
      "password": "password123"
    }
    ```
  - **Response**:  
    ```json
    {
      "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
    }
    ```
  - **Description**: Authenticates the user and returns a JWT token for subsequent requests.

[Back to Index](#index)

---
### **2. User Management**
Users can update their details (name and username) after logging in. The endpoints are protected by JWT authentication.

#### **Endpoints:**
- **Update User**:  
  - **Endpoint**: `/users/<int:id>`  
  - **Method**: `PUT`  
  - **Request Body**:  
    ```json
    {
      "name": "John Doe Updated",
      "username": "johndoe_updated"
    }
    ```
  - **Response**:  
    ```json
    {
      "message": "User updated successfully"
    }
    ```
  - **Description**: Updates the user's name and/or username.

[Back to Index](#index)

---

### **3. Product Management**
Products can be added and retrieved from the system. The endpoints are protected by JWT authentication.

#### **Endpoints:**
- **Add Product**:  
  - **Endpoint**: `/products`  
  - **Method**: `POST`  
  - **Request Body**:  
    ```json
    {
      "pname": "Laptop",
      "description": "A high-performance laptop",
      "price": 1200.50,
      "stock": 10
    }
    ```
  - **Response**:  
    ```json
    {
      "message": "Product added successfully"
    }
    ```
  - **Description**: Adds a new product to the system.

- **Get Products**:  
  - **Endpoint**: `/products`  
  - **Method**: `GET`  
  - **Response**:  
    ```json
    [
      {
        "pid": 1,
        "pname": "Laptop",
        "description": "A high-performance laptop",
        "price": 1200.50,
        "stock": 10,
        "created_at": "2023-10-01T12:00:00Z"
      }
    ]
    ```
  - **Description**: Retrieves a list of all products in the system.

[Back to Index](#index)

---

## **Database Models**

### **1. User Model**
The `User` model represents a user in the system. It has the following fields:
- **`id`**: Primary key (auto-incrementing integer).
- **`name`**: The user's full name (string, max length 25).
- **`username`**: The user's unique username (string, max length 50).
- **`password`**: The user's hashed password (string, max length 256).

#### **Methods:**
- **`set_password(password)`**: Hashes the password and stores it.
- **`check_password(password)`**: Verifies if the provided password matches the stored hash.

---

### **2. Product Model**
The `Product` model represents a product in the system. It has the following fields:
- **`pid`**: Primary key (auto-incrementing integer).
- **`pname`**: The product's name (string, max length 100).
- **`description`**: The product's description (text, optional).
- **`price`**: The product's price (numeric, 10 digits with 2 decimal places).
- **`stock`**: The product's stock quantity (integer).
- **`created_at`**: The timestamp when the product was created (datetime, defaults to current time).

[Back to Index](#index)

---

## **Security**
The application uses JWT for secure authentication. The following security measures are implemented:
- **Token Generation**: Tokens are generated using the `generate_token` function in `security.py`. Tokens expire after 10 minutes.
- **Token Verification**: The `verify_token` decorator is used to protect routes. It checks for a valid token in the `Authorization` header.

[Back to Index](#index)

---

## **Configuration**
The application's configuration is defined in `config.py`. Key settings include:
- **`SECRET_KEY`**: Used for signing JWT tokens. It is fetched from environment variables or defaults to a hardcoded value.
- **`SQLALCHEMY_DATABASE_URI`**: The URI for the MySQL database.
- **`SQLALCHEMY_TRACK_MODIFICATIONS`**: Disabled to avoid unnecessary overhead.

[Back to Index](#index)

---

## **Installation and Setup**

   ### **1. Prerequisites**
   - Python 3.x
   - MySQL database
   - `pip` for installing dependencies

---
   
### **2. Steps to Run the Project**

1. **Clone the repository**:
   ```bash
      git clone https://github.com/jackoup1/info_sec-API.git
      cd <project_directory>
   ```   
   -  **Install dependencies:**
      ```bash
         pip install -r requirements.txt
      
   -  **Create the Database:**
      ```sql
         CREATE DATABASE info_sec;
      
   - **Create the Tables:**
      ```sql
         USE info_sec;
         
         CREATE TABLE users (
         id INT AUTO_INCREMENT PRIMARY KEY,
         name VARCHAR(25) NOT NULL,
         username VARCHAR(50) NOT NULL UNIQUE,
         password VARCHAR(256) NOT NULL
         );
         
         CREATE TABLE products (
         pid INT AUTO_INCREMENT PRIMARY KEY,
         pname VARCHAR(100) NOT NULL,
         description TEXT,
         price DECIMAL(10, 2) NOT NULL,
         stock INT NOT NULL,
         created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
         );
      
   - **Run the application:**
      ```bash
         python main.py
   
   - **Access the API:**
      -The application will run on http://127.0.0.1:5000.
      -Use tools like Postman or cURL to interact with the API
   
   [Back to Index](#index)
---
## **Conclusion**
   This project provides a secure and modular Flask-based API for user and product management. It is designed to be easily extendable, with clear separation of concerns between models, routes, and utilities. The use of JWT ensures secure authentication, and the modular    structure makes it easy to add new features in the future.
   
[Back to Index](#index)
