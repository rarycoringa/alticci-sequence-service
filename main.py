import os

from sequence.app import app

if __name__ == "__main__":
    debug = os.environ.get("DEBUG", "TRUE")
    debug = True if debug.lower() == "true" else False

    app.run(host="0.0.0.0", port="8000", debug=debug)
