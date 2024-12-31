import os

class Config:
    """Base configuration class."""
    
    # Flask settings
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key')  # Use a secure key in production
    FLASK_APP = os.getenv('FLASK_APP', 'run.py')
    FLASK_ENV = os.getenv('FLASK_ENV', 'development')
    
    # OpenAI API settings
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    
    # Other potential configurations (example)
    # DATABASE_URL = os.getenv('DATABASE_URL')  # For connecting to a database if needed
    # DEBUG = os.getenv('DEBUG', True)  # Optional: Can be set based on environment

class DevelopmentConfig(Config):
    """Development configuration class."""
    DEBUG = True
    TESTING = False
    # Other development-specific settings

class ProductionConfig(Config):
    """Production configuration class."""
    DEBUG = False
    TESTING = False
    # Other production-specific settings

class TestingConfig(Config):
    """Testing configuration class."""
    DEBUG = True
    TESTING = True
    # Other testing-specific settings
