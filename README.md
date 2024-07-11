# Django_init

This repository consists of everything basics you need to know about Django and revise it whenever necessay.

## What is Django ?
 - high level Python framework that encourages rapid development and clean design.
 - known for simplicity
 - framework  that follows MVC architecutre
 - provides tools and libraries for building webapps
 - which includes built-in admin panel and ORM, templating engine.

## Environment setup
- creating a virtual environment **In Windows**.
```
python -m venv .venv
```

**Can use uv to manage virtual environment faster**
```
pip install uv
```

-creating a virtual environment with uv
```
uv venv
```

- **to activate the virtual environment**
```
.venv\Scripts\activate
```

- **To install Django finally with uv**
- to activate the virtual environment
```
uv pip install django
```


# Django Project

 - A Django project is a collection of settings and configurations that define the structure and behavior of a web application.

 - It includes the code for the application, as well as the templates, static files, and other resources that make up the application.

 ### To create a new Django Project

 ```
 django-admin startproject ProjectName
 ```
 ### Start a Django Server
 
 ```
 python manage.py runserver
 ```
 - This will start the server at _http://localhost:8000_

