from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def index():
    return '<h1>Доброе утро</h1><a>ef="/random_fact">Посмотреть случайный факт!</a>'

@app.route("/random_fact")
def random_fact():
    facts_list = ["Большинство людей, страдающих технологической зависимостью, испытывают сильный стресс, когда находятся вне зоны покрытия сети или не могут пользоваться своими устройствами.","Согласно исследованию, проведённому в 2018 году, более 50% людей в возрасте от 18 до 34 лет считают себя зависимыми от своих смартфонов.","Изучение технологической зависимости является одной из наиболее актуальных областей научных исследований в настоящее время.","Согласно исследованию, проведённому в 2019 году, более 60% людей отвечают на рабочие сообщения на своих смартфонах в течение 15 минут после того, как они ушли с работы."]
    return f'<p>{random.choice(facts_list)}</p>'
@app.route("/")
def index():
    return '<h2>Добрый вечер</h2><a>ef="/random_fact">Всё про геншин(почти)!</a>' 

@app.route("/Genshin")
def Genshin():
    Genshin = ["Как скачать геншин?https://www.bing.com/videos/riverview/relatedvideo?q=%d0%ba%d0%b0%d0%ba+%d1%81%d0%ba%d0%b0%d1%87%d0%b0%d1%82%d1%8c+%d0%b3%d0%b5%d0%bd%d1%88%d0%b8%d0%bd+%d0%bd%d0%b0+%d0%bd%d0%be%d1%83%d1%82%d0%b1%d1%83%d0%ba&mid=CAA52BCA61391D45E19CCAA52BCA61391D45E19C&FORM=VIRE","Как научиться играть в геншин?https://www.bing.com/videos/riverview/relatedvideo?q=%d0%ba%d0%b0%d0%ba+%d0%bd%d0%b0%d1%83%d1%87%d0%b8%d1%82%d1%8c%d1%81%d1%8f+%d0%b8%d0%b3%d1%80%d0%b0%d1%82%d1%8c+%d0%b2+%d0%b3%d0%b5%d0%bd%d1%88%d0%b8%d0%bd&mid=17EE8FF09183CF1AB3C917EE8FF09183CF1AB3C9&FORM=VIRE",'Как прокачать песронажа?https://www.bing.com/videos/riverview/relatedvideo?q=%d0%ba%d0%b0%d0%ba+%d0%bf%d1%80%d0%be%d0%ba%d0%b0%d1%87%d0%b0%d1%82+%d0%bf%d0%b5%d1%80%d1%81%d0%be%d0%bd%d0%b0%d0%b6%d0%b0+%d0%b2+%d0%b3%d0%b5%d0%bd%d1%88%d0%b8%d0%bd%d0%b5&mid=9C7247DF7A6C19D3FD8C9C7247DF7A6C19D3FD8C&FORM=VIRE']

app.run(debug=True)
