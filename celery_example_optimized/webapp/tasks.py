import time
from main import app


@app.task
def run_user_query():
    print("Running user query...")
    time.sleep(0.1)
