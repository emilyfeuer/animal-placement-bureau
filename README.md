# APB Site Repository

## Installation and Setup:

The below instructions assume that you have Git and Python installed. If you do not have these, follow the links below to install what you need. 

Git: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git

Python: https://www.python.org/downloads/


Before installing Django, you should first create a virtual environment. To do so, navigate to the chosen location of your project in a terminal and enter this command to create a virtual environment called "venv":

```
python -m venv venv
```

Now that you've made the virtual environment, you can use it with the below command. 

Windows:
```
venv/Scripts/activate
```

Mac:
```
source venv/bin/activate
```

At this point, you should see something like "(venv)" to the left in your terminal. Next, it's time to install Django in the virtual environment with this command:

```
pip install django
```

Now that you have Django installed, you can clone this project and start working on it.

## Project Structure:

A Django web app consists of a single project that is split into apps that each have their own specific purpose/functionality. Here is the framework of this django project:

```
apbsite/
├── .env
├── manage.py
├── apbsite/
│   ├── __init__.py
│   ├── asgi.py
│   ├─ settings.py
│   ├─ urls.py
│   ├── wsgi.py
├── pages/
    ├── migrations/
    │   └── __init__.py
    │   └── 0001_initial.py
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    ├── urls.py
    └── views.py
```

To view your local instance of this project, enter the outer "abpsite" directory (the one with manage.py in it) and enter the command ```python manage.py runserver```. From there, go to the link given in the terminal (something like http://127.0.0.1:8000/) and you should see the site. (Ignore the .env file for now, more on that later)

### Main Project Directory

The main project directory (the outer "apbsite" directory) contains several files and subdirectories that apply universally across the project. Here are some short descriptions:

- **manage.py**: this file serves as a command-line tool for administrative tasks, such as starting the server.
- **apbsite/settings.py**: Configuration settings for the project. Different aspects of functionality (such as database configurations) are defined here.
- **apbsite/urls.py**: Used to define URLs for the project, mapping a URL to a view (a view is a function that renders HTML, among other things).
- **apbsite/wsgi.py**: WSGI stands for Web Server Gateway Interface: this file is utilized when deploying to a production server.
- **apbsite/asgi.py**: ASGI stands for Asynchronous Server Gateway Interface: this file is utilized when deploying to an asynchronous web server.

### Application Directory



