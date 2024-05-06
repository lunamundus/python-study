from playwright.sync_api import sync_playwright

# playwright 실행
playwright = sync_playwright().start()

# Browser 실행
browser = playwright.chromium.launch(headless=False)

# 새로운 Tab 생성
page = browser.new_page()

# 페이지 이동
page.goto(url="https://google.com")

# 해당 화면 스크린샷
page.screenshot(path="sc.png")