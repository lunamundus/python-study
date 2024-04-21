import requests
from bs4 import BeautifulSoup

# Scraping Page URL
url = "https://weworkremotely.com/categories/remote-full-stack-programming-jobs"

# Get response from URL
response = requests.get(url)

# Used BS4
soup = BeautifulSoup(response.content, "html.parser")

# Get data from URL finding job section
jobs = soup.find("section", class_="jobs").find_all("li")[1:-1]

for job in jobs:
    try:
        title = job.find("span", class_="title").text
    except:
        title = ""
    try:
        region = job.find("span", class_="region").text
    except:
        region = ""
    try:
        company, position, _ = job.find_all("span", class_="company")
        company = company.text
        position = position.text
    except:
        company = ""
        position = ""
        
    print(title, '-----', region, '-----', company)