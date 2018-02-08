import time
from main import app


@app.task
def fit_neural_net(length):
    print("Fitting neural net...")
    time.sleep(length)
    print("Done fitting neural net...")


@app.task
def run_user_query(length):
    print("Running user query...")
    time.sleep(length)
