import multiprocessing
import time
import requests
from app import app
import pytest

def run_app():
    app.run(port=5000)

@pytest.fixture(scope='session', autouse=True)
def flask_server():
    proc = multiprocessing.Process(target=run_app)
    proc.start()
    time.sleep(1)

    # Wait until the server is up
    for _ in range(10):
        try:
            requests.get("http://localhost:5000")
            break
        except requests.ConnectionError:
            time.sleep(0.5)
    else:
        proc.terminate()
        raise RuntimeError("Flask server did not start")

    yield

    proc.terminate()
    proc.join()
