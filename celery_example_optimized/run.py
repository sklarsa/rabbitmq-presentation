from neural_net.tasks import fit_neural_net
from webapp.tasks import run_user_query

for x in range(4):
    fit_neural_net.delay()

for x in range(200):
    run_user_query.delay()
