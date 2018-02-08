from neural_net.tasks import fit_neural_net
from webapp.tasks import run_user_query

for x in range(4):
    fit_neural_net.delay(10)

for x in range(100):
    run_user_query.delay(0.1)