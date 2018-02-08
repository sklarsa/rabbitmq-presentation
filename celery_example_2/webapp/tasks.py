import time
from main import app


@app.task
def run_user_query(length):
    print("Running user query...")
    time.sleep(length)
