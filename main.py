import os

from app import create_app

if __name__ == "__main__":
    app = create_app()

    debug = os.environ.get("DEBUG", True)
    debug = True if debug.lower() == "true" else False

    app.run(host="0.0.0.0", port="8080", debug=debug)
