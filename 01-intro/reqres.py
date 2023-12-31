from locust import HttpUser, constant, task


class MyReqRes(HttpUser):

    host = "https://reqres.in"

    wait_time = constant(1)

    @task
    def get_users(self):
        res = self.client.get("/api/users?page=2")
        print(res.text)
        print(res.status_code)
        print(res.headers)

    @task
    def create_user(self):
        data = '''
        {"name":"morpheus","job":"leader"}
        '''
        res = self.client.post("/api/users", data=data)
        print(res.text)
        print(res.status_code)
        print(res.headers)