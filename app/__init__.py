from flask import Flask

app = Flask(__name__)




def create_app():
    app = Flask(__name__)

    # Load configuration
    app.config.from_object('config.Config')

    # Register Blueprints (if using multiple routes in a modular app)
    # from .chatbot import chatbot_blueprint
    # app.register_blueprint(chatbot_blueprint)

    # Initialize other components like OpenAI API or database

    return app

from app import chatbot
