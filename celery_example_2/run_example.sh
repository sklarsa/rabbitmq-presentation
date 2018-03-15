celery worker --app main --concurrency 1 -Q webapp -n worker-2 &
pid1=$!
celery worker --app main --concurrency 3 -Q neural_net -n worker-3 &
pid2=$!

python run.py

sleep 25s

kill $pid1
kill $pid2