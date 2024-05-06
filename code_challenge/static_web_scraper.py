import requests
from bs4 import BeautifulSoup

class WebScrapper:
    def __init__(self, url, headers):
        self.url = url
        self.headers = headers

    def scrape_page(self):
        # Get response from URL
        response = requests.get(url=self.url, headers=self.headers)

        # Used BS4
        soup = BeautifulSoup(response.content, "html.parser")

        # Get data from URL finding job section
        jobs = soup.find("table", id="jobsboard").find_all("td", class_="company_and_position")[1:]

        return jobs

class Jobs(WebScrapper):
    def __init__(self, url, headres=""):
        super().__init__(url=url, headers=headres)
        self.job_data = {}

    def add_jobs_data(self):
        web_response = WebScrapper(url=self.url, headers=headers)
        jobs = web_response.scrape_page()

        all_jobs = []

        for job in jobs:
            title = job.find("h2").text
            company = job.find("h3").text
            location = job.find("div", class_="location").text
            if "💰" in location:
                location = "" 

            self.job_data = {
                "title": title.rstrip().lstrip(),
                "company": company.rstrip().lstrip(),
                "location": location.rstrip().lstrip()
            }

            all_jobs.append(self.job_data)
        
        return all_jobs

keywords = ['flutter', 'python', 'golang']
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Whale/3.25.232.19 Safari/537.36"}

all_jobs = []
for keyword in keywords:
    url = f"https://remoteok.com/remote-{keyword}-jobs"
    jobs = Jobs(url=url, headres=headers)
    all_jobs = all_jobs + jobs.add_jobs_data()

print(all_jobs)