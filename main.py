from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all("a", {"rel": "noreferrer"})
articles_text = [item.getText() for item in articles]
articles_links = [item.get("href") for item in articles]

article_upvote = [int(item.getText().split()[0]) for item in soup.find_all("span", {"class": "score"})]

max_upvote = max(article_upvote)
max_index = article_upvote.index(max_upvote)
print(articles_text[max_index], articles_links[max_index], max_upvote)
