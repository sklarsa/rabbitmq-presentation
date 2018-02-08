import time
from main import app


@app.task
def fit_neural_net(length=15):
    print("Fitting neural net...")
    time.sleep(length)
    print("Done fitting neural net!")


@app.task
def run_user_query(length=0.2):
    print("Running user query...")
    time.sleep(length)
    print("Done running user query!")
