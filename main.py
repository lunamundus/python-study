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

all_jobs = []

for job in jobs:
    title = job.find("span", class_="title").text

    region = job.find("span", class_="region")
    if region:
        region = region.text

    companies = job.find_all("span", class_="company")
    company = companies[0].text
    position = companies[1].text

    url = job.find("div", class_="tooltip--flag-logo").next_sibling
    if url:
        url = url["href"]           # html 태그에서 attribute를 추출하는 방법

    job_data = {
        "title": title,
        "company": company,
        "position": position,
        "region": region,
        "URL": f"https://weworkremotely.com{url}"
    }

    all_jobs.append(job_data)

print(all_jobs)