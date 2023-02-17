from flask import Flask, render_template
from newspaper import Article
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('hola.html')

@app.route('/count/')
def count():
    a = 20
    print(a)
    return ('a')

@app.route('/article/')
def article():
    #A new article from TOI
    url = "https://elpais.com/deportes/2023-02-16/el-fc-barcelona-pago-al-vicepresidente-de-arbitros-enriquez-negreira-siete-millones-desde-2001-por-supuestas-asesorias-verbales.html"

    #For different language newspaper refer above table
    toi_article = Article(url, language="en") # en for English

    #To download the article
    toi_article.download()

    #To parse the article
    toi_article.parse()

    #To perform natural language processing ie..nlp
    toi_article.nlp()

    #To extract title
    print("Article's Title:")
    print(toi_article.title)
    print("n")

    #To extract text
    print("Article's Text:")
    print(toi_article.text)
    print("n")

    #To extract summary
    print("Article's Summary:")
    print(toi_article.summary)
    print("n")

    #To extract keywords
    print("Article's Keywords:")
    print(toi_article.keywords)
    return(toi_article.title, 'hola hola!')
