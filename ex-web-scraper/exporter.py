import csv

def save_to_file(jobs):
    file = open("jobs.csv", mode="w")
    #print(file)
    writer = csv.writer(file)
    writer.writerow(["title", "company", "location", "link"])
    #print(jobs)
    for job in jobs:
        #writer.writerow(job)
        #print(list(job.values()))
        writer.writerow(list(job.values()))
    return
    