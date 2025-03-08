import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DEBUG = os.getenv('DEBUG') == 'True'  
    SECRET_KEY = os.getenv('FLASK_SECRET_KEY')
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY') 
