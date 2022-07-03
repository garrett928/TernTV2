"""Route declaration."""
import imp
from flask import current_app as app
from flask import render_template
from TernTV2.tern_helpers.status_grabber import tern_status
from TernTV2.tern_helpers import passwd_grabber
import json


@app.route("/")
def home():
    """Landing page."""
    return render_template(
        'home.html',
        title="Jinja Demo Site",
        description="Smarter page templates with Flask & Jinja."
    )

"""
This block of app routes is for the individual webpages. For example, the daily password page,
daily quotes page, etc
"""

# show the intern status messages
@app.route("/tern_status")
def status_page():
    # only here for testing
    status = {
        "Garrett" : "Rock Sleeper",
        "Tessa" : "Concusion Getter",
        "Elizabeth" : "Robot Dog Haver"
    }
    return render_template(
        'tern_status.html',
        status=tern_status()
    )

# show the intern status messages
@app.route("/tern_pass")
def tern_pass():
    return render_template(
        'tern_pass.html',
        passwd=passwd_grabber.tern_pass()
    )

"""
This block of routes is the for slides pages. Slides are made up of one or more individual pages 
and will be what is shown on the TV.
"""


    # show the intern status messages
@app.route("/slide_1")
def slide_1():
    return render_template(
        '/slides/slide_2_x_2.html',
        frame_1="http://127.0.0.1:5000/tern_status",
        frame_2="http://127.0.0.1:5000/tern_pass",
        frame_3="http://127.0.0.1:5000/tern_pass",
        frame_4="http://127.0.0.1:5000/tern_status"
        )

        
# route to show raw json config file
@app.route("/tern_fig")
def tern_fig():
    json_file = 'tern_fig.json'

    with open(json_file) as jf:
        data = json.load(jf)
    jf.close()
    return data