import logging
import os
import sys

from dinosaur.app import create_app


logger = logging.getLogger('uvicorn')

for handler in logger.handlers:
    handler.setStream(sys.stdout)


firebase_config_json = os.environ["FIREBASE_CONFIG"]

app = create_app(firebase_config_json)
