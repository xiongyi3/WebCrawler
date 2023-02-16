import requests
import pandas as pd
from bs4 import BeautifulSoup

req = requests.get('https://www.goodreads.com/list/show/19.Best_for_Book_Clubs')
webpage = req.text
with open("filename", "wb") as f:
    f.write(webpage.encode())


soup = BeautifulSoup(webpage, 'html.parser')
results = soup.find_all("tr")

data = {"title":[], "author":[], "rating":[]}
for book in results:
 
    data["title"].append(book.find("a", class_="bookTitle").text.strip())
    data["author"].append(book.find("a", class_="authorName").text.strip())
    data["rating"].append(book.find("span", class_="minirating").text.strip())

df = pd.DataFrame(data)
df.to_csv('Popular_Books.csv',index=False)