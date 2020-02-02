import requests
from dotenv import load_dotenv
import os
from pathlib import Path

load_dotenv(verbose=True)

env_path = Path('.') / '.env'

load_dotenv(dotenv_path=env_path)

def getenv(var_name):
    return os.getenv(var_name)

request_url = "http://phc.prontonetworks.com/cgi-bin/authlogin?URI="
payload = {
    "userId": getenv("USERNAME"),
    "password": getenv("PASSWORD"),
    "serviceName": "ProntoAuthentication",
    "Submit22": "Login",
}

r = requests.post(request_url, data=payload)
print(r.content)