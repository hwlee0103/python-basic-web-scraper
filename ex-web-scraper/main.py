from flask import Flask, render_template, request, redirect, send_file
from scrapper import get_jobs
from exporter import save_to_file

app = Flask("SuperScrapper")

db = {}

@app.route("/")
def home():
    #return "Hello! Welcome to mi casa!"
    #return "<h1>Job Search</h1><form><input placeholder='What job do you want?' required /><button>Search</button>"
    return render_template("potato.html")

@app.route("/report")
def report():
    #print(request.args.get('word'))
    word = request.args.get('word')
    if word:
        word = word.lower()
        existingJobs = db.get(word)
        if existingJobs:
            jobs = existingJobs
        else:
            jobs = get_jobs(word)
            db[word] = jobs
    else:
        return redirect("/")
    return render_template("report.html", searchingBy=word, potato="hello", resultsNumber=len(jobs), jobs=jobs)
    #return f"You are looking for a job in {word}"
    #return "this is the report"

@app.route("/export")
def export():
    try:
        word = request.args.get('word')
        if not word:
            raise Exception()
        word = word.lower()
        jobs = db.get(word)
        if not jobs:
            raise Exception()
        save_to_file(jobs)
        return send_file("jobs.csv")
        #return f"Generate CSV for {word}"
    except:
        return redirect("/")
    #word = request.args.get('word')
    #if word:
    #    word = word.lower()
    #else:
    #    return redirect("/")

#@app.route("/contact")
@app.route("/<username>")
#def contact():
#it is okay to use different name on function
def potato(username): 
    #return "Contact me!"
    return f"Hello {username} how are you doing"

app.run(host="0.0.0.0")

