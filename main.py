from requests import get

websites = (
    "google.com",
    "airbnb.com",
    "https://twitter.com",
    "facebook.com",
    "https://tiktok.com"
)

result = {}

for website in websites:
    if not website.startswith("https://"):      # if website.startswith("https://") == False:
        website = f"https://{website}"
    
    response = get(website)

    if response.status_code == 200:
        result[website] = "OK"
    else:
        result[website] = "FAILED"

print(result)