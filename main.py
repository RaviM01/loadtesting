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

        wait_time = between(1, 5)
        @task
        def mainPage(self):
            self.client.get("/")
            self.client.get("https://api.demoblaze.com/entries")
        @task
        def login(self):
            self.client.options("https://api.demoblaze.com/login")
            self.client.post("https://api.demoblaze.com/login",json={"username":"aaaa","password":"YWFhYQ=="})
            self.client.options("https://api.demoblaze.com/check")
            self.client.get("https://api.demoblaze.com/entries")
            self.client.post("https://api.demoblaze.com/check",json={"token":"YWFhYTE2MzA5NDU="})            
        @task
        def clickProduct(self):
            self.client.get("/prod.html?idp_=1")
            self.client.options("https://api.demoblaze.com/check")
            self.client.options("https://api.demoblaze.com/view")
            self.client.post("https://api.demoblaze.com/check",json={"token":"YWFhYTE2MzA5NDU="})
            self.client.post("https://api.demoblaze.com/view",json={"id":"1"})
        @task
        def addToCart(self):
            self.client.options("https://api.demoblaze.com/addtocart")
            self.client.post("https://api.demoblaze.com/addtocart",json={"id":"fb3d5d23-f88c-80d9-a8de-32f1b6034bfd","cookie":"YWFhYTE2MzA5NDU=","prod_id":1,"flag":'true'})
        @task 
        def viewCart(self):
            self.client.get("/cart.html")
            self.client.options("https://api.demoblaze.com/check")
            self.client.options("https://api.demoblaze.com/viewcart")
            self.client.post("https://api.demoblaze.com/check",json={"token":"YWFhYTE2MzA5NDU="})
            self.client.post("https://api.demoblaze.com/viewcart",json={"cookie":"YWFhYTE2MzA5NDU=","flag":'true'})
            self.client.options("https://api.demoblaze.com/view")
            self.client.post("https://api.demoblaze.com/check",json={"token":"YWFhYTE2MzA5NDU="})
            self.client.post("https://api.demoblaze.com/view",json={"id":"1"})