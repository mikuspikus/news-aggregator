from celery import Celery
from queueconfig.celeryconfig import Config


app = Celery(include = ['celeryqueue.tasks'])
app.config_from_object(Config)

# celery -A celeryqueue worker -l info

if __name__ == "__main__":
    app.start()