import requests
from bs4 import BeautifulSoup

# Scraping Page URL
url = "https://weworkremotely.com/categories/remote-full-stack-programming-jobs"

# Get response from URL
response = requests.get(url)

# Used BS4
soup = BeautifulSoup(response.content, "html.parser")

# Get data from URL finding job section
jobs = soup.find("section", class_="jobs").find_all("li")