import os
from dinosaur.app import create_app

firebase_config_json = os.environ["FIREBASE_CONFIG"]

app = create_app(firebase_config_json)
