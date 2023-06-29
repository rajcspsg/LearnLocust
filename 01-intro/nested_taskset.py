import random

from locust import TaskSet, constant, task, HttpUser


class MyHttpCat(TaskSet):

    @task
    def get_status(self):
        self.client.get("/200")
        print("Get /200 endpoint")

    @task
    class MyAnotherHttpCat(TaskSet):

        @task
        def get_500_status(self):
            self.client.get("/500")
            print("Get 500 status")
            self.interrupt(reschedule=False)


class MyLoadTest(HttpUser):
    host = "https://http.cat"
    tasks = [MyHttpCat]
    wait_time = constant(1)
