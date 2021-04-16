from flask import Flask, render_template

app = Flask("SuperScrapper")

@app.route("/")
def home():
    #return "Hello! Welcome to mi casa!"
    #return "<h1>Job Search</h1><form><input placeholder='What job do you want?' required /><button>Search</button>"
    return render_template("potato.html")

#@app.route("/contact")
@app.route("/<username>")
#def contact():
#it is okay to use different name on function
def potato(username): 
    #return "Contact me!"
    return f"Hello {username} how are you doing"

app.run(host="0.0.0.0")

