
import requests
from bs4 import BeautifulSoup

from models.Estadao_noticia import Estadao_noticia

ESTADAO_URL = "https://www.estadao.com.br/ultimas/"


class Estadao():
    def __init__(self):
        pass

    def run(self):
        session = requests.Session()
        response = session.get(ESTADAO_URL)
        response.encoding = "utf-8"
        soup = BeautifulSoup(response.text, 'lxml')
        divs = soup.find("div", {'class': 'lista'}).select('section[class*="item-lista"]')
        for noticia in divs:
            body = noticia.find("div", recursive=False).find("div", {'class': 'row'}, recursive=False)
            sections = body.find_all("section", recursive=False)
            section_top = sections[0].find("a", recursive=False)
            link = section_top['href'].strip()
            titulo = section_top.find("h3", recursive=False).text.strip()
            noticia_base = section_top.find("p", recursive=False)
            if noticia_base:
                body_text = noticia_base.text.strip()
            else:
                body_text = None
            credito = sections[0].find("span", {'class': 'credito-posts'}, recursive=False).text.strip()
            data = sections[0].find("span", {'class': 'data-posts'}, recursive=False).text.strip()

            body_figure = sections[1].find("figure", recursive=False)
            if body_figure:
                body_img = body_figure.find("img", recursive=True)
                imagem_link = body_img['src'].strip()
            else:
                imagem_link = None
            
            template = Estadao_noticia(link,titulo,body_text,credito,data,imagem_link)
            template.insert()