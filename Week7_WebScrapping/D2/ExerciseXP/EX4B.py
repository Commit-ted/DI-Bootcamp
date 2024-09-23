from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd
from collections import defaultdict

# Initialize Selenium WebDriver (Make sure to have ChromeDriver installed)
# Change the path to your chromedriver executable
chrome_service = Service(executable_path='/Users/manuel/Desktop/Python_Apps/Python_AI_Web_Scraper/chromedriver')
driver = webdriver.Chrome(service=chrome_service)

# Open the Technology section of BBC News
driver.get('https://www.bbc.com/news/technology')
time.sleep(5)  # Allow the page to load

# Extract the page source
html = driver.page_source

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Find article titles and their publication dates
articles = soup.find_all('div', class_='gs-c-promo')

# Dictionary to store categorized articles by month
categorized_articles = defaultdict(list)

options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run Chrome in headless mode
options.add_argument("--no-sandbox")  # Bypass OS security model
options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
driver = webdriver.Chrome(options=options)

url = "https://www.bbc.com/innovation/technology"
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'html.parser')
news = soup.find_all("div", {"data-testid": 'edinburgh-card'})

for item in news:
    title_element = item.find('div', class_ = 'sc-4fedabc7-1 kbvCmj')
    summary_element = item.find('p', class_ = 'sc-b8778340-4 kYtujW')
    time_element = item.find('span', class_ = '')
    if title_element:
        title = title_element.text.strip()
    else:
        title = "Title not found"
    if summary_element:
        summary = summary_element.text.strip()
    else:
        summary = "Summary not found"
    print("Title:", title)
    print("Summary:", summary)
    print("----")

# Close the driver
driver.quit()

# Print the categorized lists of articles
for month, articles in categorized_articles.items():
    print(f"\nArticles for {month}:")
    for article in articles:
        print(f"Title: {article['title']}, Date: {article['date']}")

