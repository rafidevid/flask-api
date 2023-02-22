from flask import Flask
import requests
from bs4 import BeautifulSoup as parser

app = Flask(__name__)

space = "             "
url = "https://www.fakenamegenerator.com/"
author = {
    "name": "Rafi Khalbi",
    "github": "https://github.com/Rafikhalbi"
    }

def searching(key, p):
    for i in p.find_all("dl", class_="dl-horizontal"):
        if key in str(i):
            return i.find("dd").text
            
@app.route("/")
def home_app():
    data = {
        "desc": "this api for generete random data."
        }
    return {"result": data, "author": author}

@app.route("/randomdata")
def random_data():
    global author
    resp = requests.get(url, headers={"user-agent":"chrom"}).text
    p = parser(resp, "html.parser")
    name = p.find("h3").text
    adr = p.find("div", class_="adr").text.replace(space, "")
    phone = searching("Phone", p)
    birthday = searching("Birthday", p)
    age = searching("Age",p)
    height = searching("Height", p)
    weight = searching("Weight", p)
    data = {
        "name": name,
        "address": adr,
        "phone number": phone,
        "country code": "1",
        "age": age,"birthday": birthday, #i forget wkwkw
        "height": height,
        "weight": weight
        }
    return {"result": data, "author": author}

    
    
if __name__ == "__main__":
    app.run(debug= True)
