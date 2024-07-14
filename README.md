# Django_init

This repository consists of everything basics you need to know about Django and revise it whenever necessary.

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

- creating a virtual environment with uv
```
uv venv
```

- **to activate the virtual environment**
```
.venv\Scripts\activate
```
My personal error of prevention of running scripts.  
`Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
`

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


# File Structure

Root Level:
-manage.py
-Filename_Projectfolder
  -cache
  -settings.py
  -urls.py

-db.Sqlite3


User--(request to website)--Django---Url Resolver--urls.py--(may redirect to other urls)--views.py(main controller/logic here)--via or without model.py access db.
-views may use templates.


### creating an app
 
```
python manage.py startapp
```

After creating an app next we have to do is make the project aware of the app.

inside `settings.py` add `appName` inside installed apps.
form folder `template/newApp` inside the new App



### Django app structure


Jinja2- templating engine.