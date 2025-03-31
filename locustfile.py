from locust import HttpUser, task, between

class APIUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def test_get_users(self):
        self.client.get("/users/1")

    @task
    def test_create_user(self):
        self.client.post("/users/", json={"name": "John Doe", "email": "john@example.com"})