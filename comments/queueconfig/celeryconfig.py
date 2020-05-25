import os

PASSWORD = os.environ.get('R_PWD', '')
if PASSWORD:
    PASSWORD = f":{PASSWORD}@"
HOST = os.environ.get('R_HOST', 'localhost')
PORT = os.environ.get('R_PORT', '6379')
DB = os.environ.get('R_DB', '0')

class Config:
    accept_content = {'json'}
    broker_url = f"redis://{PASSWORD}{HOST}:{PORT}/{DB}"
    task_soft_time_limit=30,
    task_time_limit=120,