"""Route declaration."""
from flask import current_app as app
from flask import render_template


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
        status=status
    )