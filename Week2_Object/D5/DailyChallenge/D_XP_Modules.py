import requests
import time

def measure_load_time(url):
    start_time = time.time()
    response = requests.get(url)
    end_time = time.time()
    
    load_time = end_time - start_time
    return load_time, response.status_code

# Testing the function with multiple sites
websites = [
    "https://www.google.com",
    "https://www.ynetnews.com",
    "https://www.imdb.com",
    "https://www.wikipedia.org"
]

for site in websites:
    load_time, status_code = measure_load_time(site)
    print(f"Website: {site} | Load Time: {load_time:.4f} seconds | Status Code: {status_code}")
