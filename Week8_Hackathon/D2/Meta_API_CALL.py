import requests
import pandas as pd

# Define your access token and page ID
access_token = 'your_access_token'
page_id = 'your_page_id'

# Define the start and end date (use UNIX timestamps or date strings)
start_date = 'YYYY-MM-DD'
end_date = 'YYYY-MM-DD'

# Facebook Graph API URL
url = f"https://graph.facebook.com/v18.0/{page_id}/insights?metric=post_impressions,post_engagements&period=day&since={start_date}&until={end_date}&access_token={access_token}"

# Make the API request
response = requests.get(url)
data = response.json()

# Extract data and convert to a DataFrame for easy analysis
insights_data = data['data']
df = pd.DataFrame(insights_data)

# Export to CSV
df.to_csv('facebook_insights_data.csv', index=False)

print("Data Exported Successfully")
