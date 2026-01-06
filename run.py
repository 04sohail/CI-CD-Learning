from config import PYTHON_ENV, HOST, PORT, PYTHON_WORKER
from subprocess import Popen
import sys
import argparse
import signal


def start_server():
    if PYTHON_ENV == "DEV":
        command = [
            "uvicorn",
            "app.main:app",
            "--host",
            str(HOST),
            "--port",
            str(PORT),
            "--reload",
        ]
    else:
        command = [
            "gunicorn",
            "-w",
            str(PYTHON_WORKER),
            "-k",
            "uvicorn.workers.UvicornWorker",
            "--bind",
            f"{HOST}:{PORT}",
            "--timeout",
            "300",
            "app.main:app",
        ]

    process = Popen(command)

    def shutdown(*_):
        process.terminate()
        process.wait()
        sys.exit(0)

    signal.signal(signal.SIGTERM, shutdown)
    signal.signal(signal.SIGINT, shutdown)

    process.wait()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=["server", "celery"])
    args = parser.parse_args()

    if args.command == "server":
        start_server()