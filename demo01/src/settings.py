import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY', None)

if OPENAI_API_KEY is None:
    raise ValueError("Please set the OPENAI_API_KEY environment variable.")
