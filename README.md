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

# Django 

 ## Views
 Views in Django are like the "brain" of your application. They take in user requests, process them (often involving querying the database), and return a response. Views can return different types of responses, such as HTML, JSON, or even an error message.

 ## Templates
 Templates are HTML files with placeholders for dynamic content. They determine how the content will be displayed to the user. Django uses a templating engine that allows you to embed Django Template Language (DTL) to add logic like loops and conditionals.


 ## Model
 Models are the "blueprints" for your database. They define the structure of your data, specifying the fields and types of data you want to store. Models are Python classes that Django converts into database tables.

 ## File Structure
 ```
  myproject/
│
├── myproject/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
│
├── manage.py
├── db.sqlite3
```
  
 
 
### Basic Flow of Djnago

`User`--(request to website)--`Django`---Url Resolver--`urls.py`--(may redirect to other urls)--`views.py`(main controller/logic here)--via or without model.py access db.

views may use templates.


## creating an app
 
```
python manage.py startapp
```

After creating an app next we have to do is make the project aware of the app.

Inside `settings.py` add `appName` inside installed apps.

Form folder `template/newApp` inside the new App.

1. Here write the html to be rendered,
give its reference to views then.
2. Copy urls from original projects url.py to `newApp`'s newly formed `url.py`

This is URL.py refereing to subURL.py in Django
Then pass the control from original URL.py to subURL.



### Django app structure
```
 myproject/
│
├── myproject/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
│
├── myapp/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py `contains API views`
│   ├── urls.py  `contains URL patterns for API endpoints`
│   ├── tests.py
│
├── templates/
│   ├── myapp/
│       ├── index.html
│       ├── about.html
│       ├── contact.html
│
├── manage.py
├── db.sqlite3
 ``` 


Jinja2- templating engine.

Templating ?
-ek palta base structure banaisakepaxi tyo sabai thau bhayeko ramro, that's templating
for eg navbar is same for multipages

# Adding Tailwind CSS in Django


Installing tailwind via uv directly (if it works)
```
uv pip install django-tailwind
uv pip install 'django-tailwind[reload]'
```

If not try :
Initially installing pip for reduced errors, try any one of 2 methods:
```
python -m ensurepip --upgrade 
python -m pip install --upgrade pip
```

Then install tailwind via pip : 
```
pip install django-tailwind
pip install 'django-tailwind[reload]'
```
settings.py ma gayera application ma 'taiwind' thapne

`python manage.py tailwind init`
This will download some packages and form new folder which you have to give _newname_

in settings.py:
**installed_apps =[]** ma : _tailwind_ thapne
also add :
- **TAILWIND_APP_NAME:** _'newname'_
- **INTERNAL IPS: ['']**   
i.e array and string inside and 
- **NPM_BIN_PATH:** _r"C:\Program Files\nodejs\npm.cmd"_  
to generate this `from where npm` in cmd : _r"path"_

`python manage.py tailwind install`

- In template base html page add 
```
{% load static tailwind_tags %}
...
<head>
   ...
  {% tailwind_css %}
 ...
</head>
```

Tailwind ko lagi naya terminal banaune
`python manage.py tailwind start`

- You may need to restart app because you have not yet configured hot reloading.

### Hot reloading 
Hot reload (or hot reloading) is a feature commonly used in web development that allows developers to see changes to their code in real-time without needing to restart the development server or refresh the browser manually.

 Since we have already installed the `django-tailwind[reload]` package, we can use the tailwind-django command to enable hot reloading in our project.

Add it to your _INSTALLED_APPS_ in your _settings.py_ file:

```
INSTALLED_APPS = [
    # ...
    'django_browser_reload',
    #...
]
```

_Now hot reloading is possible_.

# Django Admin Panel

in case you forget password :
`python manage.py changepassword userName`

# Django Models
used to define the structure of database and relationship between different models.
Model is a python class that represents table in db.  
It contains fields that define structure of table and methods that define the behaviour of table.

- Usually data related files/models are not created/handled in main project.
i.e so inside the app.

### Defining a model
use models.py file in Django project
```
from django.db import models
from django.utils import timezone

# Creation of model

class modelName(models.Model):

  field1= models.
  field2=
  field3=
```

### Install Pillow library to use image field

when you want to put images or use image field you have to do changes in settings.py of project.

```
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

then to reflect media files configure in main project's urls.py
```
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    #...
    #...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

### Adding data to DB
The django doesnt yet know we have added a new model so letting it know
via migrations.
To migrate the DB and add data to new `userModel` model.
```
python manage.py makemigrations chai
python manage.py migrate
```

Now to add some data to DB.
Admin.py sanga kunai pani model attach garera admin panel ma herna milxa
For this goto admin.py and add following code to `userModel`
```
from django.contrib import admin
...
from .models import modelName

admin.site.register(modelName)
```








