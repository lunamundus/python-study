import requests
from bs4 import BeautifulSoup

all_jobs = []

def scrape_page(url):
    # Get response from URL
    response = requests.get(url)

    # Used BS4
    soup = BeautifulSoup(response.content, "html.parser")

    # Get data from URL finding job section
    jobs = soup.find("section", class_="jobs").find_all("li")[1:-1]

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
            try:
                url = url["href"]
            except:
                url = ""

        job_data = {
            "title": title,
            "company": company,
            "position": position,
            "region": region,
            "URL": f"https://weworkremotely.com{url}"
        }

        all_jobs.append(job_data)

def get_pages(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    pages = len(soup.find("div", class_="pagination").find_all("span", class_="page"))
    return pages

total_pages = get_pages('https://weworkremotely.com/remote-full-time-jobs?page=1')

for page in range(1, total_pages+1):
    url = f'https://weworkremotely.com/remote-full-time-jobs?page={page}'
    scrape_page(url)

print(len(all_jobs))