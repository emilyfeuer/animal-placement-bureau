# APB Site Repository

## Installation and Setup:

Before installing Django, you should first create a virtual environment. To do so, navigate to the chosen location of your project in a terminal and enter this command:

```
python -m venv venv
```

Now that you've made the virtual environment, you can use it with the below command. 

```
venv/Scripts/activate
```

At this point, you should see something like "(venv)" to the left in your terminal. Next, it's time to install Django in the virtual environment with this command:

```
pip install django
```

Now that you have Django installed, you can clone this project and start working on it.

## Project Structure:

A Django web app consists of a single project that is split into one or more apps that each have specific tasks/functionality. There is currently one app titled "Pages" that serves the site index. To view your local instance of this project, enter the outer "abpsite" directory (the one with manage.py in it) and enter the command ```python manage.py runserver```. From there, go to the link given in the terminal (something like http://127.0.0.1:8000/) and you should see the site.





