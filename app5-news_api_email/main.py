import requests
from send_mails import send_mail

topic = "thalapathy"

url = "https://newsapi.org/v2/everything?"\
    f"q={topic}&"\
    "from=2024-08-15&"\
    "sortBy=publishedAt&"\
    "apiKey=1b006b5ce2394ddd9be83a6406456cf1&"\
    "language=en"

#Made request to newsapi and get the json content
request = requests.get(url)
content = request.json()

body = ""
for article in content["articles"][:20]:
    title = article["title"]
    description = article["description"]
    link = article["url"]
    
    if title is not None and description is not None:
        body += "Subject: Today's news"\
            + "\n" + title + "\n" + description + "\n" + link + 2*"\n"

body = body.encode("utf-8")
send_mail(body)