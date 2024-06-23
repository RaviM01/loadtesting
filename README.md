# loadtesting
Loadtesting using locust

pip install locust
locust --headless -f main.py -u 1 -r 1 -H https://www.demoblaze.com -t 30s