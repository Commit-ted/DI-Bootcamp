from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode if necessary
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Manually specify the correct path to your chromedriver
service = Service("/opt/homebrew/bin/chromedriver")

driver = webdriver.Chrome(service=service, options=chrome_options)

# Test the setup
driver.get("https://www.google.com")
print(driver.title)

# Close the browser when done
driver.quit()