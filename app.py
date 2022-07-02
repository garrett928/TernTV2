"""App entry point."""
from TernTV2 import create_app

app = create_app()
PROJECT_PATH = '/home/garrett/software/TernTV2'

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)