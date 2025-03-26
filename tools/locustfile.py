# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "locust",
# ]
# ///
import datetime
import logging

from locust import HttpUser, task, between
from locust.env import Environment, WebUI


logger = logging.getLogger()


class ApiUser(HttpUser):
    host = "http://127.0.0.1:8000"
    wait_time = between(1, 2)  # seconds between tasks

    @task
    def get_items(self):
        self.client.get("/items/")  # adjust the endpoint path as needed

    @task
    def create_item(self):
        payload = {
            "name": f"Test Item {datetime.datetime.now()}"
        }
        self.client.post("/items/", json=payload)

if __name__ == '__main__':
    env = Environment(user_classes=[ApiUser])
    env.create_local_runner()
    web_ui: WebUI = env.create_web_ui()
    logger.warning("Starting locust server at %s:%s",web_ui.host, web_ui.port)
    env.web_ui.greenlet.join()