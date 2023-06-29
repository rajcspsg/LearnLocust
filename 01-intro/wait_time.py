import time
from datetime import datetime
from locust import User, task, constant, between, constant_pacing

import locust.stats

class MyUser(User):
    wait_time = constant_pacing(5)

    #@task
    def launch0(self):
        print("this will always inject 2-5 seconds delay" + str(datetime.now()))

    @task
    def launch(self):
        time.sleep(7)
        print("this is constant pacing behavior " + str(datetime.now()))
