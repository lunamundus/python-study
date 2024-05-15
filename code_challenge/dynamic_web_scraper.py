import time
import csv

from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

### ===== OOP ===== ###

class job_scraper:
    def __init__(self, keywords):
        self.keywords = keywords

        for keyword in self.keywords:
            url = f"https://www.wanted.co.kr/search?query={keyword}&tab=position"

            print(f"{keyword} 페이지 접속 중...")
            content = self.load_job_page(url)
            print(f"{keyword} 페이지 접속 완료!")

            print(f"{keyword} 일자리 스트랩 중...")
            job_data = self.page_scrape(content)
            print(f"{keyword} 일자리 스트랩 완료!")

            print(f"CSV 파일로 변환 중...")
            self.make_to_csv_file(keyword, job_data)
            print(f"파일 변환 완료!")
            print(f"==========")
    
    # load job page by playwright
    def load_job_page(self, url):
        # start playwright
        playwright = sync_playwright().start()
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto(url=url)
        time.sleep(1)
        # page scroll down
        for _ in range(5):
            page.keyboard.down("End")
            time.sleep(2)
        
        content = page.content()
        playwright.stop()

        return content

    # page scrape by bs4
    def page_scrape(self, content):
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

    # convert to CSV file
    def make_to_csv_file(self, keyword, job_data):
        job_file = open(f"{keyword}_jobs.csv", mode='w', encoding="cp949")
        writter = csv.writer(job_file)
        writter.writerow(["Title", "Company", "Language", "Reward", "Link"])

        for job in job_data:
            writter.writerow(job.values())

        job_file.close()


keywords = ["flutter", "python", "nextjs", "kotlin"]
job_scraper(keywords=keywords)





### ===== Function Programming ===== ###

# # load job page by playwright
# def load_job_page(url):
#     # start playwright
#     playwright = sync_playwright().start()
#     browser = playwright.chromium.launch(headless=False)
#     page = browser.new_page()

#     page.goto(url=url)
#     time.sleep(1)
#     # page scroll down
#     for _ in range(5):
#         page.keyboard.down("End")
#         time.sleep(2)
    
#     content = page.content()
#     return content


# # page scrape by bs4
# def page_scrape(content):
#     soup = BeautifulSoup(content, "html.parser")
#     jobs = soup.find_all("div", class_="JobCard_container__FqChn")

#     jobs_db = []
#     for job in jobs:
#         link = f'https://www.wanted.co.kr{job.find("a")["href"]}'
#         title = job.find("strong", class_="JobCard_title__ddkwM").text
#         company_name = job.find("span", class_="JobCard_companyName__vZMqJ").text
#         reward = job.find("span", class_="JobCard_reward__sdyHn").text
#         language = job.find("a")["data-search-value"]

#         job_data = {
#             "title": title,
#             "company_name": company_name,
#             "language": language,
#             "reward": reward,
#             "link": link
#         }

#         jobs_db.append(job_data)
    
#     return jobs_db


# # convert to CSV file
# def make_to_csv_file(keyword, job_data):
#     job_file = open(f"{keyword}_jobs.csv", mode='w', encoding="cp949")
#     writter = csv.writer(job_file)
#     writter.writerow(["Title", "Company", "Language", "Reward", "Link"])

#     for job in job_data:
#         writter.writerow(job.values())

#     job_file.close()


# keywords = ["flutter", "python", "nextjs", "kotlin"]

# for keyword in keywords:
#     url = f"https://www.wanted.co.kr/search?query={keyword}&tab=position"

#     print(f"{keyword} 페이지 접속 중...")
#     content = load_job_page(url)
#     print(f"{keyword} 페이지 접속 완료!")

#     print(f"{keyword} 페이지 스크랩 진행 중...")
#     job_data = page_scrape(content)
#     print(f"{keyword} 일자리 스크랩 완료!")

#     print(f"CSV 파일로 변환 중...")
#     make_to_csv_file(keyword, job_data)

#     print(f"==========")





### ===== Basic Code ===== ###

# # 변수 선언
# jobs_db = []
# keywords = ["flutter", "python", "react", "c++"]

# # playwright 실행
# playwright = sync_playwright().start()

# # Browser 실행
# browser = playwright.chromium.launch(headless=False)

# # 새로운 Tab 생성
# page = browser.new_page()

# # 페이지 이동
# page.goto(url="https://www.wanted.co.kr/")

# time.sleep(1)

# for keyword in keywords:
#     page.click("button.Aside_searchButton__Xhqq3")
#     time.sleep(1)

#     page.get_by_placeholder("검색어를 입력해 주세요.").fill(keyword)
#     time.sleep(1)

#     page.keyboard.down("Enter")
#     time.sleep(1)

#     page.click("a#search_tab_position")
#     time.sleep(1)

#     for _ in range(5):
#         page.keyboard.down("End")
#         time.sleep(2)
#     time.sleep(2)

#     # html 가져오기
#     content = page.content()

#     soup = BeautifulSoup(content, "html.parser")

#     jobs = soup.find_all("div", class_="JobCard_container__FqChn")

#     for job in jobs:
#         link = f'https://www.wanted.co.kr{job.find("a")["href"]}'
#         title = job.find("strong", class_="JobCard_title__ddkwM").text
#         company_name = job.find("span", class_="JobCard_companyName__vZMqJ").text
#         reward = job.find("span", class_="JobCard_reward__sdyHn").text
#         language = job.find("a")["data-search-value"]

#         job_data = {
#             "title": title,
#             "company_name": company_name,
#             "language": language,
#             "reward": reward,
#             "link": link
#         }

#         jobs_db.append(job_data)

# # playwright 종료
# playwright.stop()

# print(len(jobs_db))

# job_file = open("jobs.csv", mode='w', encoding="cp949")
# writter = csv.writer(job_file)
# writter.writerow(["Title", "Company", "Language", "Reward", "Link"])

# for job in jobs_db:
#     writter.writerow(job.values())

# job_file.close()