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

def extract_job(html):
    #html changed :)
    title = html.find("h2", {"class":"mb4"}).find("a")["title"]
    #below line could be okay?
    #title = html.find("h2").find("a")["title"]
    #print(title)
    #company_row = html.find("h3", {"class":"mb4"}).find_all("span", recursive=False)
    company, location = html.find("h3", {"class":"mb4"}).find_all("span", recursive=False)
    #below line could be okay?
    #company, location = html.find("h3").find_all("span", recursive=False)
    #print(company_row)
    #company = company_row[0]
    #location = company_row[1]
    #print(company.string, location.string)
    #print(company.get_text(strip=True).strip("-"), location.get_text(strip=True).strip("-"))
    company = company.get_text(strip=True)
    location = location.get_text(strip=True).strip("-").strip(" \r").strip("\n")
    #print(company, location)
    job_id = html['data-jobid']
    return {'title': title, 'company': company, 'location': location, 'link':f"https://stackoverflow.com/jobs/{job_id}"}

def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f"Scrapping StackOverflow Page: {page}")
        #print(page + 1)
        result = requests.get(f"{URL}&pg={page+1}")
        #print(result.status_code)
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class":"-job"})
        for result in results:
            #print(result["data-jobid"])
            job = extract_job(result)
            #print(job)
            jobs.append(job)
    return jobs

def get_jobs():
    last_page = get_last_page()
    #print(last_page)
    jobs = extract_jobs(last_page)
    #jobs = extract_jobs(2)
    return jobs