import os
from dotenv import load_dotenv

load_dotenv()

PYTHON_ENV: str = os.getenv("PYTHON_ENV", "DEV")

HOST: str = os.getenv("HOST", "0.0.0.0")
PORT: int = int(os.getenv("PORT", "9000"))
PYTHON_WORKER: int = int(os.getenv("PYTHON_WORKER", "1"))
SERVER_REQUEST_TIMEOUT: int = int(os.getenv("SERVER_REQUEST_TIMEOUT", "300"))

