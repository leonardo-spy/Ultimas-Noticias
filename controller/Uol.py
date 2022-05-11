
import requests
from bs4 import BeautifulSoup

from models.Uol_noticia import Uol_noticia

UOL_URL = "https://noticias.uol.com.br/ultimas/"


class Uol():
    def __init__(self):
        pass

    def run(self):
        session = requests.Session()
        response = session.get(UOL_URL)
        response.encoding = "utf-8"
        soup = BeautifulSoup(response.text, 'lxml')
        divs = soup.find("div", {'class': 'results-items'}).find("div", {'class': 'thumbnails'}, recursive=False).find("div", {'class': 'row'}, recursive=False).find("div", {'class': 'flex-wrap'}, recursive=False).find_all("div", recursive=False)
        for noticia in divs:
            if  noticia.find("div", {'class': 'ads-wrapper'}, recursive=False):
                continue            
            noticia_base = noticia.find("div", recursive=False).find("a", recursive=False, href=True)
            link = noticia_base['href'].strip()
            body_figure = noticia_base.find("figure", recursive=False)
            if body_figure:
                body_img = body_figure.find("img", recursive=True)
                imagem_link = body_img['data-src'].strip()
            else:
                imagem_link = None
            content = noticia_base.find("div", recursive=False)
            tipo_materia = content.find("span", recursive=False).text.strip()
            body_text = content.find("h3", recursive=False).text.strip()
            data = content.find("time", recursive=False).text.strip()
            
            template = Uol_noticia(link,imagem_link,tipo_materia,body_text,data)
            template.insert()