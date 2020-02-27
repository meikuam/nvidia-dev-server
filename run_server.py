import logging
from src.flask import api


if __name__ == "__main__":
    api.flask_app.run(host='0.0.0.0', port=5000)
