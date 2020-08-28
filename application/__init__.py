from flask import Flask

app = Flask(__name__)

app.secret_key = b'xxjadahcdhs\n\xec]/'

from application import routes
from application import utilities
from application import logic

if __name__ == "__main__":
    app.run()