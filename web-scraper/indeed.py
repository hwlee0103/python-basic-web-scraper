#need to install requests module
import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"

def get_last_page():
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

def extract_job(html):
  #print(result.find("div", {"class": "title"}).)
    title = html.find("h2", {"class": "title"}).find("a")["title"]
    #print(title)
    #sometimes company doesn't has link. so let's user if-else
    #company = result.find("span", {"class":"company"}).find("a")
    company = html.find("span", {"class":"company"})
    if company:
      company_anchor = company.find("a")
      if company_anchor is not None:
        #print(str(company_anchor.string))
        company = str(company_anchor.string)
      else:
        #print(str(company.string))
        company = str(company.string)
      company = company.strip()
    #extract location
    #location = html.find("span", {"class": "location"}).string
    else:
      company = None
    location = html.find("div", {"class": "recJobLoc"})["data-rc-loc"]
    #print(location)
    job_id = html["data-jk"]
    #print(job_id)
    return {'title': title, 'company': company, 'location': location, 'link': f"httpls://www.indeed.com/viewjob?jk{job_id}"}


##testing
def extract_jobs(last_page):
  jobs = []
  for page in range(last_page):
    print(f"Scrapping Indeed Page: {page}")
    #print(f"Scrapping page {page}")
    #print(f"&start={page*LIMIT}")
    result = requests.get(f"{URL}&start={page*LIMIT}")
    #result = requests.get(f"{URL}&start={0*LIMIT}")
    #print(result.status_code)
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})
    ##print(results)
    #result_code == 200 : request success
    for result in results:
      job = extract_job(result)
      #print(job)
      jobs.append(job)
  return jobs

def get_jobs():
  last_page = get_last_page()
  jobs = extract_jobs(last_page)
  return jobs