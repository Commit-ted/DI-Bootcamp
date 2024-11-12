from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
from datetime import datetime

# 🌟 Exercise 1: Parsing HTML with BeautifulSoup
print("🌟 Exercise 1: Parsing HTML with BeautifulSoup\n")
html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sports World</title>
</head>
<body>
    <header>
        <h1>Welcome to Sports World</h1>
        <p>Your one-stop destination for the latest sports news and videos.</p>
    </header>
    <nav>
        <a href="#football">Football</a>
        <a href="#basketball">Basketball</a>
        <a href="#tennis">Tennis</a>
    </nav>
    <section id="football">
        <p>Football section content.</p>
    </section>
</body>
</html>
"""
soup = BeautifulSoup(html_content, "html.parser")
title = soup.title.string
print("Page Title:", title)

paragraphs = soup.find_all('p')
print("\nParagraphs:")
for p in paragraphs:
    print(p.get_text())

links = soup.find_all('a', href=True)
print("\nLinks:")
for link in links:
    print(link['href'])

# 🌟 Exercise 2: Scraping `robots.txt` from Wikipedia
print("\n🌟 Exercise 2: Scraping `robots.txt` from Wikipedia\n")
url = "https://en.wikipedia.org/robots.txt"
response = requests.get(url)
if response.status_code == 200:
    print("robots.txt content:\n")
    print(response.text[:500])  # Print first 500 characters for brevity
else:
    print("Failed to fetch robots.txt")

# 🌟 Exercise 3: Extracting Headers from Wikipedia’s Main Page
print("\n🌟 Exercise 3: Extracting Headers from Wikipedia’s Main Page\n")
url = "https://en.wikipedia.org/wiki/Main_Page"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
headers = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
print("\nHeaders from Wikipedia:")
for header in headers:
    print(header.name, ":", header.get_text().strip())

# 🌟 Exercise 4: Checking for Page Title
print("\n🌟 Exercise 4: Checking for Page Title\n")
url = "https://en.wikipedia.org/wiki/Main_Page"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
if soup.title:
    print("Page Title:", soup.title.string)
else:
    print("No title found.")

# 🌟 Exercise 5: Analyzing US-CERT Security Alerts
print("\n🌟 Exercise 5: Analyzing US-CERT Security Alerts\n")
url = "https://www.cisa.gov/uscert/ncas/alerts"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
current_year = datetime.now().year
alerts = soup.find_all("a", href=True, text=lambda t: str(current_year) in t)
print(f"Number of Security Alerts in {current_year}: {len(alerts)}")

# 🌟 Exercise 6: Scraping Movie Details
print("\n🌟 Exercise 6: Scraping Movie Details\n")
url = "https://www.imdb.com/chart/top/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
movies = soup.select("td.titleColumn")
summaries = soup.select("td.titleColumn a")
print("\nTop 10 Movies:")
for i in range(10):
    movie = movies[i].get_text(strip=True)
    summary = summaries[i]['title']
    print(f"{i+1}. {movie} - {summary}")
