from requests import get

websites = (
    "google.com",
    "airbnb.com",
    "https://twitter.com",
    "facebook.com",
    "https://tiktok.com",
    "https://httpstat.us/200",
    "httpstat.us/302",
    "https://httpstat.us/505",
    "httpstat.us/404",
    "httpstat.us/101"
)

result = {}

for website in websites:
    if not website.startswith("https://"):      # if website.startswith("https://") == False:
        website = f"https://{website}"
    
    response = get(website)

    if response.status_code >= 500:
        result[website] = "Server Error"
    elif response.status_code >= 400:
        result[website] = "Client Error"
    elif response.status_code >= 300:
        result[website] = "Redirection"
    elif response.status_code >= 200:
        result[website] = "Success!"
    elif response.status_code >= 100:
        result[website] = "Informational"
    else:
        result[website] = "What's wrong...?"

print(result)