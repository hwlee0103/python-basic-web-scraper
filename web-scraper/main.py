#need to install requests module
import requests
from bs4 import BeautifulSoup


indeed_result = requests.get("https://www.indeed.com/jobs?q=python&limit=50")

#print(indeed_result.text)
#result: <Response [200]>

indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")
print(indeed_soup)