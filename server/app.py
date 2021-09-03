from flask import Flask,  render_template, request
from pathlib import Path
import json
configPath = Path.home()
configPath = Path(configPath).joinpath("aham_config/config.json")

f = open(configPath,)
config = json.load(f)
user= config['name']

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/user")
def getUser():
    print({'user':user})
    return json.dumps({'user':user})

@app.route("/library")
def library():
    filePath="/library/index.html"
    return render_template(filePath)

@app.route("/library/<path:dir>")
def libraryFiles(dir):
    filePath="/library/"+dir+"/index.html"
    return render_template(filePath)

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")
