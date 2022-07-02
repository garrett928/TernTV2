"""Route declaration."""
from flask import current_app as app
from flask import render_template
from TernTV2.tern_helpers.status_grabber import tern_status


@app.route("/")
def home():
    """Landing page."""
    return render_template(
        'home.html',
        title="Jinja Demo Site",
        description="Smarter page templates with Flask & Jinja."
    )

# show the intern status messages
@app.route("/tern_status")
def status_page():
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
@app.route("/slide_1")
def slide_1():
    return render_template(
        '/slides/slide_base.html',
        frame_1="http://127.0.0.1:5000/tern_status",
        frame_2="http://127.0.0.1:5000/tern_status",
        frame_3="http://127.0.0.1:5000/tern_status",
        frame_4="http://127.0.0.1:5000/tern_status"
        )