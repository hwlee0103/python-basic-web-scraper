#need to install requests module
import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"

def extract_indeed_pages():
  result = requests.get(URL)

#print(indeed_result.text)
#result: <Response [200]>

  soup = BeautifulSoup(result.text, "html.parser")
#print(indeed_soup)

#pagination = indeed_soup.find("div", {"class":"pagination"})
  pagination = soup.find("ul", {"class":"pagination-list"})
#print(pagination)

#pages = pagination.find_all('a')
  links = pagination.find_all('a')
#print(pages)
#spans = []
  pages = []
#for page in pages:
#for link in links:
  for link in links[:-1]:
  #print(page.find("span"))
  #spans.append(page.find("span"))
  #spans.append(link.find("span"))
  #pages.append(link.find("span").string)
    pages.append(int(link.string))

#print(spans)
#print(spans[-1])
#print(spans[:-1])
#spans = spans[:-1]
#print(pages)
#last page
  print(pages[-1])
#print(pages[:-1])
#pages = pages[:-1]
  max_page = pages[-1]

#-1 means from last item to first item
#print(spans[-1])
#0~5
#print(spans[0:5])

#requests
  print(range(max_page))
  return max_page

def extract_indeed_jobs(last_page):
  jobs = []
  for page in range(last_page):
    #print(f"&start={page*LIMIT}")
    result = requests.get(f"{URL}&start={page*LIMIT}")
    print(result.status_cod
    #result_code == 200 : request success
  return jobs

