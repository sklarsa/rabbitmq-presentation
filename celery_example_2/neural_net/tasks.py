import time
from main import app


@app.task
def fit_neural_net(length):
    print("Fitting neural net...")
    time.sleep(length)
    print("Done fitting neural net...")
