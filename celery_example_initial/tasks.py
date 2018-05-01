import time
from main import app


@app.task
def fit_neural_net():
    print("Fitting neural net...")
    time.sleep(10)
    print("Done fitting neural net...")


@app.task
def run_user_query():
    print("Running user query...")
    time.sleep(0.1)
