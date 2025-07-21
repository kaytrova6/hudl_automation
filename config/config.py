import os

# Base URL for the application under test
BASE_URL = "https://www.hudl.com/login"
BROWSER = "chrome"  # Supported: "chrome", "firefox"
HEADLESS = False
IMPLICIT_WAIT = 10

# --- Credentials (Loaded from Environment Variables) ---

HUDL_USER = os.getenv("HUDL_USER")
HUDL_PASS = os.getenv("HUDL_PASS")

# Fail fast if credentials are not set in the environment
if not HUDL_USER or not HUDL_PASS:
    raise ValueError("Environment variables HUDL_USER and HUDL_PASS must be set to run the tests.")
