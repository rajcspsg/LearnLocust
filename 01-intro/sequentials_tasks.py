from locust import SequentialTaskSet, HttpUser, constant, task

import locust.stats
locust.stats.PERCENTILES_TO_CHART=PERCENTILES_TO_CHART = [0.50, 0.75]

class MySeqTask(SequentialTaskSet):

    @task
    def get_status(self):
        self.client.get("/200")
        print("Status 200")

    @task
    def get_500_status(self):
        self.client.get("/500")
        print("status 500")


class MyLoadTest(HttpUser):
    host = "https://http.cat"
    tasks = [MySeqTask]
    wait_time = constant(1)
