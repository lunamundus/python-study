import time

from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

# load job page by playwright
def load_wanted_job_page(keyword):
    # start playwright
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto(url=f"https://www.wanted.co.kr/search?query={keyword}&tab=position")
    time.sleep(1)
    # page scroll down
    for _ in range(5):
        page.keyboard.down("End")
        time.sleep(2)
    
    content = page.content()
    return content


# page scrape by bs4
def wanted_job_page_scrape(keyword):
    content = load_wanted_job_page(keyword=keyword)
    
    soup = BeautifulSoup(content, "html.parser")
    jobs = soup.find_all("div", class_="JobCard_container__FqChn")

    jobs_db = []
    for job in jobs:
        link = f'https://www.wanted.co.kr{job.find("a")["href"]}'
        title = job.find("strong", class_="JobCard_title__ddkwM").text
        company_name = job.find("span", class_="JobCard_companyName__vZMqJ").text
        reward = job.find("span", class_="JobCard_reward__sdyHn").text
        language = job.find("a")["data-search-value"]

        job_data = {
            "title": title,
            "company_name": company_name,
            "language": language,
            "reward": reward,
            "link": link
        }

        jobs_db.append(job_data)
    
    return jobs_db