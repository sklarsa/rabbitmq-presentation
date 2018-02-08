from celery import Celery

import celeryconfig

app = Celery()
app.config_from_object(celeryconfig)

