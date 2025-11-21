📦 Flask Inventory Manager App

A lightweight, fully functional inventory management system built with Flask, SQLite, and Tailwind CSS.
Users can sign up, sign in, add products, edit them, and delete them.
Designed to be clean, modular, and ready for deployment on platforms like Render or Railway.

🚀 Features
🔐 Authentication

User signup

User login

Password hashing

Session-based authentication

📦 Product Management

Add new products

Edit product details

Delete products

View full inventory list

🗂️ Database

SQLite (local development)

SQLAlchemy ORM

User & Product models

flask_inventory_manager/
│
├── instance/ # Database + config (ignored by Git)
├── migrations/ # Flask-Migrate files (optional)
├── website/
│ ├── static/ # CSS, JS, images
│ ├── templates/ # HTML templates
│ ├── **init**.py # App factory
│ ├── auth.py # Authentication routes
│ ├── routes.py # Product routes
│ ├── models.py # Database models
│ └── utility.py # Helpers/utilities
│
├── main.py # Development server entry point
├── wsgi.py # Production entry for Gunicorn/Render
├── requirements.txt # Dependencies
├── README.md # Project documentation
└── .gitignore # Files/folders to ignore

🛠️ Tech Stack

Python 3

Flask

SQLAlchemy

Flask-Migrate

SQLite

Tailwind CSS

Jinja2 templates

Python Dotenv
