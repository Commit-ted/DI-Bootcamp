from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pprint  # To tidy up

driver = webdriver.Chrome()

# Navigate to the Rotten Tomatoes Certified Fresh Movies page
driver.get("https://www.rottentomatoes.com/browse/movies_in_theaters/critics:certified_fresh~sort:popular")

# Wait for the page to load
driver.implicitly_wait(10)

# Print the page title
print(driver.title)

# # Close the browser window
# driver.quit()