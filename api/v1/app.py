from flask import Flask
from models import storage  # Importing storage from models module
from api.v1.views import app_views  # Importing app_views from views module


app = Flask(__name__)  # Creating an instance of Flask


@app.teardown_appcontext
def teardown_appcontext(exception):
    """
    Method to handle app teardown.
    """
    storage.close()  # Closing storage when app context is torn down


if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)  # Running Flask server
