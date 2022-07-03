# TernTV2.0
All the latest intern news and updates brought to you on an underpowered and over priced raspberry pi

Note: The following instructions were written for Fedora 36 with Kernal 5.18.5. This should work fine on other linux distros and windows as well. 

# Dependencies
- Python 3.10
- Flask 2.1.2

Note: a lower version of python and flask may work but has not been tested
# Installation
Clone the repo:

`git clone https://github.com/garrett928/TernTV2.git`

`cd TernTV2.git`

## Virtual Environment
It's best practice to work inside a clean virtual environment. Doing this will keep all the python packages we are about to install local to this project and this project only. This will prevent other python projects from conflicting with this project and vice versa. Run the following command to create an environment. 

`python -m venv ./env`

Next, we need to activate the virtual environment in order to use it. Note: you will have to do this every time you open up a terminal to work on the project.

`source ./env/bin/activate`

You can check that the virtual environment is active by running:

`which python`

The output should be along the lines of "/path/to/this/project/env/bin/python". If it says "/usr/bin/python" then the environment is not active. 

Note: The paths mentioned above may be different on windows but the correct path should still include the path to your project folder. 

## Install dependicies
Inside the virtual enironment run:

`pip install -r requirements.txt`

# Running the application
To run the application simply type `flask run` from the top most project folder. Note: The project will not run if not ran from the top level project folder.

# Deployment

# Usage
The file `tern_fig.json` houses all of the settings and configurations for the project. Fellow interns can edit this file with quotes, status messages, lost intern count, and more! These settings will be updated live on the tern_tv screen. Simply navigate to a webpage, listed below, and get the latest intern news. 

### Webpages
- "/" is the home page. Right now its a default and random page
- "/tern_status" are the intern statuses, as read from the config file
- "/slide_1" will be the first slide to rotate on the TV. Most slides will be a combination of other webpages. Right now slide one shows four copies of the "/tern_status" page.

# TODO
- Create better templates for the "slides". A 2x2, a side by side vertical, side by side horizontal,etc
- Explain how this will be displayed on a tv using https://www.screenly.io/
- Add colors with CSS or something
- add instructions for enabling ssh on the pi
- add instructions for installing screenly
- make develop branch
- make pi auto pull new master branch changes

-tribal counsol pictures
-we tried kratos
-tux fan club art
-dino
-ai quote of the day
-intern quotes
-foosball leader board
-todays password
-today in histoy
-intern badges / roles
-rp chart / grid
-days since last
-allignment chart


More to come

temp links: 
https://hackersandslackers.com/flask-jinja-templates/
https://github.com/hackersandslackers/flask-jinja-tutorial/blob/master/flask_jinja_tutorial/routes.py
https://jinja.palletsprojects.com/en/2.11.x/
https://realpython.com/primer-on-jinja-templating/
https://code.tutsplus.com/tutorials/templating-with-jinja2-in-flask-essentials--cms-25571
https://dev.to/nagatodev/getting-started-with-flask-1kn1#:~:text=1%20Getting%20started%20with%20Flask,a%20Flask%20and%20React%20application.
https://dev.to/nagatodev/building-a-todo-list-application-with-flask-fcj
https://flask.palletsprojects.com/en/2.1.x/quickstart/
