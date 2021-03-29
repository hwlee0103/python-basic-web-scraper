#need to install requests module
import requests
from bs4 import BeautifulSoup


indeed_result = requests.get("https://www.indeed.com/jobs?q=python&limit=50")

#print(indeed_result.text)
#result: <Response [200]>

indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")
#print(indeed_soup)

#pagination = indeed_soup.find("div", {"class":"pagination"})
pagination = indeed_soup.find("ul", {"class":"pagination-list"})
#print(pagination)

pages = pagination.find_all('a')
#print(pages)
spans = []
for page in pages:
  #print(page.find("span"))
  spans.append(page.find("span"))
  #spans.append(page.find("b"))

#print(spans)
print(spans[-1])
print(spans[:-1])
pans = spans[:-1]

#-1 means from last item to first item
#print(spans[-1])
#0~5
#print(spans[0:5])