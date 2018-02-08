from tasks import fit_neural_net, run_user_query

for x in range(5):
    fit_neural_net.delay()

for x in range(20):
    run_user_query.delay()
