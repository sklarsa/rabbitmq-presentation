celery worker --app main --concurrency 4 &
pid1=$!
python run.py

sleep 25s

kill $pid1