# Imports 

import os
# The 'load_dotenv' function from the 'dotenv' library is used to load variables from our .env file.
from dotenv import load_dotenv

# Load Environment Variables 
# This command looks for a .env file in the project's root directory and loads its contents into environment variables.
load_dotenv()

# Configuration Variables 
# Read the 'GOOGLE_API_KEY' environment variable.
# If it's not found, it defaults to None.
API_KEY = os.getenv("GOOGLE_API_KEY")

# Validation 
if not API_KEY:
    raise ValueError("🔴 Google API Key not found. Please set the GOOGLE_API_KEY environment variable.")