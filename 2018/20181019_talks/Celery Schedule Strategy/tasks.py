from time import sleep
from celery import Celery

app = Celery('tasks', broker='pyamqp://guest@localhost//', backend='redis://localhost') 

@app.task
def show(symbol, time_count):
    for m in range(time_count):
        print(symbol * time_count)
        sleep(1)
    return symbol
