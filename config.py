
import os
from dotenv import load_dotenv

# config.py (The Source of Truth)

# We use python-dotenv so you can keep sensitive keys in a .env file that is ignored by git.# 


load_dotenv()

# Get the current environment or default to 'dev'
CURRENT_ENV = os.getenv("TEST_ENV", "booker").lower()


ENVIRONMENTS = {
    "booker": {
        "base_url": os.getenv("RESTFFUL_BOOKER_URL", "https://restful-booker.herokuapp.com/"),
        "username": os.getenv("RESTFUL_BOOKER_USERNAME"),
        "password": os.getenv("RESTFUL_BOOKER_PASSWORD"),

        "timeout": 5

    },

    "placeholder": {
       "base_url": os.getenv("JSON_PLACE_HOLDER_URL", "https://jsonplaceholder.typicode.com"),
      "username": os.getenv("JSON_PLACE_HOLDER_USERNAME"),
       "timeout": 10


    },
    "juiceshop": {
        "base_url": os.getenv("PROD_BASE_URL", "https://eb360-demo.ethixcloud.com/"),
        "password": os.getenv("DEV_ADMIN_KEY"),
        "timeout": 15
    },
     "reqres": {
        "base_url": os.getenv("PROD_BASE_URL", "https://reqres.in//"),
        "password": os.getenv("DEV_ADMIN_KEY"),
        "timeout": 15
    },
     "eb360": {
        "base_url": os.getenv("EB360_BASE_URL", "https://aldrin.ethixdevelopment.com/"),
        "username": os.getenv("EB360_USER_NAME"),
        "password": os.getenv("EB360_PASSWORD"),
        "timeout": 15
    }
}


# Defaults
# ===========================================================
DEFAULT_ENV = os.getenv("TEST_ENV", "dev")
API_KEY = os.getenv("API_KEY", "default_secret_key")
TIMEOUT = 10
# ============================================================

# Helper to get the active config
def get_config(env_name=None):
   target_env = env_name.lower() if env_name else CURRENT_ENV
   if target_env not in ENVIRONMENTS:
        raise ValueError(f"Environment '{target_env}' not found in config.")
   return ENVIRONMENTS[target_env]

# Extract active config for easier access in other files
ACTIVE_CONFIG = get_config()
BASE_URL = ACTIVE_CONFIG["base_url"]
TIMEOUT = ACTIVE_CONFIG["timeout"]
