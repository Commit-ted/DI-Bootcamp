import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# For explicit waits
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize Selenium WebDriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--allow-running-insecure-content')

# Specify the Chrome binary path for Mac M1
chrome_options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Load the Web Page
url = "https://www.inmotionhosting.com/"
driver.get(url)

# Wait until the plans are loaded
wait = WebDriverWait(driver, 10)
plans = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".ihs-plan")))

hosting_data = []

for plan in plans:
    plan_name = plan.find_element(By.CSS_SELECTOR, ".ihs-plan__name").text
    price = plan.find_element(By.CSS_SELECTOR, ".ihs-plan__price").text
    features = [feature.text for feature in plan.find_elements(By.CSS_SELECTOR, ".ihs-plan__features li")]

    hosting_data.append({
        "Plan Name": plan_name,
        "Price": price,
        "Features": features
    })

# Store and Save the Data
df = pd.DataFrame(hosting_data)
df.to_csv("inmotion_hosting_plans.csv", index=False)

print(df)

# Close Selenium WebDriver
driver.quit()

print("Data has been scraped and saved to 'inmotion_hosting_plans.csv'")