from locust import HttpUser, SequentialTaskSet, task, between, events

@events.init.add_listener
def init(environment, **_kwargs):
    print("2. Initializing locust, happens after parsing the locustfile but before test start")


@events.quitting.add_listener
def quitting(environment, **_kwargs):
    print("9. locust is about to shut down")

@events.quit.add_listener
def quit(exit_code, **kwargs):
    print(f"10. Locust has shut down with code {exit_code}")
         
class User(HttpUser):
  
    @task
    class SequenceOfTasks(SequentialTaskSet):
        wait_time = between(0, 1)
        @task
        def login(self):
            self.client.post("https://api.demoblaze.com/login",json={"username":"aaaa","password":"YWFhYQ=="})
            self.client.get("https://api.demoblaze.com/entries")