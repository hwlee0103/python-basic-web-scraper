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

def extract_jog(html):
  


##testing
def extract_indeed_jobs(last_page):
  jobs = []
##for page in range(last_page):
  #print(f"&start={page*LIMIT}")
  ##result = requests.get(f"{URL}&start={page*LIMIT}")
  result = requests.get(f"{URL}&start={0*LIMIT}")
  #print(result.status_code)
  soup = BeautifulSoup(result.text, "html.parser")
  results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})
  ##print(results)
  #result_code == 200 : request success
  for result in results:
    #print(result.find("div", {"class": "title"}).)
    title = result.find("h2", {"class": "title"}).find("a")["title"]
    #print(title)
    #sometimes company doesn't has link. so let's user if-else
    #company = result.find("span", {"class":"company"}).find("a")
    company = result.find("span", {"class":"company"})
    company_anchor = company.find("a")
    if company_anchor is not None:
      print(str(company_anchor.string))
    else:
      print(str(company.string))
    company = company.strip()
    print(company)
  return jobs
