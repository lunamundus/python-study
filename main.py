import time

from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

# 변수 선언
jobs_db = []
keywords = ["flutter", "python", "react", "c++"]

# playwright 실행
playwright = sync_playwright().start()

# Browser 실행
browser = playwright.chromium.launch(headless=False)

# 새로운 Tab 생성
page = browser.new_page()

# 페이지 이동
page.goto(url="https://www.wanted.co.kr/")

time.sleep(1)

for keyword in keywords:
    page.click("button.Aside_searchButton__Xhqq3")
    time.sleep(1)

    page.get_by_placeholder("검색어를 입력해 주세요.").fill(keyword)
    time.sleep(1)

    page.keyboard.down("Enter")
    time.sleep(1)

    page.click("a#search_tab_position")
    time.sleep(1)

    for _ in range(5):
        page.keyboard.down("End")
        time.sleep(2)
    time.sleep(2)

    # html 가져오기
    content = page.content()

    soup = BeautifulSoup(content, "html.parser")

    jobs = soup.find_all("div", class_="JobCard_container__FqChn")

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

# playwright 종료
playwright.stop()

print(jobs_db)
print(len(jobs_db))