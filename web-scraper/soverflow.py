import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://stackoverflow.com/jobs?q=python&sort=i"

def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    #print(soup)
    pages = soup.find("div", {"class":"s-pagination"}).find_all("a")
    #print(pages[-1])
    #print(pages[0:-2])
    #pages = pages[-2]
    #print(pages)
    last_page = pages[-2].get_text(strip=True)
    return last_page

def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        #print(page + 1)
        result = requests.get(f"{URL}&pg={page+1}")
        #print(result.status_code)
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class":"-job"})
        for result in results:
            print(result["data-jobid"])

def get_jobs():
    last_page = get_last_page()
    #print(last_page)
    jobs = extract_jobs(last_page)
    return []