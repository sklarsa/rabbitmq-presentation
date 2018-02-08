from tasks import fit_neural_net, run_user_query

for x in range(4):
    fit_neural_net.delay(10)

for x in range(40):
    run_user_query.delay(0.1)
