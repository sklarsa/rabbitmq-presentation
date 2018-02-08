celery worker --app main --concurrency 1 -Q webapp &
pid1=$!
celery worker --app main --concurrency 3 -Q neural_net &
pid2=$!

python run.py

sleep 20s

kill $pid1
kill $pid2