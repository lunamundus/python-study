import time

from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

# playwright 실행
playwright = sync_playwright().start()

# Browser 실행
browser = playwright.chromium.launch(headless=False)

# 새로운 Tab 생성
page = browser.new_page()

# 페이지 이동
page.goto(url="https://www.wanted.co.kr/")

time.sleep(2)

page.click("button.Aside_searchButton__Xhqq3")

time.sleep(2)

page.get_by_placeholder("검색어를 입력해 주세요.").fill("flutter")

time.sleep(2)

page.keyboard.down("Enter")

time.sleep(2)

page.click("a#search_tab_position")

time.sleep(2)

for _ in range(5):
    page.keyboard.down("End")
    time.sleep(2)

time.sleep(3)

# html 가져오기
content = page.content()

# playwright 종료
playwright.stop()


soup = BeautifulSoup(content, "html.parser")