import importlib
import os

from celery import Celery

env = os.environ.setdefault('REKINDLE_ENV', 'development')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'rekindle.settings.{env}')

app = Celery(main='rekindle', backend='redis://localhost:6379/0')
app.config_from_object(obj='django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {repr(self.request)}')


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    lightstage_tasks = importlib.import_module(name='.tasks', package='lightstage')
    sender.add_periodic_task(schedule=0.4, sig=lightstage_tasks.get_block_number.s(), name='get_block')
