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

for article in articles:
    title_tag = article.find('h3')
    date_tag = article.find('time')
    
    if title_tag and date_tag:
        title = title_tag.text.strip()
        date = date_tag['datetime']
        
        # Parse the month from the date (assuming date format is YYYY-MM-DD)
        month = pd.to_datetime(date).strftime('%B')
        
        # Categorize articles by month
        categorized_articles[month].append({
            'title': title,
            'date': date
        })

# Close the driver
driver.quit()

# Print the categorized lists of articles
for month, articles in categorized_articles.items():
    print(f"\nArticles for {month}:")
    for article in articles:
        print(f"Title: {article['title']}, Date: {article['date']}")

