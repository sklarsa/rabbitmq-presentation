import time
from main import app


@app.task
def fit_neural_net():
    print("Fitting neural net...")
    time.sleep(10)
    print("Done fitting neural net...")
