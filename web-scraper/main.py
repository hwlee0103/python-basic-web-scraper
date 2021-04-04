from indeed import get_jobs as get_indeed_jobs
#from indeed import extract_indeed_pages, extract_indeed_jobs

indeed_jobs = get_indeed_jobs()

print(indeed_jobs)
#last_indeed_page = extract_indeed_pages()

#print(last_indeed_page)
#indeed_jobs = extract_indeed_jobs(last_indeed_page)

#print(indeed_jobs)
########indeed.py#####################
#need to install requests module
#import requests
#from bs4 import BeautifulSoup

#indeed_result = requests.get("https://www.indeed.com/jobs?q=python&limit=50")

#print(indeed_result.text)
#result: <Response [200]>

#indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")
#print(indeed_soup)

#pagination = indeed_soup.find("div", {"class":"pagination"})
#pagination = indeed_soup.find("ul", {"class":"pagination-list"})
#print(pagination)

#pages = pagination.find_all('a')
#links = pagination.find_all('a')
#print(pages)
#spans = []
#pages = []
#for page in pages:
#for link in links:
#for link in links[:-1]:
  #print(page.find("span"))
  #spans.append(page.find("span"))
  #spans.append(link.find("span"))
  #pages.append(link.find("span").string)
  #pages.append(int(link.string))

#print(spans)
#print(spans[-1])
#print(spans[:-1])
#spans = spans[:-1]
#print(pages)
#last page
#print(pages[-1])
#print(pages[:-1])
#pages = pages[:-1]
#max_page = pages[-1]

#-1 means from last item to first item
#print(spans[-1])
#0~5
#print(spans[0:5])

#requests
#print(range(max_page))

#for n in range(max_page):
#  print(f"start = {n*50}");

####################################